import turtle


## Parameters: turtle object, angle to turn, line length
def draw_pentagram(pent, edgeLen, line_len):
    ## Five lines in the star/pentagram so range(5)
    for i in range(5):
        pent.forward(line_len)
        pent.right(edgeLen)


## Create a turtle object
t = turtle.Turtle()
## Change pen thickness
t.pensize(5)

## Start from (0, 0) by default
## 100 steps and turn 144 degrees
draw_pentagram(t, 144, 100)

## Listen to events before continuing
turtle.mainloop()

try:
    ## Shut the turtle graphics window
    turtle.bye()
except:
    ## Used as a placeholder for future code
    pass
