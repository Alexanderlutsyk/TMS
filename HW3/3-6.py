import turtle
import random

radius = random.randint(100,300)
x = turtle.xcor()
y = turtle.ycor()
speed = 2
while True:
    turtle.forward(speed)
    turtle.right(10)
    speed += 0.05
    if turtle.distance(x, y) > radius:
        break
input()        
