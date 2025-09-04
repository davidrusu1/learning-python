import turtle
import random

screen = turtle.Screen()
screen.bgcolor("lightgreen")
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_petal(radius, color):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.circle(radius, 60)
        t.left(120)
    t.end_fill()

def draw_flower(x, y, petale=6, radius=10, color="red"):

    t.penup()
    t.goto(x, y)
    t.setheading(-90)
    t.pendown()
    t.color("green")
    t.pensize(1)
    t.forward(25)

    # Floricica
    t.penup()
    t.goto(x, y)
    t.setheading(random.randint(0, 360))
    t.pendown()
    t.color(color)
    for _ in range(petale):
        draw_petal(radius, color)
        t.left(360 / petale)

colors = ["red", "orange", "magenta", "yellow", "purple", "blue"]
for _ in range(100):
    x = random.randint(-380, 380)
    y = random.randint(-280, 280)
    petale = random.choice([5, 6, 7])
    raza = random.randint(5, 12)
    culoare = random.choice(colors)
    draw_flower(x, y, petale, raza, culoare)

turtle.done()
