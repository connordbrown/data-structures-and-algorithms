def reverse_string(s):
  if len(s) == 0:
    return ""

  # just change order in which chars are concatenated
  return reverse_string(s[1:]) + s[0]


assert reverse_string("hello") == "olleh"
assert reverse_string("abcdefg") == "gfedcba"
assert reverse_string("stopwatch") == "hctawpots"
assert reverse_string("") == ""

