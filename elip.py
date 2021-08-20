import turtle
import random
'''t = turtle.Turtle()
i=0
while i<2:
    t.circle(100,90)
    t.circle(50,90)
    i+=1
turtle.done()'''

t = turtle.Turtle()
t.speed(20)
i=0
while i < 36:
    j=0
    while j<2:
        t.circle(100,90)
        t.circle(50,90)
        j+=1
    i+=1
    t.rt(10)
turtle.done()
