# improved recursive solution
# O(N) time | O(h) space, where "h" is the height of the tree
def nodeDepths_v1(root, depth = 0):
    if root is None:
        return 0

    depth = depth + nodeDepths_v1(root.left, depth + 1) + nodeDepths_v1(root.right, depth + 1)
    return depth


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# iterative solution with a stack
# O(N) time | O(h) space because stack will max contain height numbers of elements
def nodeDepths_v2(root):
    sumOfDepths = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    return sumOfDepths


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.left = BinaryTree(4)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)
root.left.right = BinaryTree(5)
root.right = BinaryTree(3)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
actual_v1 = nodeDepths_v1(root)
actual_v2 = nodeDepths_v2(root)
print(actual_v1 == 16)
print(actual_v2 == 16)