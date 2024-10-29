from turtle import *


# for i in range(10):
#     forward(15)
#     left(9)

# first custom function
def left_turn():
    color("red", "yellow")
    begin_fill()
    for i in range(40):
        forward(15)
        left(9)
    end_fill()


left_turn()

bye()
