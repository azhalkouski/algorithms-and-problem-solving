# This is the class of the input root. Do not edit it.
# O(n) time | O(N) space because we're storing a list of sums which is ~half the nodes and N/2 is N from complexity analysis perspective
# as for the recursive execution call stack, its space complexity is O(h),
# where h is the depth of the tree, HOWEVER O(N) is greater that O(h) so
# O(N) has higher priority from complexity analysis persective, and we say
# that the overall complexity is O(N) time | O(N) space
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    branchSums = []
    calculateSums(root, branchSums, 0)
    return branchSums


def calculateSums(node, branchSums, workingSum):
    if node is None:
        return

    newWorkingSum = workingSum + node.value
    
    if node.left is None and node.right is None:
        branchSums.append(newWorkingSum)
        return

    calculateSums(node.left, branchSums, newWorkingSum)
    calculateSums(node.right, branchSums, newWorkingSum)
