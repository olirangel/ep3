
import turtle
#turtle.shape("arrow")
#60
for i in range(0,4):
    turtle.forward(20)
    turtle.right(90)


turtle.penup()
turtle.forward(50)
turtle.pendown()


#61
for i in range (0,3):
    turtle.forward(30)
    turtle.right(120)


turtle.penup()
turtle.forward(50)
turtle.pendown()

#62
for i in range (0,20):
    turtle.forward(5)
    turtle.right(20)

turtle.exitonclick()

import turtle
#63
turtle.color("yellow")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(30)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(60)
turtle.pendown()


turtle.color("black")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(30)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(60)
turtle.pendown()


turtle.color("red")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(30)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(60)
turtle.pendown()


turtle.color("blue")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(30)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(60)
turtle.pendown()


#64
turtle.color("black")
for i in range(0,5):
    turtle.forward(100)
    turtle.right(144)
turtle.exitonclick()

import turtle
import random
#EJERCICIO 65
#1
turtle.left(90)
turtle.forward(120)
turtle.right(90)

turtle.penup()
turtle.forward(30)
turtle.pendown()
#2
turtle.forward(60)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(60)

turtle.penup()
turtle.forward(30)
turtle.pendown()
#3
turtle.forward(60)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(60)

turtle.penup()
turtle.right(180)
turtle.forward(60)
turtle.pendown()

turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(60)
#FIN
turtle.exitonclick()



import turtle
import random
#66
for i in range (0,8):
    color = random.choice(["red","pink","green","orange","yellow","blue"])
    turtle.color(color)
    turtle.forward(50)
    turtle.right(45)
turtle.exitonclick()




import turtle
#for i in range (0,10):
#    turtle.right(30)
#    for i in range (0,8):
#        turtle.forward(20)
#        turtle.right(30)
#67
for i in range (0,10):
    turtle.right(36)
    for i in range (0,8):
        turtle.forward(100)
        turtle.right(45)

turtle.exitonclick()


import turtle
import random
#68
lin= random.randint(5, 20)
for x in range(0, lin):
    length = random.randint(25,100)
    random.randint(1,365)
    rotar = turtle.forward(length)
    turtle.right(rotar)
    turtle.exltoneliek()





