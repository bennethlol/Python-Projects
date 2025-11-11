import turtle
# Make canvas
window = turtle.Screen()
window.bgcolor("white")

# Make turtles
turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.color("red")
turtle2 = turtle.Turtle()
turtle2.shape("turtle")
turtle2.color("blue")

# Turtles draw square
for i in range(1,5):
    turtle1.forward(100)
    turtle1.left(90)

for i in range(1,5):
    turtle2.forward(200)
    turtle2.left(90)

window.exitonclick()

