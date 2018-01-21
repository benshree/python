#ColorSpiral.py

import turtle
t = turtle.Pen()
turtle.bgcolor("black")
#you can chose between 2 and 8 sides for some cool shapes!
sides = (input("Enter a number of sides between 2 and 8:"))
sides = int(sides)
colors = []
for j in range(1, sides+1):
    col = input("Enter color"+ str(j) +":")
    colors.append(col)


for x in range(60):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides + x)
    t.left(360/sides)
    t.width(x*sides/200)
    


  
