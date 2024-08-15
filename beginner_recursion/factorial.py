def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n - 1)


assert factorial(3) == 6
assert factorial(6) == 720
assert factorial(18) == 6402373705728000
assert factorial(1) == 1
assert factorial(13) == 6227020800
assert factorial(0) == 1
