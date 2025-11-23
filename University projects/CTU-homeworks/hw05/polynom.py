def polyEval(poly, x):
    a = poly[-1]
    for i in range (len(poly)-2, -1, -1):
        a = poly[i] + a*x
    return a

def polySum(poly1, poly2): 
    result = [] 
    min_l = min(len(poly1), len(poly2)) 
 
    for i in range(0, min_l): 
        result.append(poly1[i] + poly2[i]) 
 
    if len(poly1) < len(poly2): 
        result += poly2[min_l : ] 
    elif len(poly1) > len(poly2): 
        result += poly1[min_l : ] 
 
    while result[-1] == 0: 
        del result[-1] 
 
    return result
    

def polyMultiply(poly1, poly2):
    result = ((len(poly1) - 1) + (len(poly2) - 1) + 1) * [0] 
 
    for i in range(0, len(poly1)): 
        for j in range(0, len(poly2)): 
            result[i + j] += poly1[i] * poly2[j] 
 
    return result
   
