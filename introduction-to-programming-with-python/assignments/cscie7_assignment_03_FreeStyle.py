## Preesa
import turtle


def set_up_screen():
    ## Create a turtle window object
    screen = turtle.Screen()
    ## Maximize the screen
    screen.setup(width=0.5, height=1.0)
    ## Change the title of the turtle window
    screen.title("See Python turtle draw flag of Thailand! ~Preesa")


def draw_stripe(t, fill_color: str, flag_wid: int, flag_len: int) -> None:
    """This function draws a color-filled stripe."""
    t.pendown()
    t.color(fill_color, fill_color)
    t.begin_fill()
    ## Set turtle's orientation to east
    t.setheading(0)
    t.forward(flag_len)
    t.right(90)
    ## Each stripe on the TH flag is one sixth of its width
    t.forward(flag_wid/6)
    t.right(90)
    t.forward(flag_len)
    t.right(90)
    t.forward(flag_wid/6)
    t.end_fill()
    ## Set turtle's orientation to south
    t.setheading(270)
    t.forward(flag_wid/6)
    t.penup()


def draw_flag(width):
    ## Create a turtle object
    t = turtle.Turtle()
    ## Change pen thickness
    t.pensize(1)
    ## Set drawing speed
    t.speed(100)

    ## Flag ratio
    flag_wid = width
    flag_len = (9/6) * flag_wid

    ## Pen up and go to the top left corner of the flag
    t.penup()
    t.goto(-(flag_len/2), flag_wid/2)
    ## Start drawing
    colors = ["red", "white", "blue"]
    for color in colors:
        draw_stripe(t, color, flag_wid, flag_len)
    for color in colors[::-1]:
        draw_stripe(t, color, flag_wid, flag_len)
    ## Make turtle invisible
    t.hideturtle()


if __name__ == '__main__':
    set_up_screen()
    draw_flag(width=200)
    ## Listen to events before continuing
    # turtle.mainloop()
    try:
        turtle.exitonclick()
    except:
        print("The program didn't exit properly!")

## Reference:
### TH flag ratio: https://asean.org/wp-content/uploads/2012/05/Flag-of-the-Kingdom-of-Thailand.pdf
