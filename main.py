import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def shift_counter_clockwise():
    tim.left(10)


def shift_clockwise():
    tim.right(10)


def clear_screen():
    turtle.resetscreen()
    # tim.clear()
    # tim.penup()
    # tim.home()
    # tim.pendown()


screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=shift_counter_clockwise)
screen.onkey(key="d", fun=shift_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
