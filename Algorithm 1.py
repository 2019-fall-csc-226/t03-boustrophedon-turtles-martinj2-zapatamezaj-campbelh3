######################################################################
# Author: Jose Zapata & Joey Martin
# Username: zapatmezaj & martinj2
#
# Assignment: T03: Boustrophedon Turtles
# Purpose: Introduces the use of functions with the turtle library
######################################################################
# Acknowledgements:
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################
import turtle
# import turtle files


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

sam.forward(650)
sam.right(90)
sam.forward(500)
sam.right(90)
sam.forward(650)
sam.right(90)
sam.forward(500)


bob.penup()
bob.setpos(-300, 250)
bob.pendown()
# move the origin of the turtle to the upper left hand side of the screen

def main():
    wn = turtle.Screen()
    # makes the screen for the turtle
    for i in range(9):
        bob.forward(600)
        bob.right(90)
        bob.forward(25)
        bob.right(90)
        bob.forward(600)
        bob.left(90)
        bob.forward(25)
        bob.left(90)
        # loop the movement of the turtle to make it fill the screen
    bob.forward(600)
    wn.exitonclick()
    # end program by clicking on the screen

main()
# start the loop




