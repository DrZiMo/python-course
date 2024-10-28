from turtle import *

#Squrare
color('red')
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

#triangle
color('blue')
right(90)
forward(200)
right(135)
forward(285)

#Letter D
goto(0, 0)
left(-45)
width(50)
left(90)
forward(200)
right(90)
forward(100)
right(45)
forward(71)
right(45)
forward(100)
right(45)
forward(71)
right(45)
forward(100)
hideturtle()

# letter C
width(10)
color("pink")
left(180)
forward(50)
left(45)
forward(50)
left(45)
forward(50)
left(45)
forward(50)

# FILL COLOR
color("red", "yellow")

begin_fill()
for i in range(5):  # drawing a star
    right(180 - 36)
    forward(200)
end_fill()

bye()