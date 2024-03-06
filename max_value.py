def max_value(nums):
  max = float('-inf')
  
  for num in nums:
    if num > max:
      max = num
      
  return max

assert(max_value([4, 7, 2, 8, 10, 9])) == 10
assert(max_value([10, 5, 40, 40.3])) == 40.3
assert(max_value([-5, -2, -1, -11])) == -1
assert(max_value([42])) == 42
assert(max_value([1000, 8, 9000])) == 9000
assert(max_value([2, 5, 1, 1, 4])) == 5