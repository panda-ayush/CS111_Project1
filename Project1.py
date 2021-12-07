######################################################
# Project: Project 1
# Student Name:  Ayush Panda
# UIN: 671442036
# URL: <address to your Repl.it for the project>
#
######################################################

import turtle
import random

t1 = turtle.Turtle()
t2 = turtle.Turtle()

window = turtle.Screen()
window.screensize(500, 500)

def draw_rectangle(turtle,x_cord, y_cord, turt_heading, fill_color, turt_pensize, length, width):
    turtle.pensize(turt_pensize)
    turtle.heading(turt_heading)
    turtle.goto(x_cord, y_cord)
    for i in range(2):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)

def draw_triangle(turtle, x_cord, y_cord, turt_heading, fill_color, turt_pensize, side_length):
    turtle.pensize(turt_pensize)
    turtle.heading(turt_heading)
    turtle.goto(x_cord, y_cord)
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120)

def draw_circle(turtle,x_cord, y_cord, turt_heading, turt_pensize, fill_color, radius, extent, steps):
    turtle.begin_fill(fill_color)
    turtle.pensize(turt_pensize)
    turtle.heading(turt_heading)
    turtle.penup()
    turtle.goto(x_cord, y_cord)
    turtle.pendown()
    turtle.circle(radius, extent, steps)
    turtle.end_fill(fill_color)

def draw_shape(turtle, star_amount, star_length, x_cord = 0, y_cord = 0):
    turtle.fillcolor("Red")
    turtle.begin_fill()
    for i in range(star_amount):
        turtle.penup()
        x_cord = random.randint(-100, 100)
        y_cord = random.randint(-100, 100)
        turtle.goto(x_cord, y_cord)
        turtle.pendown()
        for i in range(5):
            turtle.forward(star_length)
            turtle.left(144)
    turtle.end_fill()

window = turtle.Screen().exitonclick()

def draw_object():
    pass

def draw_background(turtle):
   turtle.window.bgcolor("black")


def main():
    draw_circle(t1, 0, 0, 0, 1, "LightGrey", 100, 1, 1)
    # draw_shape(t2, 50, 15, 0, 0, )
    print("Name: Ayush Panda") #prints the name of person who made project
    print("UIN: 671442036") #prints the UIN for who made the project

#turtle(name the parametert), x, y, heading, pensize, pen_color, and fill_color,
#draw_rectangle(t1, 50, 25)
#draw_triangle(t1, 25)
#draw_circle(t1, 50, 360, 360)
draw_shape(t1, 5, 20)
#look into position function, tracer function, speed fucntion, screen.setup, screensize, bgcolor()
# main()

window = turtle.Screen().exitonclick()