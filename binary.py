"""
Assessment 3.3: Non-Linear Data Structure
Diagram 1: Binary Tree built from the last name  ALCOMENDRAS
Traversals: BFS (level-order) and DFS (pre-order)
"""
from collections import deque

LAST_NAME = "ALCOMENDRAS"


class Node:
    def __init__(self, value, index):
        self.value = value      # letter
        self.index = index      # position in the name (letters repeat, e.g. A)
        self.left = None
        self.right = None


def build_tree(name):
    """Insert letters level by level (left to right) -> complete binary tree."""
    if not name:
        return None
    nodes = [Node(ch, i) for i, ch in enumerate(name)]
    for i, node in enumerate(nodes):
        left, right = 2 * i + 1, 2 * i + 2
        if left < len(nodes):
            node.left = nodes[left]
        if right < len(nodes):
            node.right = nodes[right]
    return nodes[0]


def bfs(root):
    """Breadth-First Search: visit level by level using a queue."""
    order, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        order.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def dfs(root):
    """Depth-First Search (pre-order): Root -> Left -> Right using a stack."""
    order, stack = [], [root]
    while stack:
        node = stack.pop()
        order.append(node.value)
        if node.right:           # push right first so left is processed first
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order


if __name__ == "__main__":
    root = build_tree(LAST_NAME)
    print("Last name :", LAST_NAME)
    print("BFS       :", " - ".join(bfs(root)))
    print("DFS       :", " - ".join(dfs(root)))