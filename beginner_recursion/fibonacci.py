def fibonacci(n):
  if n == 0 or n == 1:
    return n
  return fibonacci(n - 2) + fibonacci(n - 1)


assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(8) == 21
