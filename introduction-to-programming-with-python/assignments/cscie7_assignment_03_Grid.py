import turtle


## Parameters: turtle object, length of edge, number of boxes per side
def draw_grid(grid, edge_len, box_num):
    box_len = edge_len / box_num
    ## Draw (box_num+1) parallel lines
    for i in range(box_num+1):
        grid.pendown()
        grid.forward(edge_len)
        grid.penup()
        grid.backward(edge_len)
        ## Skip these steps when drawing the last line
        if i != box_num:
            grid.right(90)
            grid.forward(box_len)
            grid.left(90)
            grid.pendown()


## Create a turtle object
t = turtle.Turtle()
## Change pen thickness
t.pensize(5)

## Start coordinate on the canvas
t.goto(0, 0)
## Draw (4+1) parallel lines of 200 length
draw_grid(t, 200, 4)
## Turn the turtle 90 degrees left to draw verticle lines after the last horizontal line
t.left(90)
## Draw (4+1) parallel lines of 200 length
draw_grid(t, 200, 4)

## Listen to events before continuing
turtle.mainloop()

try:
    ## Shut the turtle graphics window
    turtle.bye()
except:
    ## Used as a placeholder for future code
    pass
