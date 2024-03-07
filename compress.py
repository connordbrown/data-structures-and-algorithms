def compress(s):
  s += '!' # dummy character to indicate change
  i = 0 # current index
  j = 0 # count
  output = []
  while (j < len(s)):
    if s[j] == s[i]:
      j += 1
    else:
      if j - i == 1:
        output.append(s[i])
      else:
        output.append(str(j - i))
        output.append(s[i])
      i = j
  return ''.join(output)

assert compress('ccaaatsss') == '2c3at3s'
assert compress('ssssbbz') == '4s2bz'
assert compress('ppoppppp') == '2po5p'
assert compress('nnneeeeeeeeeeeezz') == '3n12e2z'
assert compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy') == '127y'