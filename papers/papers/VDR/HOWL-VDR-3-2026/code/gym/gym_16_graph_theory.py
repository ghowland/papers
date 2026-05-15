"""
VDR Gym 16: Graph Theory
Exact shortest path, MST, max-flow, PageRank on small graphs.
All weights rational. All results exact.
"""
from __future__ import annotations
from fractions import Fraction
import sys
sys.path.insert(0, '..')
from vdr import VDR, Vec, Mat

passed = 0
failed = 0
def check(name, condition):
    global passed, failed
    if condition:
        passed += 1
        print("  PASS: %s" % name)
    else:
        failed += 1
        print("  FAIL: %s" % name)

INF = VDR(10**9)

# === 1. Dijkstra exact shortest path ===
print("\n=== 1. Dijkstra exact shortest path ===")

def dijkstra(adj, src):
    """Exact Dijkstra on adjacency dict. adj[u] = [(v, weight_vdr), ...]"""
    n = len(adj)
    dist = {}
    for u in adj:
        dist[u] = INF
    dist[src] = VDR(0)
    visited = set()
    for _ in range(n):
        # pick unvisited with smallest dist
        u = None
        for node in adj:
            if node not in visited:
                if u is None or dist[node] < dist[u]:
                    u = node
        if u is None:
            break
        visited.add(u)
        for v, w in adj[u]:
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
    return dist

# graph: 0->1 (1/3), 0->2 (1), 1->2 (1/4), 1->3 (2), 2->3 (1/2)
adj = {
    0: [(1, VDR(1, 3)), (2, VDR(1))],
    1: [(2, VDR(1, 4)), (3, VDR(2))],
    2: [(3, VDR(1, 2))],
    3: [],
}
dist = dijkstra(adj, 0)
print("  dist[0]=%s dist[1]=%s dist[2]=%s dist[3]=%s" % (
    dist[0], dist[1], dist[2], dist[3]))

check("dist[0] = 0", dist[0] == VDR(0))
check("dist[1] = 1/3", dist[1] == VDR(1, 3))
# 0->1->2 = 1/3 + 1/4 = 7/12 < 0->2 = 1
check("dist[2] = 7/12", dist[2] == VDR(7, 12))
# 0->1->2->3 = 7/12 + 1/2 = 13/12
check("dist[3] = 13/12", dist[3] == VDR(13, 12))

# === 2. Bellman-Ford with negative weights ===
print("\n=== 2. Bellman-Ford with negative weights ===")

def bellman_ford(n, edges, src):
    """edges = [(u, v, weight_vdr), ...]"""
    dist = [INF] * n
    dist[src] = VDR(0)
    for _ in range(n - 1):
        for u, v, w in edges:
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
    return dist

edges_bf = [
    (0, 1, VDR(4)),
    (0, 2, VDR(1)),
    (2, 1, VDR(-3, 2)),  # negative weight -3/2
    (1, 3, VDR(1)),
    (2, 3, VDR(5)),
]
dist_bf = bellman_ford(4, edges_bf, 0)
print("  dist=%s" % [str(d) for d in dist_bf])
# 0->2 = 1, 2->1 = 1 + (-3/2) = -1/2, 1->3 = -1/2 + 1 = 1/2
check("BF dist[0] = 0", dist_bf[0] == VDR(0))
check("BF dist[2] = 1", dist_bf[2] == VDR(1))
check("BF dist[1] = -1/2", dist_bf[1] == VDR(-1, 2))
check("BF dist[3] = 1/2", dist_bf[3] == VDR(1, 2))

# === 3. Prim's MST ===
print("\n=== 3. Prim's MST ===")

