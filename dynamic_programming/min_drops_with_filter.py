# Mr E has noticed something quite strange: Any bean stalk whose length leaves a remainder of 2 when divided by 7 dies overnight.
# He demands you change your algorithm to avoid these 'dead lengths.'
# You think it might just be his cat digging around in the pots late at night, but you don't wish to argue.

# 2A: Write a recurrence minGoodDrops(j, n) that represents the minimum number of drops of fertilizer necessary to grow a bean stalk
# from j inches to n inches, avoiding any intermediate stage of length k when k mod 7 = 2.
def minGoodDrops(j, n):
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
        # get new_length based on drop size
        new_length = n - drop
        
        # check that new_length is not 'dead length' - could also check for negative length to speed up calculation
        if new_length % 7 != 2:
            # add 1 for each drop used
            num_drops = 1 + minGoodDrops(j, n - drop)
            # get minimum number of drops
            min_drops = min(min_drops, num_drops)
        
    return min_drops


# 2B: Memoize the recurrence in 2A - the memo table  𝑇[0],…,𝑇[𝑛] should store the value of minDrops(j, n).
def minGoodDrops_Memoize(n): 
    # must return a number
    # answer must coincide with recursive version
    # assume that j = 1 is always the starting point.
    
    # possible growth lengths for different drops
    drops = [1, 4, 5, 11]
    
    # create empty memo table - array of size (n + 1)
    T = [None] * (n + 1)
    
    # call helper function
    return _minGoodDrops_Memoize(n, drops, T)

def _minGoodDrops_Memoize(length, drop_sizes, memo):
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
        # get new_length based on drop size
        new_length = length - drop
        
        # check that new_length is not 'dead length' - could also check for negative length to speed up calculation
        if new_length % 7 != 2:
            # add 1 for each drop used
            num_drops = 1 + _minGoodDrops_Memoize(length - drop, drop_sizes, memo)
            # get minimum number of drops
            min_drops = min(min_drops, num_drops)
    
    # put min_drops into memo table
    memo[length] = min_drops

    # return final minimum
    return min_drops


# 2C: Recover the solution in terms of growth from each drop of fertilizer
def minGoodDrops_Solution(n): 
    # must return a number
    # answer must coincide with recursive version
    # assume that j = 1 is always the starting point.
    
    # possible growth lengths for different drops
    drops = [1, 4, 5, 11]
    
    # create empty memo table - array of size (n + 1)
    T = [None] * (n + 1)
    
    # create empty drops_used table
    drops_used = [None] * (n + 1)
    
    # call helper functions to get tuple solution
    return _minGoodDrops_Solution(n, drops, T, drops_used), get_path(n, drops_used)

def get_path(n, S):
    # create empty fertilizer per drop list
    fert_per_drop = []
    
    # calculate specific path used to get minDropsTotal - cannot go past n = 1
    while (n > 1):
        if S[n] != None:
            fert_per_drop.append(S[n])
            n = n - S[n]
    
    return fert_per_drop

def _minGoodDrops_Solution(length, drop_sizes, memo, drops_used):
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
        # get new_length based on drop size
        new_length = length - drop
        
        # check that new_length is not 'dead length' - could also check for negative length to speed up calculation
        if new_length % 7 != 2:
            # add 1 for each drop used
            num_drops = 1 + _minGoodDrops_Solution(length - drop, drop_sizes, memo, drops_used)
            # get minimum number of drops
            if num_drops < min_drops:
                min_drops = num_drops
                best_drop = drop
    
    # put min_drops into memo table
    memo[length] = min_drops
    
    # update drops_used only if a better solution is found
    if drops_used[length] is None or num_drops < memo[length]:
        drops_used[length] = best_drop

    # return final minimum
    return min_drops

# Test 2A
# assert minGoodDrops(1, 9) == 2  # should be 2
# assert minGoodDrops(1, 13) == 2 # should be 2
# assert minGoodDrops(1, 19) == 4 # should be 4
# assert minGoodDrops(1, 34) == 5 # should be 5
# assert minGoodDrops(1, 43) == 5 # should be 5
# assert minGoodDrops(1, 55) == 6 # should be 6 

# Test 2B
# assert minGoodDrops_Memoize(9) == 2    # should be 2
# assert minGoodDrops_Memoize(13) == 2   # should be 2
# assert minGoodDrops_Memoize(19) == 4   # should be 4
# assert minGoodDrops_Memoize(34) == 5   # should be 5
# assert minGoodDrops_Memoize(43) == 5   # should be 5
# assert minGoodDrops_Memoize(55) == 6   # should be 6
# assert minGoodDrops_Memoize(69) == 8   # should be 8
# assert minGoodDrops_Memoize(812) == 83 # should be 83

# Test 2C
assert minGoodDrops_Solution(9)[0] == 2   # should be 2, [4, 4]
assert len(minGoodDrops_Solution(9)[1]) == 2
assert minGoodDrops_Solution(13)[0] == 2   # should be 2, [11, 1]
assert len(minGoodDrops_Solution(13)[1]) == 2
assert minGoodDrops_Solution(19)[0] == 4   # should be 4, [4, 5, 4, 5]
assert len(minGoodDrops_Solution(19)[1]) == 4
assert minGoodDrops_Solution(34)[0] == 5   # should be 5, [5, 1, 11, 11, 5]
assert len(minGoodDrops_Solution(34)[1]) == 5
assert minGoodDrops_Solution(43)[0] == 5   # should be 5, [4, 5, 11, 11, 11]
assert len(minGoodDrops_Solution(43)[1]) == 5
assert minGoodDrops_Solution(55)[0] == 6   # should be 6, [5, 11, 11, 11, 11, 5]
assert len(minGoodDrops_Solution(55)[1]) == 6
assert minGoodDrops_Solution(69)[0] == 8   # should be 8, [11, 1, 11, 11, 11, 11, 11, 1]
assert len(minGoodDrops_Solution(69)[1]) == 8
assert minGoodDrops_Solution(812)[0] == 83 # should be 83, [5, 11, 11, 11, 11, 5, 11, 11, 11, 11, 5, 11, 11, 11, 11, 5, 11, 11, 11, 11, 5, 11, 11, 11, 11, 5, 11, 11, 11, 11, 5, 11, 11, 11, 11, 5, 11, 11, 11, 11, 5, 11, 11, 11, 11, 5, 11, 11, 11, 11, 5, 11, 11, 11, 11, 5, 11, 11, 11, 11, 5, 11, 11, 11, 11, 5, 11, 11, 11, 11, 5, 11, 11, 11, 11, 5, 11, 11, 11, 11, 5, 11, 11]
assert len(minGoodDrops_Solution(812)[1]) == 83