# O(n) time | O(n) space, where n is the length of the input string
def caesarCipherEncryptor(string, key):
    newStrList = []
    
    for letter in string:
        newStrList.append(nextInAlphabetByKeySteps(letter, key))
    
    return ''.join(newStrList)


def nextInAlphabetByKeySteps(letter, keySteps):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')

    # this .index() call could have been O(N) but since the alphabet is 26 characters every time
    # we consider this operation to be constant time
    # if we had to traverse N number of characters then it would be O(N) and thus the overall
    # space time complexity would be O(N * N) which is O(N^2)
    nextIdx = alphabet.index(letter) + keySteps
    if nextIdx < len(alphabet):
        return alphabet[nextIdx]
    else:
        idxFromZero = nextIdx % len(alphabet)
        return alphabet[idxFromZero]


print(caesarCipherEncryptor("xyz", 2) ==  "zab")
print(caesarCipherEncryptor("abc", 26) ==  "abc")
print(caesarCipherEncryptor("abc", 57) ==  "fgh")
