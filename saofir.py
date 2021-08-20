import turtle
sc = turtle.Screen()
sc.bgcolor("gray")
sc.title("Star")
#bút
Sao = turtle.Turtle()
Sao.speed(0)
Sao.color("yellow")
#vẽ
for j in range (1,100):
    for i in range (1,6):
        Sao.left(144)
        Sao.forward(200)
    Sao.left(5)
turtle.done()