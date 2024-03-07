def compress(s):
  s += '!' # dummy character to indicate change
  i = 0 # current index
  j = 0 # count
  output = ""
  while (j < len(s)):
    if s[j] == s[i]:
      j += 1
    else:
      if j - i == 1:
        output += s[i]
      else:
        output += str(j - i) + s[i]
      i = j
  return output