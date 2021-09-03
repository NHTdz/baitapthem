import turtle
t = turtle.Turtle()
import math
def draw(r):
    """Hàm vẽ hình tròn với bán kính r"""
    t = turtle.Turtle()
    t.hideturtle()
    t.pencolor('red')
    t.circle(r)
    turtle.done()
def area(r):
    """Hàm tính diện tích hình tròn với bán kính r"""
    return math.pi * r**2
r = float(input("Nhập vào bán kính: "))
draw(r)
s = area(r)
print("Diện tích của hình tròn có bán kính = {} là: {}".format(r, s))