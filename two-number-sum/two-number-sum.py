# O(n^2) time | O(1) space
def twoNumberSum_v1(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []


# O(n) time | O(n) space
def twoNumberSum_v2(array, targetSum):
    nums = {} # create a hash-table

    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []


# O(nlog(n)) time | O(1) space
# So, if you value space more than time, you would
# probably choose this solution. Otherwise, you would choose the option with
# a hash-table
def twoNumberSum_v3(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1

    while left != right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []


def twoNumberSum_v4(array, targetSum):
    unique_set = set(array)

    for num in array:
        target = targetSum - num
        if target in unique_set and target is not num:
            return [num, target]
        
    return []
    