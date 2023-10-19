# refactoring of solution 1
def findClosestValueInBst(tree, target):
    if tree == None:
        return None
        
    return checkNode(tree, target, tree.value)


def checkNode(node, target, prevClosestVal):
    if target == node.value:
        return node.value

    nextNode = node.right if target > node.value else node.left
    
    if nextNode == None:
        return prevClosestVal

    prevClosestVal = nextNode.value if abs(target - nextNode.value) < abs(target - prevClosestVal) else prevClosestVal
    return checkNode(nextNode, target, prevClosestVal)


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None




# TESTING
# case 1
root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)
expected = 13
actual = findClosestValueInBst(root, 12)
print(expected == actual)


 # case 2
root2 = BST(10)
root2.left = BST(5)
root2.left.left = BST(-51)
root2.left.left.left = BST(-403)
root2.left.right = BST(5)
root2.right = BST(15)
root2.right.left = BST(13)
root2.right.left.right = BST(14)
root2.right.right = BST(22)
expected2 = -51
actual2 = findClosestValueInBst(root2, -70)
print(expected2 == actual2)