# O(nLog(N)) time | O(1) space
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if redShirtHeights[-1] == blueShirtHeights[-1]:
        return False

    redsAreInTheBackground = True if redShirtHeights[-1] > blueShirtHeights[-1] else False

    for i in range(len(redShirtHeights)):
        if redsAreInTheBackground is True:
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False
        else:
            if blueShirtHeights[i] <= redShirtHeights[i]:
                return False
    return True


print(classPhotos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5]) == True)
