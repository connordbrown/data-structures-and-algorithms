def partition(a, l, r):
    x = a[r] # pivot
    i = l - 1
    for j in range(l, r):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    # swap pivot back into correct place
    a[i + 1], a[r] = a[r], a[i + 1]
    # return pivot index
    return i + 1


def quickselect(a, j):
    """ Get jth smallest value in an array in linear (if pivot is randomly/deterministically chosen) time."""
    l = 0
    r = len(a) - 1
    # get pivot index
    split_point = partition(a, l, r) 
    # if pivot is correct element, return it
    if split_point == r - j + 1:
        result = a[split_point]
    # if element is to left of pivot, modify j and recursively call quickselect on new j
    elif split_point > r - j + 1:
        result = quickselect(a[:split_point], j - (r - split_point + 1))
    # if element is to right of pivot, modify j and recursively call quickselect on new j
    else:
        result = quickselect(a[split_point + 1: r + 1], j)

    return result


test_cases = [ 
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 2, 8) ,
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 0),
    ([0, 0, 0, 0, 0, 0, -1], 1, 0),
    ([10, -10, 9, -9, 8, -8, 7, -7], 5, -7)
]

for (test_array, j, expected_output) in test_cases:
    output =  quickselect(test_array, j)
    assert output == expected_output