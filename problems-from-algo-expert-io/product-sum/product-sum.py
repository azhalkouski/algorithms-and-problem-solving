# O(n) time | O(d) space - d is the greatest depth, n is number of all elements (including subarrays)
# so if input is [5, 2, [7, -1], 3, [6, [-13, 8], 4]], then n is equal to 12, and not 9
def productSum(array, depth = 1):
    sum = 0
    for item in array:
        if type(item) is int:
            sum += depth * item
        else:
            sum += depth * productSum(item, depth + 1)
    return sum


print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]) == 12)
