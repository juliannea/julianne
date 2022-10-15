
c = input("length of longest triangle side")
a = input("length of one triangle side")
b = input("length of one triangle side")

c_int = int(c)
a_int = int(a)
b_int = int(b)

return abs((a_int ** 2 + b_int ** 2) - c_int ** 2)< .0001
        

