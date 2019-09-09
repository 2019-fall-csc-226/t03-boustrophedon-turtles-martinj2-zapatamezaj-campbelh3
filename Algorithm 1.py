import turtle
# import turtle files

wn = turtle.Screen()
# makes the screen for the turtle

def draw_turtle(colr, sz):
    """
      Draw a turtle with the given color and pensize.
      Then it returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

bob = draw_turtle('red', 25)
# draw the turtle given the color and size

sam = draw_turtle('blue', 25)

sam.penup()
sam.setpos(-325, 275)
sam.pendown()

bob.penup()
bob.setpos(-300, 250)
bob.pendown()
# move the origin of the turtle to the upper left hand side of the screen

def move_turtle():
    for i in range(13):
        bob.forward(650)
        bob.right(90)
        bob.forward(25)
        bob.right(90)
        bob.forward(650)
        bob.left(90)
        bob.forward(25)
        bob.left(90)
# loop the movement of the turtle to make it fill the screen

move_turtle()
# start the loop

wn.exitonclick()
# end program by clicking on the screen