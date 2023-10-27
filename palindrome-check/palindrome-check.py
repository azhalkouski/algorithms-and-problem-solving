# O(n) time | O(1) space - strictly speaking it is O(n/2) time, but it
# converges to O(n) because "/2" - 2 is a static factor
def isPalindrome(string):
    left = 0
    right = len(string) - 1

    while left <= right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True

print(isPalindrome("abcdcba") == True)
print(isPalindrome("abb") == False)
print(isPalindrome("abcdefghihgfedcba") == True)
