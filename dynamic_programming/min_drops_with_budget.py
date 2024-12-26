# "Your plans always cost too much!" Mr E exclaimed. He never told you he was on a budget,
# nor how much each fertilizer cost, but somehow he expected you to factor in his fixed income
# while growing his increasingly ornate jungle frog habitats. You delicately ask how much each
# fertilizer costs, and got the following information:  

# Daily growth (in)	Cost ($)
#            1	    1
#            4	    2
#            5	    3
#           11	    7

# Given n, and initial investment 𝐷0, plan how Mr E can grow an n inch bean stalk while avoiding the 'dead lengths' (when the stalk grows to a length 2 mod 7), and not going over budget.

# 3A: Write a recurrence - write a recurrence minDropsWithBudget(j, D, n) given a stalk of length j, with budget D, 
# that returns the minimum number of drops of fertilizer needed to grow to length n, while avoiding any intermediate length k where k = 2 mod 7.
def minDropsWithBudget(j, D, n):
    # base case: initial length of stalk
    if (n == j):
        return 0
    
    # base case: invalid stalk length
    if (n < j):
        return float('inf')
    
    # possible growth lengths and corresponding costs
    drops = [(1, 1), (4, 2), (5, 3), (11, 7)]
    
    # start with worst possible min_drops
    min_drops = float('inf')
    
    # iterate through different drops and their corresponding costs
    for drop, cost in drops:
        # get new_length and new_budget based on drop size
        new_length = n - drop
        new_budget = D - cost
        
        # check if new length is not 'dead length' and cost is within budget - could also check for negative length to speed up calculation
        if new_length % 7 != 2 and new_budget > 0:
            # add 1 for each drop used 
            num_drops = 1 + minDropsWithBudget(j, new_budget, new_length)
            # get minimum number of drops
            min_drops = min(min_drops, num_drops)
    
    return min_drops


# 3B: Memoize the recurrence - Write a memo table to memoize the recurrence.
# Your memo table must be of the form 𝑇[j][d] for j ranging from 1 to 𝑛 and 𝑑 ranging from 0 to D.
# You will have to handle the base cases carefully.
def minDropsWithBudget_Memoize(D, n): 
    # must return a number
    # answer must coincide with recursive version
    # assume that j = 1 is always the starting point.
    
    # possible growth lengths and corresponding costs
    drops = [(1, 1), (4, 2), (5, 3), (11, 7)]
    
    # create empty memo table - array of size (n + 1) * (D + 1)
    T = [[None] * (D + 1) for _ in range(n + 1)]
    
    # call helper function
    return _minDropsWithBudget_Memoize(D, n, drops, T)

def _minDropsWithBudget_Memoize(budget, length, drop_sizes, memo):
    # base case - length and budget already calculated
    if memo[length][budget] != None:
        return memo[length][budget]
    
    # base case: initial length of stalk
    if (length == 1):
        return 0
    
    # base case: invalid stalk length
    if (length < 1):
        return float('inf')
    
    # start with worst possible min_drops
    min_drops = float('inf')
    
    # iterate through different drops and their corresponding costs
    for drop, cost in drop_sizes:
        # get new_length and new_budget based on drop size
        new_length = length - drop
        new_budget = budget - cost
        
        # check if new length is valid, new length is not 'dead length', and cost is within budget
        if new_length > 0 and new_length % 7 != 2 and new_budget > 0:
            # add 1 for each drop used 
            num_drops = 1 + _minDropsWithBudget_Memoize(new_budget, new_length, drop_sizes, memo)
            # get minimum number of drops
            min_drops = min(min_drops, num_drops)
    
    # put min_drops into memo table
    memo[length][budget] = min_drops
    
    return min_drops


# 3C: Recover the solution - Now write code that will also return the minimum number of drops
# along with the list of fertilizers (in order) that will achieve this minimum number.
def minDropsWithBudget_Solution(D, n): 
    # must return a number
    # answer must coincide with recursive version
    # assume that j = 1 is always the starting point.
    
    # possible growth lengths and corresponding costs
    drops = [(1, 1), (4, 2), (5, 3), (11, 7)]
    
    # create empty memo table - array of size (n + 1) * (D + 1)
    T = [[None] * (D + 1) for _ in range(n + 1)]
    
    # create empty drops_used table
    drops_used = [None] * (n + 1)
    
    # call helper function
    return _minDropsWithBudget_Solution(D, n, drops, T, drops_used), get_path(n, drops_used)

