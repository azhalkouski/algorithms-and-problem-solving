# O(n*m) time | O(m) space - where 'n' is the number of items in the strings array, and 'm' is the length of the longest string
def commonCharacters(strings):
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


print(commonCharacters(["abc", "bcd", "cbad"]).sort() == ["b", "c"].sort())
print(commonCharacters(["aaaa", "a"]).sort() == ["a"].sort())
print(commonCharacters(["a"]).sort() == ["a"].sort())
print(commonCharacters(["ab&cdef!", "f!ed&cba", "a&bce!d", "ae&fb!cd", "efa&!dbc", "eff!&fff&fffffffbcda", "eeee!efff&fffbbbbbaaaaaccccdddd", "*******!***&****abdcef************", "*******!***&****a***********f*", "*******!***&****b***********c*"]).sort() == ["!", "&"].sort())