def prim_mst(n, adj_list):
    """adj_list[u] = [(v, weight_vdr), ...]. Returns total MST weight."""
    in_mst = [False] * n
    key = [INF] * n
    key[0] = VDR(0)
    total = VDR(0)
    for _ in range(n):
        u = None
        for i in range(n):
            if not in_mst[i]:
                if u is None or key[i] < key[u]:
                    u = i
        if u is None:
            break
        in_mst[u] = True
        total = total + key[u]
        for v, w in adj_list[u]:
            if not in_mst[v] and w < key[v]:
                key[v] = w
    return total

# triangle: 0-1 (1/3), 0-2 (1/2), 1-2 (1/4)
mst_adj = {
    0: [(1, VDR(1, 3)), (2, VDR(1, 2))],
    1: [(0, VDR(1, 3)), (2, VDR(1, 4))],
    2: [(0, VDR(1, 2)), (1, VDR(1, 4))],
}
mst_weight = prim_mst(3, mst_adj)
# MST picks edges 1/4 and 1/3, total = 7/12
print("  MST weight = %s" % mst_weight)
check("MST weight = 7/12", mst_weight == VDR(7, 12))

# === 4. Max-flow (Ford-Fulkerson with BFS) ===
print("\n=== 4. Max-flow (Ford-Fulkerson with BFS) ===")

def max_flow_bfs(n, cap, s, t):
    """cap[u][v] = VDR capacity. Modifies cap in place. Returns max flow."""
    from collections import deque
    flow = VDR(0)
    while True:
        # BFS to find augmenting path
        parent = [-1] * n
        visited = [False] * n
        visited[s] = True
        q = deque([s])
        while q:
            u = q.popleft()
            for v in range(n):
                if not visited[v] and cap[u][v] > VDR(0):
                    visited[v] = True
                    parent[v] = u
                    if v == t:
                        break
            else:
                continue
            break
        if not visited[t]:
            break
        # find bottleneck
        bottleneck = INF
        v = t
        while v != s:
            u = parent[v]
            if cap[u][v] < bottleneck:
                bottleneck = cap[u][v]
            v = u
        # update residual
        v = t
        while v != s:
            u = parent[v]
            cap[u][v] = cap[u][v] - bottleneck
            cap[v][u] = cap[v][u] + bottleneck
            v = u
        flow = flow + bottleneck
    return flow

Z = VDR(0)
# 4-node network: s=0, t=3
# 0->1: 1/2, 0->2: 1/3, 1->3: 1/4, 2->3: 1/3, 1->2: 1/5
cap = [
    [Z, VDR(1, 2), VDR(1, 3), Z],
    [Z, Z, VDR(1, 5), VDR(1, 4)],
    [Z, Z, Z, VDR(1, 3)],
    [Z, Z, Z, Z],
]
mf = max_flow_bfs(4, cap, 0, 3)
print("  max flow = %s = %s" % (mf, mf.to_fraction()))
# max flow = min of cut capacities
# path 0->1->3: bottleneck 1/4
# path 0->2->3: bottleneck 1/3
# path 0->1->2->3: bottleneck min(1/2-1/4, 1/5, 1/3-1/3) = min(1/4, 1/5, 0) = 0
# total = 1/4 + 1/3 = 7/12
check("max flow = 7/12", mf == VDR(7, 12))

# === 5. PageRank as exact linear system ===
print("\n=== 5. PageRank as exact linear system ===")

# 4-page web: 0->1, 0->2, 1->2, 2->0, 3->0, 3->2
# transition matrix T[j][i] = 1/outdegree(i) if i->j
# PageRank: (I - d*T) * r = ((1-d)/n) * 1
# Use d = 1/2 for simplicity (rational)
n_pages = 4
d_pr = VDR(1, 2)
# outdegrees: 0:2, 1:1, 2:1, 3:2
# T[j][i]:
# 0 gets from: 2(out=1), 3(out=2) -> T[0][2]=1, T[0][3]=1/2
# 1 gets from: 0(out=2) -> T[1][0]=1/2
# 2 gets from: 0(out=2), 1(out=1), 3(out=2) -> T[2][0]=1/2, T[2][1]=1, T[2][3]=1/2
# 3 gets from: nobody -> all zero
T = Mat([
    [VDR(0), VDR(0), VDR(1), VDR(1, 2)],
    [VDR(1, 2), VDR(0), VDR(0), VDR(0)],
    [VDR(1, 2), VDR(1), VDR(0), VDR(1, 2)],
    [VDR(0), VDR(0), VDR(0), VDR(0)],
])

