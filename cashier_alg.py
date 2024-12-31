v = [25, 10, 5, 1]
n = 100
r = len(v) - 1

def change(n, v, r):
    """ returns histogram of coins required to get change for initial value n """
    d = [0, 0, 0, 0] # histogram
    k = 0 # index of v
    while n > 0:
        # find coin smaller than amount
        while k < r and v[k] > n:
            k = k + 1
        # cannot make change
        if v[k] > n:
            return 'no solution'
        # increase number of given coin, subtract value from amount
        else:
            d[k] += 1
            n -= v[k]
    return d 
            
    
print(change(n, v, r))