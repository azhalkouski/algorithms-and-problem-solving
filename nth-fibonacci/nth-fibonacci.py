# O(n) time | O(n) space
def getNthFib(n):
    fibSequence = [0, 1]
    while len(fibSequence) < n:
        fibSequence.append((fibSequence[len(fibSequence) - 1] + fibSequence[len(fibSequence) - 2]))  
    return fibSequence[n-1]


# O(2^n) time | O(n) space
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return getNthFib(n - 1) + getNthFib(n - 2)



# we can use memoization with a hashtable but to optimize the recursive solution
# although it well give us O(n) time | O(n) space it is still not the most optimal
# solution, because the best way to do it is to go iterative with space time complexity
# of O(n) time | O(1) space
# O(n) time | O(n) space
def getNthFib(n,  memoize = {1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize)
        return memoize[n]


# THE BEST APPROACH
# O(n) time | O(1) space
def getNthFib(n):
    prev = 0
    last = 1
    nextElIdx = 3
    while nextElIdx <= n:
        nextEl = prev + last
        prev = last
        last = nextEl
        nextElIdx += 1
    return 0 if n == 1 else last