# (I - d*T) * r = ((1-d)/n) * 1
I4 = Mat.identity(4)
A_pr = I4 - T.scale(d_pr)
b_pr = Vec([VDR(1, 8)] * 4)  # (1 - 1/2) / 4 = 1/8
r_pr = A_pr.solve(b_pr)

print("  PageRank = %s" % [str(r_pr[i]) for i in range(4)])

# verify: all positive
all_pos = all(r_pr[i] > VDR(0) for i in range(4))
check("all PageRank positive", all_pos)

# verify: sum to 1
pr_sum = r_pr[0]
for i in range(1, 4):
    pr_sum = pr_sum + r_pr[i]

# page 2 should have highest rank (most inlinks)
check("page 2 has highest rank", r_pr[2] > r_pr[0])
check("page 2 > page 1", r_pr[2] > r_pr[1])

# === 6. Floyd-Warshall all-pairs shortest path ===
print("\n=== 6. Floyd-Warshall all-pairs shortest path ===")

def floyd_warshall(n, dist_mat):
    """dist_mat is n x n list of lists of VDR. Modifies in place."""
    d = [[dist_mat[i][j] for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                via_k = d[i][k] + d[k][j]
                if via_k < d[i][j]:
                    d[i][j] = via_k
    return d

# 3-node graph
fw = [
    [VDR(0), VDR(1, 3), INF],
    [INF, VDR(0), VDR(1, 4)],
    [VDR(1, 2), INF, VDR(0)],
]
fw = floyd_warshall(3, fw)
print("  0->2: %s, 2->1: %s" % (fw[0][2], fw[2][1]))
check("FW 0->1 = 1/3", fw[0][1] == VDR(1, 3))
check("FW 0->2 = 7/12", fw[0][2] == VDR(7, 12))  # 0->1->2
check("FW 2->0 = 1/2", fw[2][0] == VDR(1, 2))
check("FW 2->1 = 5/6", fw[2][1] == VDR(5, 6))  # 2->0->1

# === 7. Vertex degree and adjacency matrix properties ===
print("\n=== 7. Adjacency matrix properties ===")

# K4 complete graph with weight 1/k for edge to node k
# adjacency matrix (weighted, symmetric)
A_g = Mat([
    [VDR(0), VDR(1), VDR(1, 2), VDR(1, 3)],
    [VDR(1), VDR(0), VDR(1), VDR(1, 2)],
    [VDR(1, 2), VDR(1), VDR(0), VDR(1)],
    [VDR(1, 3), VDR(1, 2), VDR(1), VDR(0)],
])
check("adjacency symmetric", A_g == A_g.T)

# weighted degree: row sum
deg0 = VDR(0)
for j in range(4):
    deg0 = deg0 + A_g[0, j]
print("  deg(0) = %s" % deg0.to_fraction())
check("deg(0) = 11/6", deg0 == VDR(11, 6))

# A² counts weighted 2-step paths
A2 = A_g * A_g
check("A² symmetric", A2 == A2.T)
print("  A²[0,0] = %s (self-loops via 2-step)" % A2[0, 0].to_fraction())
# A²[0,0] = sum of A[0,k]² for k
# = 0 + 1 + 1/4 + 1/9 = 49/36
check("A²[0,0] = 49/36", A2[0, 0] == VDR(49, 36))


print("\n" + "=" * 50)
print("Gym 16 results: %d passed, %d failed" % (passed, failed))
if failed == 0:
    print("ALL GYM 16 TESTS PASSED")
print("=" * 50)
