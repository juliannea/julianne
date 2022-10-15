def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

def is_even_shorter_version(n):
    return n%2 == 0
    


def is_odd(n):
    return not(is_even(n))

def isRightAngle(a,b,c):
    '''
    c is longest
    
    '''
    sum = a*a + b*b
    return abs(math.sqrt(sum)-c) < 0.001

def isRightAngle2(a,b,c):
    '''
    any order for sides
    '''
    
    return isRightAngle2(a,b,c) or \
            isRightAngle2(b,c,a) or \
            isRightAngle2(a,c,b)


result = is_even(10)
print ('Result for 10:', result)
result = is_even(11)
print('Result for 11:', result)

print('Direct Call:', is_even(11)) ##only use print when you want someone using the program to see the output always use return othewise

print('Direct Call:', is_even_shorter_version(12))

print('Result for 3:', is_odd(3))

print(isRightAngle(5,3,4))

print(isRightAngle2(5,3,4))
      

