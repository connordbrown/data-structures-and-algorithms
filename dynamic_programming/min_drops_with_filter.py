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

# Test 2A
assert minGoodDrops(1, 9) == 2 # should be 2
assert minGoodDrops(1, 13) == 2 # should be 2
assert minGoodDrops(1, 19) == 4 # should be 4
assert minGoodDrops(1, 34) == 5 # should be 5
assert minGoodDrops(1, 43) == 5 # should be 5
assert minGoodDrops(1, 55) == 6 # should be 6 