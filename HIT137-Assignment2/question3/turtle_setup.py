import turtle


def setup_turtle(start_length):
    """Configures the turtle for tree drawing."""
    turtle.title("Recursive Tree Drawing")
    turtle.speed("fastest")
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -250)
    turtle.pendown()
    turtle.color("brown")
    turtle.forward(start_length)
    turtle.color("green")
