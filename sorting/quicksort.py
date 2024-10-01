def swap(a, m, n):
    temp = a[m]
    a[m] = a[n]
    a[n] = temp

def partition(a):
    # get first and last indices of a
    low = 0
    high = len(a) - 1
 
    # set pivot to rightmost element
    pivot = a[high]
    
    # pointers for swapping array values
    i = low - 1
    j = 0
    
    # swap elements according to relationship with pivot
    while (j < high):
        if a[j] < pivot:
            swap(a, i + 1, j)
            i = i + 1
        j = j + 1
        
    # swap pivot into final location
    swap(a, i + 1, high)
    
    return i + 1
    
def quicksort(a):
    # return once a has been divided into small enough pieces
    if len(a) <= 1:
        return

    # divide a into two subarrays using p
    p = partition(a)
    left_arr = a[:p]
    right_arr = a[p + 1:]
    
    # recursively sort each half
    quicksort(left_arr)
    quicksort(right_arr)
    
    # create reference to update a with sorted values
    a[:] = left_arr + [a[p]] + right_arr


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
    quicksort(case)
    # check for equality
    assert case == sorted_case