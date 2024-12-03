# O(n) time | O(n) space
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode_v1(linkedList):
    currentNode = linkedList
    allNodesMap = {} # O(n) space
    count = 0
    
    while currentNode is not None: # O(n) time
        count += 1
        allNodesMap[count] = currentNode
        currentNode = currentNode.next
    
    middleNodeIdx = count // 2 + 1 # O(1)
    return allNodesMap[middleNodeIdx] # O(1)



# O(n) time | O(1) space
def middleNode_v2(linkedList):
    slowNode = linkedList
    fastNode = linkedList

    while fastNode is not None and fastNode.next is not None:
        slowNode = slowNode.next
        fastNode = fastNode.next.next

    return slowNode


# Example input linked lists
# 1 -> 2 -> 3 -> 4 -> 5 -> 6
# 1 -> 2 -> 3 -> 4 -> 5

linkedList = LinkedList(0)
linkedList.next = LinkedList(1)
expected = LinkedList(2)
linkedList.next.next = expected
expected.next = LinkedList(3)

print(middleNode_v1(linkedList) == expected)
print(middleNode_v2(linkedList) == expected)