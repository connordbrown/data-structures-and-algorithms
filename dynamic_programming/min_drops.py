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


# 1B: Memoize the recurrence - the memo table  𝑇[0],…,𝑇[𝑛] should store the value of minDrops(j, n).
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


# 1C: Recover the solution - modify the solution from part B to also return which fertilizer Mr E needs to use at each step.
# Result must be a pair: minimum number of total drops, list of fertilizer per drop: each element of this list must be 1, 4, 5 or 11
def minDrops_Solution(n): # Assume that j = 1 is always the starting point
   # must return a pair of number, list
   # number returned is the same as minDrops_Memoize
   # list must be a list of consisting of elements [1,4, 5, 11]
    
    # possible growth lengths for different drops
    drop_sizes = [1, 4, 5, 11]
    
    # create empty memo table - array of size (n + 1)
    T = [None] * (n + 1)
    
    # create empty drops_used table
    drops_used = [None] * (n + 1)
    
    # call helper functions to get tuple solution
    return _minDrops_Solution(n, drop_sizes, T, drops_used), get_path(n, drops_used)

def get_path(n, S):
    # create empty fertilizer per drop list
    fert_per_drop = []
    
    # calculate specific path used to get minDropsTotal - cannot go past n = 1
    while (n > 1):
        if S[n] != None:
            fert_per_drop.append(S[n])
            n = n - S[n]
    
    return fert_per_drop

def _minDrops_Solution(length, drop_sizes, memo, drops_used):
    # base case - length already calculated
    if memo[length] != None:
        return memo[length]
    
    # base case - initial length
    if length == 1:
        return 0
    
    # base case - invalid stalk length
    if length < 1:
        return float('inf')
    
    # minimum number of drops required
    min_drops = float('inf')
    # drop type used for a given minimum number of drops
    best_drop = None

    for drop in drop_sizes:
        # add 1 for each drop used
        num_drops = 1 + _minDrops_Solution(length - drop, drop_sizes, memo, drops_used)
        # get minimum number of drops
        if num_drops < min_drops:
            min_drops = num_drops
            best_drop = drop

    # put min_drops into memo table
    memo[length] = min_drops
    
    # update drops_used only if a better solution is found
    if drops_used[length] == None or num_drops < memo[length]:
        drops_used[length] = best_drop
    
    # return final minimum
    return min_drops


# Test 1A
# assert minDrops(1, 9) == 2  # should be 2
# assert minDrops(1, 13) == 2 # should be 2
# assert minDrops(1, 19) == 4 # should be 4
# assert minDrops(1, 34) == 3 # should be 3
# assert minDrops(1, 43) == 5 # should be 5

# Test 1B
# assert minDrops_Memoize(9) == 2  # should be 2
# assert minDrops_Memoize(13) == 2 # should be 2
# assert minDrops_Memoize(19) == 4 # should be 4
# assert minDrops_Memoize(34) == 3 # should be 3
# assert minDrops_Memoize(43) == 5 # should be 5

# Test 1C
assert minDrops_Solution(9) == (2, [4, 4])               # should be 2, [4, 4]
assert minDrops_Solution(13) == (2, [1, 11])             # should be 2, [1, 11]
assert minDrops_Solution(19) == (4, [1, 1, 5, 11])       # should be 4, [1, 1, 5, 11]
assert minDrops_Solution(34) == (3, [11, 11, 11])        # should be 3, [11, 11, 11]
assert minDrops_Solution(43) == (5, [4, 5, 11, 11, 11])  # should be 5, [4, 5, 11, 11, 11]