def get_path(n, S):
    # create empty fertilizer per drop list
    fert_per_drop = []
    
    # calculate specific path used to get minDropsTotal - cannot go past n = 1
    while (n > 1):
        if S[n] != None:
            fert_per_drop.append(S[n])
            n = n - S[n]
    
    return fert_per_drop

def _minDropsWithBudget_Solution(budget, length, drop_sizes, memo, drops_used):
    # base case - length and budget already calculated
    if memo[length][budget] != None:
        return memo[length][budget]
    
    # base case: initial length of stalk
    if (length == 1):
        return 0
    
    # base case: invalid stalk length
    if (length < 1):
        return float('inf')
    
    # minimum number of drops required
    min_drops = float('inf')
    # drop type used for a given minimum number of drops
    best_drop = None
    
    # iterate through different drops and their corresponding costs
    for drop, cost in drop_sizes:
        # get new_length and new_budget based on drop size
        new_length = length - drop
        new_budget = budget - cost
        
        # check if new length is valid, new length is not 'dead length', and cost is within budget
        if new_length > 0 and new_length % 7 != 2 and new_budget > 0:
            # add 1 for each drop used 
            num_drops = 1 + _minDropsWithBudget_Solution(new_budget, new_length, drop_sizes, memo, drops_used)
            # get minimum number of drops
            if num_drops < min_drops:
                min_drops = num_drops
                best_drop = drop
    
    # put min_drops into memo table
    memo[length][budget] = min_drops
    
    # update drops_used only if a better solution is found
    if drops_used[length] is None or num_drops < memo[length][budget]:
        drops_used[length] = best_drop
    
    return min_drops


# Test 3A
# assert minDropsWithBudget(1, 25, 10) == 2  # must be 2
# assert minDropsWithBudget(1, 25, 6) == 1   # must be 1
# assert minDropsWithBudget(1, 25, 30) == 5  # must be 5
# assert minDropsWithBudget(1, 16, 30) == 7  # must be 7
# assert minDropsWithBudget(1, 18, 31) == 7  # must be 7
# assert minDropsWithBudget(1, 22, 38) == 7  # must be 7
# assert minDropsWithBudget(1, 32, 55) == 11 # must be 11
# assert minDropsWithBudget(1, 35, 60) == 12 # must be 12

# Test 3B
# assert minDropsWithBudget_Memoize(25, 10) == 2 # must be 2
# assert minDropsWithBudget_Memoize(25, 6) == 1 # must be 1
# assert minDropsWithBudget_Memoize(25, 30) == 5 # must be 5
# assert minDropsWithBudget_Memoize(16, 30) == 7 # must be 7
# assert minDropsWithBudget_Memoize(18, 31) == 7 # must be 7
# assert minDropsWithBudget_Memoize(22, 38) == 7 # must be 7
# assert minDropsWithBudget_Memoize(32, 55) == 11 # must be 11
# assert minDropsWithBudget_Memoize(35, 60) == 12 # must be 12

# Test 3C
assert minDropsWithBudget_Solution(25, 10)[0] == 2 # must be 2, [4,5]
assert sum(minDropsWithBudget_Solution(25, 10)[1]) == 9
assert minDropsWithBudget_Solution(25, 6)[0] == 1 # must be 1, [5]
assert sum(minDropsWithBudget_Solution(25, 6)[1]) == 5
assert minDropsWithBudget_Solution(25, 30)[0] == 5 # must be 5, [4, 5, 4, 5, 11]
assert sum(minDropsWithBudget_Solution(25, 30)[1]) == 29
assert minDropsWithBudget_Solution(16, 30)[0] == 7 # must be 7, [4, 5, 4, 4, 4, 4, 4]
assert sum(minDropsWithBudget_Solution(16, 30)[1]) == 29
assert minDropsWithBudget_Solution(18, 31)[0] == 7 # must be 7, [4, 5, 4, 4, 4, 4, 5]
assert sum(minDropsWithBudget_Solution(18, 31)[1]) == 30
assert minDropsWithBudget_Solution(22, 38)[0] == 7 # must be 7,  [4, 5, 4, 4, 4, 5, 11]
assert sum(minDropsWithBudget_Solution(22, 38)[1]) == 37
assert minDropsWithBudget_Solution(32, 55)[0] == 11 # must be 11, [4, 5, 4, 4, 4, 4, 5, 4, 4, 11, 5]
assert sum(minDropsWithBudget_Solution(32, 55)[1]) == 54
assert minDropsWithBudget_Solution(35, 60)[0] == 12 # must be 12, [4, 5, 4, 4, 4, 4, 5, 4, 4, 11, 5, 5]
assert sum(minDropsWithBudget_Solution(35, 60)[1]) == 59