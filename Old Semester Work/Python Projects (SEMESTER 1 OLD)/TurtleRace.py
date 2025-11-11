import turtle
from random import randint

window = turtle.Screen()
window.bgcolor('lightgreen')

larry = turtle.Turtle()
larry.shape('turtle')
larry.color('darkgreen')
larry.penup()
larry.left(180)
larry.forward(200)  
larry.right(90)
larry.pendown()
larry.forward(randint(0, 200))

curly = turtle.Turtle()
curly.shape('circle')
curly.color('red')
curly.left(90)
curly.forward(randint(0, 200))

moe = turtle.Turtle()
moe.shape('turtle')
moe.color('blue')
moe.penup()
moe.forward(200)
moe.left(90)
moe.pendown()
moe.forward(randint(0, 200))

window.exitonclick()