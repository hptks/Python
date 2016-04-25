import turtle

def draw():
    window=turtle.Screen()
    window.bgcolor("black")

    adam=turtle.Turtle()
    adam.shape("turtle")
    adam.color("black")
    adam.goto(-150,-150)
    adam.color("white")
    adam.speed(5)
    for i in range(1,4):
        adam.forward(400)
        adam.left(120)

    n=200
    for i in range(1,4):
        adam.forward(n)
        adam.left(60)
        adam.forward(n)
        adam.left(120)
        adam.forward(n)
        adam.left(120)
        adam.forward(n)
        n=n/2
        adam.left(60)

    window.exitonclick()
    
draw()
