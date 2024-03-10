def pair_sum(numbers, target_sum):
  previous_numbers = {}
  
  for index, num in enumerate(numbers):
    complement = target_sum - num
    
    if complement in previous_numbers:
      return (previous_numbers[complement], index)
    
    previous_numbers[num] = index

assert pair_sum([3, 2, 5, 4, 1], 8) == (0, 2)
assert pair_sum([4, 7, 9, 2, 5, 1], 5) == (0, 5)
assert pair_sum([4, 7, 9, 2, 5, 1], 3) == (3, 5)
assert pair_sum([1, 6, 7, 2], 13) == (1, 2)
assert pair_sum([9, 9], 18) == (0, 1)
assert pair_sum([6, 4, 2, 8 ], 12) == (1, 3)