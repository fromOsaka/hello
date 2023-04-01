from turtle import Turtle
r = Turtle()
m = 30 
for i in range(4):
    r.forward(5*m)
    r.right(90)
r.penup()
for x in range(0,10):
    for y in range(-10,10):
        r.goto(x*m,y*m)
        r.dot(2,'red')