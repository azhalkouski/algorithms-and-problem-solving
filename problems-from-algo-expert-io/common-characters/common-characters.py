# O(n*m) time | O(m) space - where 'n' is the number of items in the strings array, and 'm' is the length of the longest string
def commonCharacters_v1(strings):
    if len(strings) == 1:
        return strings

    # O(m) time | O(m) space - where 'm' is the length of the longest string
    # (in case of initialization with the longest string on this stepm, 
    # and if the string itself consists of anly unique characters
    commonIntersection = set(strings[0])
    # O(n*m) time | O(m) space - where 'n' is the number of items in the strings array, and 'm' is the length of the longest string
    for i in range(1, len(strings)):
        commonIntersection = set(commonIntersection.intersection(set(strings[i])))
        
    return list(commonIntersection)


# manual implementation without use of 'intersection()' method
# O(n*m) time | O(m) space - where 'n' is the number of items in the strings array, and 'm' is the length of the longest string
def commonCharacters_v2(strings):
    smallestString = getSmallestString(strings)
    potentialCommonCharacters = set(smallestString)

    for string in strings:
        removeNonexistingCharacters(string, potentialCommonCharacters)
    
    return list(potentialCommonCharacters)


def getSmallestString(strings):
    smallestString = strings[0]
    for string in strings:
        if len(string) < len(smallestString):
            smallestString = string
    return smallestString


def removeNonexistingCharacters(string, potentialCommonCharacters):
    uniqueStringCharacters = set(string)

    # convert to list because otherwise 'RuntimeError: Set changed size during iteration'
    for character in list(potentialCommonCharacters):
        if character not in uniqueStringCharacters:
            potentialCommonCharacters.remove(character)


print(commonCharacters_v1(["abc", "bcd", "cbad"]).sort() == ["b", "c"].sort())
print(commonCharacters_v1(["aaaa", "a"]).sort() == ["a"].sort())
print(commonCharacters_v1(["a"]).sort() == ["a"].sort())
print(commonCharacters_v1(["ab&cdef!", "f!ed&cba", "a&bce!d", "ae&fb!cd", "efa&!dbc", "eff!&fff&fffffffbcda", "eeee!efff&fffbbbbbaaaaaccccdddd", "*******!***&****abdcef************", "*******!***&****a***********f*", "*******!***&****b***********c*"]).sort() == ["!", "&"].sort())
print(commonCharacters_v2(["abc", "bcd", "cbad"]).sort() == ["b", "c"].sort())
print(commonCharacters_v2(["aaaa", "a"]).sort() == ["a"].sort())
print(commonCharacters_v2(["a"]).sort() == ["a"].sort())
print(commonCharacters_v2(["ab&cdef!", "f!ed&cba", "a&bce!d", "ae&fb!cd", "efa&!dbc", "eff!&fff&fffffffbcda", "eeee!efff&fffbbbbbaaaaaccccdddd", "*******!***&****abdcef************", "*******!***&****a***********f*", "*******!***&****b***********c*"]).sort() == ["!", "&"].sort())
