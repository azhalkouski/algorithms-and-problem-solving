# O(n) time | O(n) space, where n is the length of the input string
def runLengthEncoding(string):
    count = 1
    runLength = []

    for i in range(1, len(string)):
        currentChar = string[i]
        prevChar = string[i - 1]

        if currentChar != prevChar or count == 9:
            runLength.append(str(count) + prevChar)
            count = 0
        
        count += 1
    runLength.append(str(count) + string[-1])
    return ''.join(runLength)
