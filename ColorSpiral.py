#ColorSpiral.py

import turtle
t = turtle.Pen()
turtle.bgcolor("black")
#you can chose between 2 and 6 sides for some cool shapes!
sides = (input("Enter a number of sides between 2 and 6:"))
sides = int(sides)
colors = []

  
if sides == 2:
    col = input("Enter color 1:")
    colors.append(col)
    co = input("Enter color 2:" )
    colors.append(co)
elif sides == 3:
    col = input("Enter color 1:")
    colors.append(col)
    co = input("Enter color 2:" )
    colors.append(co)
    co = input("Enter color 3:" )
    colors.append(co)

elif sides == 4:
    col = input("Enter color 1:")
    colors.append(col)
    co = input("Enter color 2:" )
    colors.append(co)
    colo = input("Enter color 3:" )
    colors.append(colo)
    color = input("Enter color 4:" )
    colors.append(color)

elif sides == 5:
    col = input("Enter color 1:")
    colors.append(col)
    co = input("Enter color 2:" )
    colors.append(co)
    colo = input("Enter color 3:" )
    colors.append(colo)
    color = input("Enter color 4:" )
    colors.append(color)
    color = input("Enter color 5:" )
    colors.append(color)
   
elif sides == 6:
    col = input("Enter color 1:")
    colors.append(col)
    co = input("Enter color 2:" )
    colors.append(co)
    colo = input("Enter color 3:" )
    colors.append(colo)
    color = input("Enter color 4:" )
    colors.append(color)
    color = input("Enter color 5:" )
    colors.append(color)
    colorx = input("Enter color 6:" )
    colors.append(colorx)

else :
    print("sorry, try again")
    


for x in range(60):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides + x)
    t.left(360/sides)
    t.width(x*sides/200)
