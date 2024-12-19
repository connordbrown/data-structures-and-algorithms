def binary_search(a, val):
    """Given sorted array a, returns index of a given value if found, else -1."""
    # get beginning and ending indices of a
    low = 0
    high = len(a) - 1
    
    # compare low and high indices to locate an i such that a[i] == i
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == val:
            return mid
        elif a[mid] > val:
            high = mid - 1
        else:
            low = mid + 1    
    return -1

# testing
array = [1, 2, 3, 4, 5, 6, 7, 8]
assert binary_search(array, 3) == 2
assert binary_search(array, 10) == -1