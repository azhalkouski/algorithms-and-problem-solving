# O(n*m) time | O(n) space, where n is the length of the document and m is the lendth of charactes
def generateDocument_v1(characters, document):
    for letter in document:
        idxInCharacters = characters.find(letter)
        if idxInCharacters == -1:
            return False
        else:
            characters = characters[:idxInCharacters] + characters[idxInCharacters + 1:]
    return True


# OPTIMAL SOLUTION from space time complexity perspective
# O(n + m) time | O(c) space, where
# 'n' is the number of items in characters,
# 'c' is the number of unique characters in characters,
# 'm' is the number of characters in the document
def generateDocument_v2(characters, document):
    charactersDict = {}

    # O(n) time | O(c) space, where n is the number of items in characters,
    # and c is the number of unique characters in characters
    for char in characters:
        if char in charactersDict.keys():
            charactersDict[char] += 1
        else:
            charactersDict[char] = 1

    # O(m) time | O(1) space, where m is the number of characters in the document
    for char in document:
        if char in charactersDict.keys() and charactersDict[char] > 0:
            charactersDict[char] -= 1
        else:
            return False
            
    return True


# CONSTANT SPACE solution as a trade off for hashmap solution in case we
# can't afford that extra space consumption
# O(m * (n + m)) time | O(1) space, where 'm' is the number of characters in the document,
# and 'n' is the number of characters in the 'characters'
def generateDocument_v3(characters, document):
    for char in document:
        frequencyInDocument = countCharFrequency(char, document)
        frequencyInCharacters = countCharFrequency(char, characters)

        if frequencyInDocument > frequencyInCharacters:
            return False
    return True


def countCharFrequency(character, target):
    count = 0
    for char in target:
        if character == char:
            count += 1
    return count


print(generateDocument_v1("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!") == True)
print(generateDocument_v1("aheaollabbhb", "hello") == True)
print(generateDocument_v1("estssa", "testing") ==  False)
print(generateDocument_v1("helloworldO", "hello wOrld") ==  False)
print(generateDocument_v1("&*&you^a%^&8766 _=-09     docanCMakemthisdocument", "Can you make this document &") ==  True)

print(generateDocument_v2("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!") == True)
print(generateDocument_v2("aheaollabbhb", "hello") == True)
print(generateDocument_v2("estssa", "testing") ==  False)
print(generateDocument_v2("helloworldO", "hello wOrld") ==  False)
print(generateDocument_v2("&*&you^a%^&8766 _=-09     docanCMakemthisdocument", "Can you make this document &") ==  True)

print(generateDocument_v3("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!") == True)
print(generateDocument_v3("aheaollabbhb", "hello") == True)
print(generateDocument_v3("estssa", "testing") ==  False)
print(generateDocument_v3("helloworldO", "hello wOrld") ==  False)
print(generateDocument_v3("&*&you^a%^&8766 _=-09     docanCMakemthisdocument", "Can you make this document &") ==  True)