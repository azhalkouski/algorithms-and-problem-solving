# O(NlogN) time | O(N) space
def nonConstructibleChange(coins):
    sortedCoins = sorted(coins) # O(NlogN) time | O(N) space
    change = 0
    for nextCoin in sortedCoins: # O(N) time | O(1) space
        if change + 1 >= nextCoin:
            change += nextCoin
        else:
            return change + 1
    return change + 1


coins1 = [5, 7, 1, 1, 2, 3, 22]
print(nonConstructibleChange(coins1) ==  20)
coins2 = [1, 1, 1, 1, 1]
print(nonConstructibleChange(coins2) ==  6)
coins3 = []
print(nonConstructibleChange(coins3) ==  1)