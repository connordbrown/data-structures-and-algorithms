def pair_product(numbers, target_product):
  previous_numbers = {}
  
  for index, num in enumerate(numbers):
    complement = target_product / num
    
    if complement in previous_numbers:
      return (index, previous_numbers[complement]) # current index, complement index
  
    # put num into dictionary if not present
    previous_numbers[num] = index

pair_product([3, 2, 5, 4, 1], 8) # -> (1, 3)
pair_product([3, 2, 5, 4, 1], 10) # -> (1, 2)
pair_product([4, 7, 9, 2, 5, 1], 5) # -> (4, 5)
pair_product([4, 7, 9, 2, 5, 1], 35) # -> (1, 4)
pair_product([3, 2, 5, 4, 1], 10) # -> (1, 2)
pair_product([4, 6, 8, 2], 16) # -> (2, 3)