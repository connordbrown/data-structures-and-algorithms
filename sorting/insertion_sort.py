def insertion_sort(a):
    for i in range(1, len(a)): # must start at 1
        # for loop implementation
        # for j in range(i - 1, -1, -1):
        #     if a[j] > a[j + 1]:
        #         a[j], a[j + 1] = a[j + 1], a[j]

        # while loop implementation
        j = i - 1 # can also do j = i, must alter swap variables
        while j >= 0 and a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            j = j - 1

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
    insertion_sort(case)
    # check for equality
    assert case == sorted_case