# code/vdr/checkpoint.py
from __future__ import annotations

from typing import Any, Dict, List

from .linalg import vdr_to_dict, vdr_from_dict, Vec, Mat
from .nn import ParameterVec, ParameterMat


def save_parameters(params):
    out = []
    for p in params:
        if isinstance(p, ParameterVec):
            out.append(
                {
                    "type": "vec",
                    "name": p.name,
                    "value": [vdr_to_dict(x) for x in p.value._data],
                    "grad": [vdr_to_dict(x) for x in p.grad._data],
                }
            )
        elif isinstance(p, ParameterMat):
            rows_val = []
            rows_grad = []
            for i in range(p.value.nrows):
                rows_val.append([vdr_to_dict(p.value[i, j]) for j in range(p.value.ncols)])
                rows_grad.append([vdr_to_dict(p.grad[i, j]) for j in range(p.grad.ncols)])
            out.append(
                {
                    "type": "mat",
                    "name": p.name,
                    "value": rows_val,
                    "grad": rows_grad,
                }
            )
        else:
            raise TypeError("Unsupported parameter type: %s" % type(p).__name__)
    return out


def load_parameters(saved):
    out = []
    for item in saved:
        if item["type"] == "vec":
            value = Vec([vdr_from_dict(d) for d in item["value"]])
            grad = Vec([vdr_from_dict(d) for d in item["grad"]])
            p = ParameterVec(value, name=item.get("name"))
            p.grad = grad
            out.append(p)
        elif item["type"] == "mat":
            value_rows = []
            grad_rows = []
            for row in item["value"]:
                value_rows.append([vdr_from_dict(d) for d in row])
            for row in item["grad"]:
                grad_rows.append([vdr_from_dict(d) for d in row])
            p = ParameterMat(Mat(value_rows), name=item.get("name"))
            p.grad = Mat(grad_rows)
            out.append(p)
        else:
            raise ValueError("Unknown checkpoint parameter type: %r" % item["type"])
    return out


def save_model(model):
    return save_parameters(model.parameters())
