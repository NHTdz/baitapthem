import turtle
t= turtle.Turtle()
def heart_shape():
    t.fillcolor('red')
    t.begin_fill()
    for x in range(5):
        t.fd(100)
        t.rt(90)
    t.rt(90)
    t.end_fill()
    t.begin_fill()
    t.circle(50)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.circle(50)
    t.end_fill()
    t.bk(100)
    t.lt(90)
for x in range(4):
    heart_shape()
    t.rt(360/4)

turtle.done()