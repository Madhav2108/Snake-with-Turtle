import turtle
import time
import random

delay = 0.1

score=0
high_score=0

wn=turtle.Screen()
wn.title("Snake Game by Mahesh Sawant")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"
# khana
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)