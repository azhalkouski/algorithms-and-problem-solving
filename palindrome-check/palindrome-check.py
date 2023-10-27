# O(n^2) time | O(n) space, n^2 because of creation a new string on every
# iteration
def isPalindrome_v1(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        # this is where the new strign is created every time on each iteration
        # because in Python strings are immutable
        reversedString += string[i]
    return string == reversedString


# O(n) time | O(n) space, n^2 because of creation a new string on every
# iteration
def isPalindrome_v2(string):
    reversedChars = []
    for i in reversed(range(len(string))):
        # this is where the new strign is created every time on each iteration
        # because in Python strings are immutable
        reversedChars.append(string[i])
    return string == "".join(reversedChars)


# O(n) time | O(n) space (because of the recursion call stack)
def isPalindrome_v3(string, i = 0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome_v3(string, i + 1)


# O(n) time | O(1) space - strictly speaking it is O(n/2) time, but it
# converges to O(n) because "/2" - 2 is a static factor
def isPalindrome_v4(string):
    left = 0
    right = len(string) - 1

    while left <= right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True


print('------Test v1------')
print(isPalindrome_v1("abcdcba") == True)
print(isPalindrome_v1("abb") == False)
print(isPalindrome_v1("abcdefghihgfedcba") == True)
print('------Test v2------')
print(isPalindrome_v2("abcdcba") == True)
print(isPalindrome_v2("abb") == False)
print(isPalindrome_v2("abcdefghihgfedcba") == True)
print('------Test v3------')
print(isPalindrome_v3("abcdcba") == True)
print(isPalindrome_v3("abb") == False)
print(isPalindrome_v3("abcdefghihgfedcba") == True)
print('------Test v4------')
print(isPalindrome_v4("abcdcba") == True)
print(isPalindrome_v4("abb") == False)
print(isPalindrome_v4("abcdefghihgfedcba") == True)
