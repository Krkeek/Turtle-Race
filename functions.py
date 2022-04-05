from turtle import Turtle, Screen


def t_setup():
    t_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    t_pos = [-100, -50, 0, 50, 100, 150]
    turtles = []

    for _ in range(6):
        turtles.append(Turtle(shape="turtle"))

    for turtle in turtles:
        turtle.penup()
        turtle.color(t_colors[turtles.index(turtle)])
        turtle.goto(x=-230, y=t_pos[turtles.index(turtle)])





