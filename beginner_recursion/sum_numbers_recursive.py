def sum_numbers_recursive(numbers):
  if len(numbers) == 0:
    return 0
  return numbers[0] + sum_numbers_recursive(numbers[1:])


assert sum_numbers_recursive([5, 2, 9, 10]) == 26
assert sum_numbers_recursive([1, -1, 1, -1, 1, -1, 1]) == 1
assert sum_numbers_recursive([]) == 0
assert sum_numbers_recursive([1000, 0, 0, 0, 0, 0, 1]) == 1001
assert sum_numbers_recursive([700, 70, 7]) == 777
assert sum_numbers_recursive([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -55
assert sum_numbers_recursive([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert sum_numbers_recursive([123456789, 12345678, 1234567, 123456, 12345, 1234, 123, 12, 1, 0]) == 137174205
