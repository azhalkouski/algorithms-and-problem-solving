# BRUTE FORCE
# O(n + n) time | O(n) space, which gives us O(n) time | O(n) space
def firstNonRepeatingCharacter_v1(string):
    for i in range(len(string)): # O(n) time | O(1) space
        # O(n) time | O(n) space since we make a copy with the slices
        if string[:i].find(string[i]) == -1 and string[i+1:].find(string[i]) == -1:
            return i
    return -1


# OPTIMAL SOLUTION
# O(n) time | O(1) space, the reason it is O(n) time is because we actually have O(n + n),
# which is O(2N) and we eliminate this '2' as a constant factor, which leaves us with
# O(n) time
def firstNonRepeatingCharacter_v2(string):
    # since we know that this particular problem works with lowercase English letters
    # we know that we're going  to deal with only 26 characters, thus we can create
    # a hashmap and consider it to be a constant operation, because regardless of the
    # length of the input string we are not gonna have more than 26 keys in the hashmap
    # so, we consider it to be O(1) space
    charactersFrequencies = {} # O(n) time | O(1) space (as explained above)
    for char in string:
        charactersFrequencies[char] = charactersFrequencies.get(char, 0) + 1

    for i in range(len(string)): # O(n) time | O(1) space
        if charactersFrequencies[string[i]] == 1:
            return i
    return -1


print(firstNonRepeatingCharacter_v1("abcdcaf") == 1)
print(firstNonRepeatingCharacter_v1("ababac") == 5)
print(firstNonRepeatingCharacter_v1("ababacc") == -1)

print(firstNonRepeatingCharacter_v2("abcdcaf") == 1)
print(firstNonRepeatingCharacter_v2("ababac") == 5)
print(firstNonRepeatingCharacter_v2("ababacc") == -1)
