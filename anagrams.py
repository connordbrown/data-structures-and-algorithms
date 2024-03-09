def anagrams(s1, s2):
  return char_count(s1) == char_count(s2)
  
def char_count(s):
  count = {}
  for char in s:
    count[char] = count.get(char, 0) + 1
  return count