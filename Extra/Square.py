# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  11/14/2022

import turtle

window = turtle.Screen()
window.bgcolor("red")


def draw_square(some_turtle):
  for i in range(1, 5):
    some_turtle.forward(100)
    some_turtle.right(90)


def draw_art():
  brad = turtle.Turtle()
  brad.shape("turtle")
  brad.color("yellow")
  brad.speed(5)
  for i in range(1, 37):
    draw_square(brad)
    brad.right(10)


draw_art()

window.exitonclick()
