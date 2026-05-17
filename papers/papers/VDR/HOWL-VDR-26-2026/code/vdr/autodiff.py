# code/vdr/autodiff.py
from __future__ import annotations

from fractions import Fraction
from typing import List, Optional, Sequence, Set, Union

from .vdr import VDR
from .linalg import Vec, Mat


ScalarLike = Union[VDR, int, Fraction]


def _to_vdr(x: ScalarLike) -> VDR:
    if isinstance(x, VDR):
        return x
    if isinstance(x, Fraction):
        return VDR.from_fraction(x)
    return VDR(int(x))


def _zero() -> VDR:
    return VDR(0)


def _one() -> VDR:
    return VDR(1)


class Node:
    def __init__(
        self,
        value: ScalarLike,
        parents: Optional[Sequence["Node"]] = None,
        op: str = "",
        name: Optional[str] = None,
    ):
        self.value = _to_vdr(value)
        self.grad = VDR(0)
        self.parents = list(parents) if parents is not None else []
        self.op = op
        self.name = name
        self._backward = lambda: None

    def zero_grad(self):
        self.grad = VDR(0)

    def __add__(self, other):
        other = ensure_node(other)
        out = Node(self.value + other.value, [self, other], op="add")

        def _backward():
            self.grad = self.grad + out.grad
            other.grad = other.grad + out.grad

        out._backward = _backward
        return out

    def __radd__(self, other):
        return ensure_node(other) + self

    def __sub__(self, other):
        other = ensure_node(other)
        out = Node(self.value - other.value, [self, other], op="sub")

        def _backward():
            self.grad = self.grad + out.grad
            other.grad = other.grad - out.grad

        out._backward = _backward
        return out

    def __rsub__(self, other):
        return ensure_node(other) - self

    def __mul__(self, other):
        other = ensure_node(other)
        out = Node(self.value * other.value, [self, other], op="mul")

        def _backward():
            self.grad = self.grad + (other.value * out.grad)
            other.grad = other.grad + (self.value * out.grad)

        out._backward = _backward
        return out

    def __rmul__(self, other):
        return ensure_node(other) * self

    def __truediv__(self, other):
        other = ensure_node(other)
        out = Node(self.value / other.value, [self, other], op="div")

        def _backward():
            self.grad = self.grad + (out.grad / other.value)
            other.grad = other.grad - (
                (self.value * out.grad) / (other.value * other.value)
            )

        out._backward = _backward
        return out

    def __rtruediv__(self, other):
        return ensure_node(other) / self

    def __neg__(self):
        out = Node(-self.value, [self], op="neg")

        def _backward():
            self.grad = self.grad - out.grad

        out._backward = _backward
        return out

    def __pow__(self, n):
        if not isinstance(n, int):
            raise TypeError("Only integer powers supported")
        if n < 0:
            raise ValueError("Negative powers not supported in autodiff")
        if n == 0:
            return Node(VDR(1))
        out_val = VDR(1)
        for _ in range(n):
            out_val = out_val * self.value
        out = Node(out_val, [self], op="pow%d" % n)

        def _backward():
            if n == 0:
                return
            coeff = VDR(n)
            if n == 1:
                deriv = coeff
            else:
                deriv = coeff
                for _ in range(n - 1):
                    deriv = deriv * self.value
            self.grad = self.grad + (deriv * out.grad)

        out._backward = _backward
        return out

    def backward(self):
        topo = []
        visited = set()
        _build_topo(self, visited, topo)
        self.grad = VDR(1)
        for node in reversed(topo):
            node._backward()

    def __repr__(self):
        if self.name:
            return "Node(name=%r, value=%r, grad=%r)" % (
                self.name,
                self.value,
                self.grad,
            )
        return "Node(value=%r, grad=%r, op=%r)" % (
            self.value,
            self.grad,
            self.op,
        )


def _build_topo(node: Node, visited: Set[int], topo: List[Node]):
    node_id = id(node)
    if node_id in visited:
        return
    visited.add(node_id)
    for p in node.parents:
        _build_topo(p, visited, topo)
    topo.append(node)


def ensure_node(x) -> Node:
    if isinstance(x, Node):
        return x
    return Node(x)


def relu(x) -> Node:
    x = ensure_node(x)
    out_val = x.value if x.value > VDR(0) else VDR(0)
    out = Node(out_val, [x], op="relu")

    def _backward():
        if x.value > VDR(0):
            x.grad = x.grad + out.grad

    out._backward = _backward
    return out


def sum_nodes(xs: Sequence[Node]) -> Node:
    if len(xs) == 0:
        return Node(VDR(0))
    total = ensure_node(xs[0])
    for i in range(1, len(xs)):
        total = total + xs[i]
    return total


def mean_nodes(xs: Sequence[Node]) -> Node:
    if len(xs) == 0:
        raise ValueError("mean_nodes requires nonempty list")
    return sum_nodes(xs) / Node(VDR(len(xs)))


def mse_loss(pred: Sequence[Node], target: Sequence[ScalarLike]) -> Node:
    if len(pred) != len(target):
        raise ValueError("pred and target lengths must match")
    terms = []
    for i in range(len(pred)):
        d = ensure_node(pred[i]) - ensure_node(target[i])
        terms.append(d * d)
    return mean_nodes(terms)


def dot_nodes(a: Sequence[Node], b: Sequence[Node]) -> Node:
    if len(a) != len(b):
        raise ValueError("dot requires same lengths")
    terms = []
    for i in range(len(a)):
        terms.append(ensure_node(a[i]) * ensure_node(b[i]))
    return sum_nodes(terms)


def linear_node(weights: Sequence[ScalarLike], xs: Sequence[Node], bias: ScalarLike) -> Node:
    if len(weights) != len(xs):
        raise ValueError("weights and xs lengths must match")
    terms = []
    for i in range(len(xs)):
        terms.append(ensure_node(weights[i]) * ensure_node(xs[i]))
    return sum_nodes(terms) + ensure_node(bias)


def zero_grads(nodes: Sequence[Node]):
    for n in nodes:
        n.zero_grad()


def value_of_vec(nodes: Sequence[Node]) -> Vec:
    return Vec([ensure_node(n).value for n in nodes])


def grad_of_vec(nodes: Sequence[Node]) -> Vec:
    return Vec([ensure_node(n).grad for n in nodes])
