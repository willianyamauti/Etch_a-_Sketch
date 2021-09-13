from turtle import Turtle, Screen

# TODO: add new features

brush = Turtle()
my_screen = Screen()


def move_forward():
    brush.forward(10)


def move_backward():
    brush.backward(10)


def turn_counter_clockwise():
    brush.left(10)


def turn_clockwise():
    brush.right(10)


def clean_screen():
    my_screen.resetscreen()


# higher order function, recebe uma função como argumento e
# a função precisa estar sem ()
""" Movements """
my_screen.onkey(key='w', fun=move_forward)
my_screen.onkey(key='s', fun=move_backward)
my_screen.onkey(key='a', fun=turn_counter_clockwise)
my_screen.onkey(key='d', fun=turn_clockwise)

""" Options """
my_screen.onkey(key='c', fun=clean_screen)


my_screen.listen()
my_screen.exitonclick()
