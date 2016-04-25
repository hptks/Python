import turtle

def draw():
    window=turtle.Screen()
    window.bgcolor("black")

    turtle=turtle.Turtle()
    turtle.shape("turtle")
    turtle.color("black")
    turtle.goto(-150,-150)
    turtle.color("white")
    turtle.speed(5)
    for i in range(1,4):
        turtle.forward(400)
        turtle.left(120)

    n=200
    for i in range(1,4):
        turtle.forward(n)
        turtle.left(60)
        turtle.forward(n)
        turtle.left(120)
        turtle.forward(n)
        turtle.left(120)
        turtle.forward(n)
        n=n/2
        turtle.left(60)

    window.exitonclick()
    
draw()
