# MAX HEAP - current configuration
# To implement MIN HEAP - reverse signs in bubble_up and bubble_down comparisons
# Base data structure - array/list

def bubble_up(arr, i):
  """Recursively bubbles up an element at index i in the array."""
  if i <= 0:
    return
  
  parent_idx = (i - 1) // 2
  if arr[i] > arr[parent_idx]:
      arr[i], arr[parent_idx] = arr[parent_idx], arr[i]
      bubble_up(arr, parent_idx)

def bubble_down(arr, i, n):
  """Recursively bubbles down an element at index i in the array."""
  # current/parent index
  largest = i
  # left child of current index
  left = 2 * i + 1
  # right child of current index
  right = 2 * i + 2

  # if left child is bigger than current
  if left < n and arr[left] > arr[largest]:
    largest = left

  # if right child is bigger than current
  if right < n and arr[right] > arr[largest]:
    largest = right

  # if largest value is no longer parent, swap values
  # and recursively call bubble_down on new largest value
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    bubble_down(arr, largest, n)

def heapify(arr):
  """Builds a max heap from the given array."""
  n = len(arr)
  for i in range(n // 2 - 1, -1, -1): # indices n // 2 - 1 have no children, so nothing happens
    bubble_down(arr, i, n)

def extract_max(arr):
    """Given a heap a, extract_max(a) will swap the root with the last child of the heap, then fix the heap"""
    n = len(arr)
    # extract elements one by one - exclude extracted elements from next iteration (sorting in place)
    for i in range(n - 1, 0, -1):
        # swap max element to end of array and decrement index recursively
        arr[i], arr[0] = arr[0], arr[i]
        bubble_down(arr, 0, i)

def heapsort(arr):
  """Sorts the given array in place using heapsort."""
  # build a max heap
  heapify(arr)
  # extract elements in sorted order
  extract_max(arr)

test_cases = [ 
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [0, 0, 0, 0, 0, 0, -1],
        [10, -10, 9, -9, 8, -8, 7, -7]
    ]

for test in test_cases:
  expected_output = sorted(test)
  heapsort(test)
  assert test == expected_output