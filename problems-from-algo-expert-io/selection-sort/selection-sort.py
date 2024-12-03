# O(n^2) time | O(1) space
def selectionSort(array):
    for i in range(len(array)):
        idxOfSmallest = findSmallestInRange(i, len(array), array)
        swap(i, idxOfSmallest, array)
    return array


'''returns index in array'''
def findSmallestInRange(start, stop, array):
    idxOfSmallest = start
    for i in range(start, stop):
        if array[i] < array[idxOfSmallest]:
            idxOfSmallest = i
    return idxOfSmallest


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


print(selectionSort([1]) == [1])
print(selectionSort([1, 3, 2]) == [1, 2, 3])
print(selectionSort([4, 1, 5, 0, -9, -3, -3, 9, 3, -4, -9, 8, 1, -3, -7, -4, -9, -1, -7, -2, -7, 4]) == [-9, -9, -9, -7, -7, -7, -4, -4, -3, -3, -3, -2, -1, 0, 1, 1, 3, 4, 4, 5, 8, 9])
