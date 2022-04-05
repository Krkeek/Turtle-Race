from turtle import Screen
from functions import *

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="user_bet", prompt="Which turtle will win the race? Enter a color: ").lower()
turtles = t_setup()
t_start_race(turtles, user_bet)

screen.exitonclick()
