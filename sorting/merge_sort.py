def merge(left_arr, right_arr, a):
    # pointers for each array
    i = j = k = 0
    
    # lengths of array halves
    m = len(left_arr)
    n = len(right_arr)
    
    # counter for number of comparisons
    counter = 0
    
    # add elements of left_arr and right_arr to a according to element size
    while i < m and j < n:
        if left_arr[i] < right_arr[j]:
            a[k] = left_arr[i]
            i += 1
        else:
            a[k] = right_arr[j]
            j += 1
        k += 1
        counter += 1

    # when all elements are traversed in either left_arr or right_arr, add remaining elements of other array
    while i < m:
        a[k] = left_arr[i]
        i += 1
        k += 1

    while j < n:
        a[k] = right_arr[j]
        j += 1
        k += 1
    
    return counter
    
    
def mergesort(a):
    # return once a has been divided into small enough pieces
    if len(a) <= 1:
        return

    # divide a in half, create two subarrays left_arr and right_arr
    mid = len(a)//2
    left_arr = a[:mid]
    right_arr = a[mid:]

    # recursively sort each half
    mergesort(left_arr)
    mergesort(right_arr)
    
    # join halves together in a
    merge_comparisons = merge(left_arr, right_arr, a)
    
    return merge_comparisons


test_cases = [ 
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [0, 0, 0, 0, 0, 0, -1],
        [10, -10, 9, -9, 8, -8, 7, -7]
]

for case in test_cases:
    # get sorted array for testing
    sorted_case = sorted(case)
    # sort case array in place
    mergesort(case)
    # check for equality
    assert case == sorted_case