def pair_product(numbers, target_product):
  previous_numbers = {}
  
  for index, num in enumerate(numbers):
    complement = target_product / num
    
    if complement in previous_numbers:
      return (previous_numbers[complement], index) # current index, complement index
  
    # put num into dictionary if not present
    previous_numbers[num] = index

assert pair_product([3, 2, 5, 4, 1], 8) == (1, 3)
assert pair_product([3, 2, 5, 4, 1], 10) == (1, 2)
assert pair_product([4, 7, 9, 2, 5, 1], 5) == (4, 5)
assert pair_product([4, 7, 9, 2, 5, 1], 35) == (1, 4)
assert pair_product([3, 2, 5, 4, 1], 10) == (1, 2)
assert pair_product([4, 6, 8, 2], 16) == (2, 3)