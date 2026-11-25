class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def preorder(node, result):
    """Root -> Left -> Right"""
    if node is None:
        return
    result.append(node.data)       # visit root
    preorder(node.left, result)    # traverse left
    preorder(node.right, result)   # traverse right


def inorder(node, result):
    """Left -> Root -> Right"""
    if node is None:
        return
    inorder(node.left, result)     # traverse left
    result.append(node.data)       # visit root
    inorder(node.right, result)    # traverse right


def postorder(node, result):
    """Left -> Right -> Root"""
    if node is None:
        return
    postorder(node.left, result)   # traverse left
    postorder(node.right, result)  # traverse right
    result.append(node.data)       # visit root

def build_tree():
    root = Node("J")

    # Left side
    root.left = Node("U")
    root.left.left = Node("T")
    root.left.left.left = Node("L")
    root.left.left.left.left = Node("A")
    root.left.left.left.right = Node("S")
    root.left.left.right = Node("C")

    root.left.right = Node("I")
    root.left.right.left = Node("O")
    root.left.right.right = Node("M")

    # Right side
    root.right = Node("S")
    root.right.left = Node("N")
    root.right.left.left = Node("E")
    root.right.left.right = Node("N")

    root.right.right = Node("A")
    root.right.right.left = Node("D")
    root.right.right.right = Node("R")

    return root


# ---------- Main ----------

def main():
    root = build_tree()

    pre, ino, post = [], [], []
    preorder(root, pre)
    inorder(root, ino)
    postorder(root, post)

    # First output: the name
    print("JUSTIN ALCOMENDRAS")

    input("Press Enter to continue...")

    print()
    print("DFS Methods in Tree")
    print("-" * 84)
    print("\n1. PreOrder  (Root -> Left -> Right):")
    print("   " + " -> ".join(pre))
    print("\n2. InOrder   (Left -> Root -> Right):")
    print("   " + " -> ".join(ino))
    print("\n3. PostOrder (Left -> Right -> Root):")
    print("   " + " -> ".join(post))
    print("-" * 84)

if __name__ == "__main__":
    main()
