import turtle

wn = turtle.Screen()

pirate = turtle.Turtle()

for turn in [160.-43,270,-97,-43,200,-940,17,-86]:
    pirate.left(turn)  ##repeats turns for all degrees listed
    pirate.forward(100)
    
print ("The pirate heading is", pirate.heading())

wn.exitonclick()
