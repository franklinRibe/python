import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

tarta = turtle.Turtle()
tarta.color("blue")
tarta.pensize(3)

mick = turtle.Turtle()
mick.color("Yellow")
mick.pensize(5)


for i in range(10):

    tarta.forward(50)
    mick.left(200)
    tarta.left(120)
    mick.forward(200)
    tarta.forward(10)
    mick.right(80)

window.exitonclick()