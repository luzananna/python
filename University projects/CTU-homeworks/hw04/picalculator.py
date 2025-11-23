import math 
def leibnizPi(n):  
    a = 0 
    for b in range(n): 
        s = (-1) ** b / (2 * b + 1) 
        a += s 
     
    return a * 4 
def newtonPi(x0): 
    x1 = 0 
    while True: 
        x1 = x0 - (math.sin(x0) / math.cos(x0))  
        if x1 == x0: 
            return x1 
        else: 
            x0 = x1 
def nilakanthaPi(x): 
    sum = 3 
    k = 2 
    s = 1 
    for i in range(x - 1): 
        sum += s * (4 / ((k) * (k + 1) * (k + 2))) 
        s *= -1 
        k += 2 
    return float(sum)
