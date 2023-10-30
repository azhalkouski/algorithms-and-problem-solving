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


print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD") == "9A4A2B4C2D")
print(runLengthEncoding("aA") == "1a1A")
print(runLengthEncoding("1A2BB3CCC4DDDD") == "111A122B133C144D")
print(runLengthEncoding(" ") == "1 ")
print(runLengthEncoding(";;;;;;;;;;;;''''''''''''''''''''1233333332222211112222111s") == "9;3;9'9'2'111273524142311s")
