import turtle
#nền
sc = turtle.Screen()
sc.bgcolor("blue")
sc.title("Square")
#turtle
hv = turtle.Turtle()
hv.speed(5)
hv.color("red")
#vẽ
for i in range(4):
  hv.forward(400)
  hv.left(90)
turtle.done()