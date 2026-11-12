"""
Assessment 3.3: Non-Linear Data Structure
Diagram 2: Graph built from the last name  ALCOMENDRAS
Each letter is a vertex; consecutive letters are connected by an edge.
The last name has two A's, so both map to the same vertex A, which
closes a cycle (A-L-C-O-M-E-N-D-R-A) and adds a branch A-S.
Traversals: BFS and DFS starting at vertex A (neighbors visited alphabetically).
"""
from collections import deque

LAST_NAME = "ALCOMENDRAS"


def build_graph(name):
    graph = {}
    for ch in name:
        graph.setdefault(ch, set())
    for a, b in zip(name, name[1:]):
        if a != b:
            graph[a].add(b)
            graph[b].add(a)
    return {v: sorted(n) for v, n in graph.items()}


def bfs(graph, start):
    """Breadth-First Search: visit neighbors level by level using a queue."""
    visited, order, queue = {start}, [], deque([start])
    while queue:
        v = queue.popleft()
        order.append(v)
        for n in graph[v]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
    return order


def dfs(graph, start):
    """Depth-First Search: go as deep as possible, then backtrack (recursion)."""
    visited, order = set(), []

    def visit(v):
        visited.add(v)
        order.append(v)
        for n in graph[v]:
            if n not in visited:
                visit(n)

    visit(start)
    return order


if __name__ == "__main__":
    g = build_graph(LAST_NAME)
    print("Last name :", LAST_NAME)
    print("Adjacency :")
    for v, ns in g.items():
        print(f"  {v}: {', '.join(ns)}")
    print("BFS       :", " - ".join(bfs(g, "A")))
    print("DFS       :", " - ".join(dfs(g, "A")))