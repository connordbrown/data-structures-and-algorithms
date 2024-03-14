def five_sort(nums):
  i = 0
  j = len(nums) - 1
  while (i <= j):
    if (nums[j] == 5): # must check j first in case j is already 5
      j -= 1
    elif (nums[i] == 5):
      nums[i], nums[j] = nums[j], nums[i] # Pythonic swap notation - can also use temp variable
      i += 1
    else:
      i += 1
  return nums

assert five_sort([12, 5, 1, 5, 12, 7]) == [12, 7, 1, 12, 5, 5]
assert five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]) == [2, 2, 10, 6, 1, 5, 5, 5, 5, 5]  
assert five_sort([5, 5, 5, 1, 1, 1, 4]) == [4, 1, 1, 1, 5, 5, 5] 
assert five_sort([5, 5, 6, 5, 5, 5, 5]) == [6, 5, 5, 5, 5, 5, 5]
assert five_sort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]) == [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5] 

fours = [4] * 20000
fives = [5] * 20000
nums = fours + fives
# twenty-thousand 4s followed by twenty-thousand 5s
assert five_sort(nums) == sorted(nums)
