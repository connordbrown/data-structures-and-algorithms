
# MAX HEAP - current configuration
# To implement MIN HEAP - reverse signs in bubble_up and bubble_down comparisons

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
  left = 2 * i + 1
  right = 2 * i + 2
  largest = i

  if left < n and arr[left] > arr[largest]:
    largest = left

  if right < n and arr[right] > arr[largest]:
    largest = right

  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    bubble_down(arr, largest, n)

def heapify(arr):
  """Builds a max heap from the given array."""
  n = len(arr)
  for i in range(n // 2 - 1, -1, -1):
    bubble_down(arr, i, n)


def heapsort(arr):
  """Sorts the given array using heapsort."""
  n = len(arr)

  # build a max heap
  heapify(arr)

  # extract elements one by one
  for i in range(n - 1, 0, -1):
    # swap max element to end of array and decrement index recursively
    arr[i], arr[0] = arr[0], arr[i]
    bubble_down(arr, 0, i)

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