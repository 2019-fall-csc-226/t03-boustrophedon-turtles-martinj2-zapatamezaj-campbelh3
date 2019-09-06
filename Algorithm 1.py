import turtle

def draw_turtle(colr, sz):
    """
      Draw a turtle with the given color and pensize.
      Then it returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

bob = draw_turtle(back,25)

#next step is to make a window