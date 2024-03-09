def anagrams(s1, s2):
  return char_count(s1) == char_count(s2)
  
def char_count(s):
  count = {}
  for char in s:
    count[char] = count.get(char, 0) + 1
  return count

assert anagrams('restful', 'fluster') == True
assert anagrams('cats', 'tocs') == False
assert anagrams('monkeyswrite', 'newyorktimes') == True
assert anagrams('paper', 'reapa') == False
assert anagrams('elbow', 'below') == True
assert anagrams('tax', 'taxi') == False
assert anagrams('taxi', 'tax') == False
assert anagrams('night', 'thing') == True
assert anagrams('abbc', 'aabc') == False
assert anagrams('po', 'popp') == False
assert anagrams('pp', 'oo') == False