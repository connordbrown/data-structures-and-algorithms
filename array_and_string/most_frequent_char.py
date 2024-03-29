def most_frequent_char(s):
  count_dict = {}
  for char in s:
    count_dict[char] = count_dict.get(char, 0) + 1
  
  most_frequent = None
  for char in s:
    if most_frequent is None or count_dict[char] > count_dict[most_frequent]:
      most_frequent = char
  return most_frequent

assert most_frequent_char('bookkeeper') == 'e'
assert most_frequent_char('david') ==  'd'
assert most_frequent_char('abby') == 'b' 
assert most_frequent_char('mississippi') == 'i' 
assert most_frequent_char('potato') == 'o' 
assert most_frequent_char('eleventennine') == 'e'
assert most_frequent_char('riverbed') ==  'r'