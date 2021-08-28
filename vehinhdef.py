import turtle
t = turtle.Turtle()
def circle(r):
    t.circle(r)
def square(a):
    for x in range(4):
        t.fd(a)
        t.rt(90)
def rectangle(a,b):
    for x in range(2):
        t.fd(a)
        t.rt(90)
        t.fd(b)
        t.rt(90)
def regular_pentagon(a):
    for x in range(5):
        t.fd(a)
        t.rt(72)
def equilateral_triangle(a):
    for x in range(3):
        t.fd(a)
        t.rt(120)
def oval():
    for x in range(2):
        t.circle(180,90)
        t.circle(90,90)
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
def amount(c):
    for x in range(c):
        t.rt(360/c)
# vẽ hình theo input
shape = input("What do you want to draw?: ")
c = int(input("How many shapes do you want to draw? "))
if shape == "circle":
    r = float(input("The radius of the circle is: "))
    for x in range(c):
        t.rt(360/c)
        circle(r)
elif shape == "square":
    a = float(input("Side length of square is: "))
    for x in range(c):
        t.rt(360/c)
        square(a)
elif shape == "rectangle":
    a, b = eval(float(input("The lengths of the sides of the rectangle is: ")))
    for x in range(c):
        t.rt(360/c)
        rectangle(a,b)
elif shape == "regular_pentagon":
    a = float(input("Side length of regular pentagon is: "))
    for x in range(c):
        t.rt(360/c)
        regular_pentagon(a)
elif shape == "equilateral_triangle":
    a = float(input("Side length of equilateral triangle is: "))
    for x in range(c):
        t.rt(360/c)
        equilateral_triangle(a)
elif shape == "oval":
    for x in range(c):
        t.rt(360/c)
        oval()
elif shape == "heart_shape":
    for x in range(c):
        heart_shape()
        t.rt(360 / c)
else:
    print("Sorry.I don't have this shape.")
turtle.done()
