import turtle
from math import sqrt

## Parameters: turtle object, angle to turn, line length
def draw_hexagon(t, side_len, x_start, y_start):
    t.goto(x_start, y_start)
    # t.setheading(0)
    for i in range(6):
        t.up()
        t.forward(side_len)
        t.down()
        t.left(120)
        t.forward(side_len)
        t.left(120)
        t.up()
        t.forward(side_len)
        t.right(180)
    print("draw_hexagon()", t.heading())

def move_center(t, side_len):

    t.forward(side_len)
    t.left(120)
    t.forward(2 * side_len)
    # t.right(60)
    t.right(180)
    # t.setheading(0)

def main(side_len):
    ## Create a turtle object
    t = turtle.Turtle()
    ## Change pen thickness
    t.pensize(5)
    ## Change the drawing speed
    t.speed(100)

    ## Set the start point
    t.up()
    t.home()
    ## Set turtle's orientation to north
    t.setheading(180)
    t.forward(side_len)
    t.right(60)
    t.forward(side_len)
    t.right(180)
    ## Set turtle's orientation to east
    # t.setheading(0)

    def get_x_y():
        return t.pos()[0], t.pos()[1]

    for i in range(6):
        x, y = get_x_y()
        print(x, y)
        draw_hexagon(t, side_len=side_len, x_start=x, y_start=y)
        t.right(60)
        move_center(t, side_len)


if __name__ == '__main__':
    main(side_len=100)
    ## Listen to events before continuing
    # turtle.mainloop()
    turtle.exitonclick()
    try:
        turtle.bye()
    except:
        pass
