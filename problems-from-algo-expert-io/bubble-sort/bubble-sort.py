# O(n^2) time Average and Worst | O(1) space
def bubbleSort(array):
    isSorted = False
    # we can eliminate one number on the righthand at the end of each iteration
    # bacause with each iteration the n-th largest number will be moved to the end
    # of the list and thus we don't need to swap it ever again
    # this the 'iterationsCount' is introduced
    iterationsCount = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - iterationsCount):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSorted = False
        iterationsCount += 1
    return array

print(bubbleSort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9])
print(bubbleSort([1, 2, 3]) == [1, 2, 3])
print(bubbleSort([427, 787, 222, 996, -359, -614, 246, 230, 107, -706, 568, 9, -246, 12, -764, -212, -484, 603, 934, -848, -646, -991, 661, -32, -348, -474, -439, -56, 507, 736, 635, -171, -215, 564, -710, 710, 565, 892, 970, -755, 55, 821, -3, -153, 240, -160, -610, -583, -27, 131]) == [-991, -848, -764, -755, -710, -706, -646, -614, -610, -583, -484, -474, -439, -359, -348, -246, -215, -212, -171, -160, -153, -56, -32, -27, -3, 9, 12, 55, 107, 131, 222, 230, 240, 246, 427, 507, 564, 565, 568, 603, 635, 661, 710, 736, 787, 821, 892, 934, 970, 996])