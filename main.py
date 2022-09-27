
def fibanacci(n):
    fi = pow((1 + pow(5, 0.5))/ 2, n)
    fi_ = pow((1 - pow(5, 0.5))/ 2, n)
    result = (fi - fi_)/(5**(1/2))
    if n>=0 and float(n).is_integer():
        return result
    else:
        return "n = 1,2,3..."

print(fibanacci(5))

