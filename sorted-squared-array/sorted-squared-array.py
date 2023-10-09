# brute force solution
# not the best solution becaues of O(n*log(n)) time complexity - logarithm
# because of the `sorted()` implementation
def sortedSquaredArray_v1(array):
    if array[0] < 0:
        return sorted([item**2 for item in array])
    return [item**2 for item in array]


# optimal solution
# O(n) time | O(n) space
def sortedSquaredArray_v2(array):
    squared = []
    leftP = 0
    rightP = len(array) -1
    offsetRight = -1
    while leftP <= rightP:
        if abs(array[leftP]) > abs(array[rightP]):
            squared.insert(offsetRight, array[leftP] ** 2)
            leftP += 1
        else:
            squared.insert(offsetRight, array[rightP] ** 2)
            rightP -= 1
        offsetRight -= 1
    return squared


print(sortedSquaredArray_v2([-10, -5, 0, 5, 10]) == [0, 25, 25, 100, 100])

print(sortedSquaredArray_v2([1, 2, 3, 5, 6, 8, 9]) == [1, 4, 9, 25, 36, 64, 81])