def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        raise ValueError("This operation is not supported for given input parameters")
     
def modulo(x, y):  
    if  x >= y and y > 0:
        return(x%y)
    else:
        raise ValueError("This operation is not supported for given input parameters")

def secondPower(x):
    return(x**2)


def power(x, y):
    if y < 0:
        raise ValueError("This operation is not supported for given input parameters")
    else:
        return float(x**y)


def secondRadix(x):
    if x > 0:
        return x**(1/2)
    else:
        raise ValueError("This operation is not supported for given input parameters")

def magic(x, y, z, k):
    l = x + k 
    m = y + z 
    if m==0:
        raise ValueError("This operation is not supported for given input parameters")
    n = ((l / m) + 1)
    return n


def control(a, x, y, z, k):
    if a == "ADDITION":
        return addition(x,y)
    elif a=="SUBTRACTION": 
        return subtraction(x,y)
    elif a=="MULTIPLICATION": 
        return multiplication(x,y)
    elif a=="DIVISION": 
        return division(x,y)
    elif a=="MOD": 
        return modulo(x,y)
    elif a=="POWER": 
        return power(x,y)
    elif a=="SECONDRADIX": 
        return secondRadix(x)
    elif a=="MAGIC":
        return magic(x, y, z, k)
    else:
        raise ValueError("This operation is not supported for given input parameters")