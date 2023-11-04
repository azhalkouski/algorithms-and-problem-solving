# O(n * m) time | O(n * m) space
def semordnilap(words):
  wordSet = set(words)
  semordnilapPairs = []

  for word in words:
    reverse = word[::-1]
    if reverse in wordSet and reverse != word:
      semordnilapPairs.append([word, reverse])
      wordSet.remove(word)
      wordSet.remove(reverse)
  
  return semordnilapPairs


print(semordnilap(["aaa", "bbbb"]) == [])
print(semordnilap(["dog", "hello", "desserts", "test", "god", "stressed"]) == [['dog', 'god'], ['desserts', 'stressed']])
print(semordnilap(["abcdefghijk", "aaa", "hello", "racecar", "kjihgfedcba"]) == [["abcdefghijk", "kjihgfedcba"]])
