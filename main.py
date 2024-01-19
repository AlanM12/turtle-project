# Turtle Project
# Author: Alan Messeh


import turtle
turtle.shape("turtle") # optional

def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()
def square(len):
    for i in range(4):
        turtle.forward(len)
        turtle.right(90)

def triangle(len):
    for i in range(3):
        turtle.forward(len)
        turtle.left(120)

def house(len):
    square(len)
    triangle(len)
def main():
    turtle.speed(0)
    turtle.color("red")
    house(150)
    turtle.color("blue")
    turtle.penup()
    turtle.forward(200)
    turtle.pendown()
    house(100)

turtle.speed(0) # optional
turtle.color("red")

main()
turtle.Screen().exitonclick()
# #def shape
# turtle.pensize(5)
# turtle.forward(90)
# turtle.left(90)
# turtle.forward(90)
# turtle.left(90)
# turtle.forward(90)
# turtle.left(90)
# turtle.forward(90)
#
# turtle.penup()
# turtle.pendown()
#
# turtle.color("blue")
# turtle.left(90)
# turtle.forward(250)
# turtle.left(90)
# turtle.forward(90)
# turtle.left(90)
# turtle.forward(90)
# turtle.left(90)
# turtle.forward(90)
