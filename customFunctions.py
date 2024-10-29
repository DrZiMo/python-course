from turtle import *


# for i in range(10):
#     forward(15)
#     left(9)

# first custom function
def left_turn(number_of_turns, fill_color):
    color("red", fill_color)
    begin_fill()
    for i in range(number_of_turns):
        forward(15)
        left(9)
    end_fill()


left_turn(40, "yellow")
left_turn(10, "blue")
left_turn(10, "pink")
left_turn(10, "purple")
left_turn(10, "green")

bye()
