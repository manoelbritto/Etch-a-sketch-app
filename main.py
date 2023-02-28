from turtle import Turtle, Screen

timy = Turtle()
screen = Screen()

angle = 10
distance = 10
initial_position = (0, 0)

def move_forward():
    timy.fd(distance)

def move_backwards():
    timy.backward(distance)

def move_right():
    timy.right(angle)

def move_left():
    timy.left(angle)

def clear():
    timy.reset()

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='d', fun=move_right)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='c', fun=clear)

screen.exitonclick()