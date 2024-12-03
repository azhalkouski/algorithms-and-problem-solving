# O(log(n)) time | O(1) space
def binarySearch(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (right + left) // 2
        if array[middle] == target:
            return middle
        elif array[middle] > target:
            right = middle - 1
        elif array[middle] < target:
            left = middle + 1
    return -1



print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33) == 3)
print(binarySearch([1, 5, 23, 111], 5) == 1)
print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 355) == 10)
print(binarySearch([1, 5, 23, 111], 120) == -1)