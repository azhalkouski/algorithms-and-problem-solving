# O(NLog(N)) time | O(1) space
def minimumWaitingTime(queries):
    queries.sort()

    totalWaitingTime = 0
    for idx, duration in enumerate(queries):
        queriesLeft = len(queries) - (idx + 1)
        totalWaitingTime += duration * queriesLeft

    return totalWaitingTime


print(minimumWaitingTime([3, 2, 1, 2, 6]) == 17)
print(minimumWaitingTime([1, 2, 4, 5, 2, 1]) == 23)
print(minimumWaitingTime([1, 9]) == 1)