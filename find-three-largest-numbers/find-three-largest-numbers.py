# O(n) time | O(1) space, where 'n' is a number of elements in array 
def findThreeLargestNumbers(array):
    output = [None, None, None]

    for item in array:
        potentialIndex = 2

        while potentialIndex >= 0:
            if output[potentialIndex] is None or item > output[potentialIndex]:
                for i in range(potentialIndex):
                    output[i] = output[i + 1]

                output[potentialIndex] = item
                break
            else:
                potentialIndex -= 1

    return output


print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]) == [18, 141, 541])
print(findThreeLargestNumbers([7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7]) == [7, 7, 8])
print(findThreeLargestNumbers([-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]) == [-2, -1, 7])
