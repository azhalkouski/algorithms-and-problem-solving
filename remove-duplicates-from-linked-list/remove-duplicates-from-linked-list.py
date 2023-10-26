# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None and currentNode.next is not None:
        if currentNode.value != currentNode.next.value:
            currentNode = currentNode.next
            continue
        currentNode.next = currentNode.next.next
    return linkedList
