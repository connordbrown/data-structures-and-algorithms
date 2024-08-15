def palindrome(s):
  # given
  if len(s) == 0 or len(s) == 1:
    return True

  # if first and last characters are different
  if s[0] != s[-1]:
    return False

  # slice excludes first and last characters
  return palindrome(s[1:-1])


assert palindrome("pop") == True
assert palindrome("kayak") == True
assert palindrome("pops") == False
assert palindrome("boot") == False
assert palindrome("rotator") == True
assert palindrome("abcbca") == False
assert palindrome("") == True
