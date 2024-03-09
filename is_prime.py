from math import sqrt, floor

def is_prime(n):
  # not prime by default
  if n < 2:
    return False
  # sqrt is inflection point for factors
  for i in range(2, floor(sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

assert is_prime(1) == False
assert is_prime(2) == True 
assert is_prime(3) == True 
assert is_prime(4) == False
assert is_prime(5) == True 
assert is_prime(6) == False
assert is_prime(7) == True 
assert is_prime(8) == False
assert is_prime(25) == False
assert is_prime(31) == True
assert is_prime(2017) == True 
assert is_prime(2048) == False
assert is_prime(713) ==  False