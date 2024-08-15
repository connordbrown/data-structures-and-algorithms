def sum_of_lengths(strings):
  if len(strings) == 0:
    return 0
  return len(strings[0]) + sum_of_lengths(strings[1:])

assert sum_of_lengths(['goat', 'cat', 'purple']) == 13
assert sum_of_lengths(['bike', 'at', 'pencils', 'phone']) == 18
assert sum_of_lengths([]) == 0
assert sum_of_lengths(['', ' ', '  ', '   ', '    ', '     ']) == 15
assert sum_of_lengths(['0', '313', '1234567890']) == 14 
