from turtle import *

bgcolor('#1e2d40')
speed(0)
hideturtle()
for i in range(100):
    color('#01f6bd')
    circle(i)
    color('#72fcdc')
    circle(i*0.8)
    right(4)
    forward(4)
done()