import turtle
t = turtle.Turtle()
d=1
b = float(input("Nhập khoảng cách max:"))
while True:
    t.fd(d)
    t.lt(45)
    d+=1
    a= t.distance(0,0)
    if a >= b:
        print("done!")
        break
turtle.done()