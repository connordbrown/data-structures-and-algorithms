def uncompress(s):
  output = []
  i = 0
  j = 0
  while j < len(s):
    if s[j].isnumeric():
       j += 1
    else:
      # multiple number by letter, append to output
      output.append(int(s[i:j]) * s[j])
      j += 1
      # advance i to j to restart cycle
      i = j
      
  return ''.join(output)

assert uncompress("2c3a1t") == 'ccaaat'
assert uncompress("4s2b") == 'ssssbb'
assert uncompress("4s2b") == 'ssssbb'
assert uncompress("3n12e2z") == 'nnneeeeeeeeeeeezz'
assert uncompress("127y") == 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'