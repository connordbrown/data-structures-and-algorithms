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