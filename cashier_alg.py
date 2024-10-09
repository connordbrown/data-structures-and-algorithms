v = [25, 10, 5, 1]
n = 65
r = len(v) - 1

def change(n, v, r):
    """ returns histogram of coins required to get change for initial value n """
    d = [0, 0, 0, 0]
    k = 0    
    while n > 0:
        while k < r and v[k] > n:
            k = k + 1
        if v[k] > n:
            return 'no solution'
        else:
            d[k] += 1
            n -= v[k]
    return d 
            
    
print(change(n, v, r))