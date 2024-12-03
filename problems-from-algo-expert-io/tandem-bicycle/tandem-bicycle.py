# O(nLog(n)) time | O(N) space - where n is the number of tandem bicycles
def tandemBicycle_v1(redShirtSpeeds, blueShirtSpeeds, fastest):
    sum = 0
    
    if fastest == True:
        combined = redShirtSpeeds + blueShirtSpeeds # O(N+M) time | O(N+M) space; I think since N == M we can leave it as O(2N) and thus O(N)
        combined.sort() # O(nLog(n)) time | O(1) space
        [sum := sum + item for item in combined[-len(blueShirtSpeeds):]] # O(2N/2) thus O(N) time | O(1) space
    else:
        redShirtSpeeds.sort() # O(N)time | O(1) space
        blueShirtSpeeds.sort() # O(N)time | O(1) space
        for idx in range(len(redShirtSpeeds)): # O(N)
            fastestOne = redShirtSpeeds[idx] if redShirtSpeeds[idx] >= blueShirtSpeeds[idx] else blueShirtSpeeds[idx] # O(1)
            print(fastestOne)
            sum += fastestOne # O(1)
    
    return sum


# O(nLog(n)) time | O(1) space - where n is the number of tandem bicycles
def tandemBicycle_v2(redShirtSpeeds, blueShirtSpeeds, fastest):
    sum = 0
    numberOfBicycles = len(redShirtSpeeds)
    redShirtSpeeds.sort() # O(N)time | O(1) space
    blueShirtSpeeds.sort() # O(N)time | O(1) space
    
    if fastest == True:
        # combine the fastest A with the slowest B
        # combine the prev fastest A with the next slowest (a bit faster one) B
        # go on this way
        for i in range(numberOfBicycles):
            sum += max(blueShirtSpeeds[i], redShirtSpeeds[-(i+1)])
    else:
        # combine the slowest A with the slowest B
        # combine next A with the next B
        # go on this way
        for i in range(numberOfBicycles): # O(N)
            sum += max(redShirtSpeeds[i], blueShirtSpeeds[i]) # O(1)
    
    return sum



print(tandemBicycle_v2([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], True) == 32)
print(tandemBicycle_v2([1, 1, 1, 1, 2, 2, 2, 2, 9, 11], [1, 1, 1, 1, 3, 3, 3, 3, 5, 7], True) == 48)
print(tandemBicycle_v2([1, 1, 1, 1, 3, 3, 3, 3, 5, 7], [1, 1, 1, 1, 2, 2, 2, 2, 9, 11], False) == 36)