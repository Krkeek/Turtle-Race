from turtle import Turtle
import random


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

    return turtles


def t_start_race(turtles, user_bet):

    race_over = False

    while not race_over:
        for turtle in turtles:
            turtle.forward(random.randint(1, 10))
            t_pos = turtle.position()[0]
            if t_pos >= 220:
                if turtle.color()[0] == user_bet:
                    print("You win!")
                else:
                    print(f"You lose. The {turtle.color()[0]} turtle is the winner, not the {user_bet} one.")
                race_over = True






