# Mr E is growing magic beans again, but this time for a different purpose.
# He wants to grow specific lengths of bean stalks to use as bridges and ladders for his pet frogs.

# He starts with a 1 inch cutting of a stalk, and each day he can apply one drop of one of four fertilizers to it, 
# making it grow either 1, 4, 5, or 11 inches, depending on the fertilizer. He wishes to get a bean stalk of length n 
# using the minimum number of drops of fertilizer, and he doesn't want to cut the finished stalk (you cannot shorten a stalk).

# Your goal is to use dynamic programming to find out how to grow a stalk of length n from a stalk of length 1 using the least number of steps.


# 1A: Write a recurrence
def minDrops(j, n):
    """
    Gets minimum number of drops of fertilizer needed to grow a stalk from
    j inches to n inches.
    """
    # base case: initial length of stalk
    if (n == j):
        return 0
    # base case: invalid stalk length
    if (n < j):
        return float('inf')
    
    # possible growth lengths for different drops
    drops = [1, 4, 5, 11]
    
    # start with worst possible min_drops
    min_drops = float('inf')
    
    # iterate through different drops
    for drop in drops:
        # add 1 for each drop used
        num_drops = 1 + minDrops(j, n - drop)
        # get minimum number of drops
        min_drops = min(min_drops, num_drops)
        
    return min_drops


# 1B: Memoize the recurrence
def minDrops_Memoize(n): 
    # must return a number
    # answer must coincide with recursive version
    # assume that j = 1 is always the starting point.
    
    # possible growth lengths for different drops
    drops = [1, 4, 5, 11]
    
    # create empty memo table - array of size (n + 1)
    T = [None] * (n + 1)
    
    # call helper function
    return _minDrops_Memoize(n, drops, T)

def _minDrops_Memoize(length, drop_sizes, memo):
    # base case - length already calculated
    if memo[length] != None:
        return memo[length]
    
    # base case - initial length
    if length == 1:
        return 0
    
    # base case - invalid stalk length
    if length < 1:
        return float('inf')
    
    min_drops = float('inf')
    for drop in drop_sizes:
        # add 1 for each drop used
        num_drops = 1 + _minDrops_Memoize(length - drop, drop_sizes, memo)
        # get minimum number of drops
        min_drops = min(min_drops, num_drops)
    
    # put min_drops into memo table
    memo[length] = min_drops

    # return final minimum
    return min_drops


# Test 1A
# assert minDrops(1, 9) == 2  # should be 2
# assert minDrops(1, 13) == 2 # should be 2
# assert minDrops(1, 19) == 4 # should be 4
# assert minDrops(1, 34) == 3 # should be 3
# assert minDrops(1, 43) == 5 # should be 5

# Test 1B
assert minDrops_Memoize(9) == 2  # should be 2
assert minDrops_Memoize(13) == 2 # should be 2
assert minDrops_Memoize(19) == 4 # should be 4
assert minDrops_Memoize(34) == 3 # should be 3
assert minDrops_Memoize(43) == 5 # should be 5