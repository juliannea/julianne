def is_rightangled(a, b, c):
    
    return ((a ** 2 + b ** 2) - (c ** 2)) < 0.001

is_rightangled(2,3,5)