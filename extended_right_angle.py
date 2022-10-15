def is_rightangled(a, b, c):
    
    if b > a and b > c:
        return abs((a ** 2 + c ** 2) - (b ** 2)) < 0.001
    elif a > b and a > c:
        return abs((b ** 2 + c ** 2) - (a ** 2)) < 0.001
    else:
        return abs((a ** 2 + b ** 2) - (c ** 2)) < 0.001
     

is_rightangled(2,3,5)