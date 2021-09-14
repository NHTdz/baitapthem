import turtle
square = turtle.Turtle()
def draw_square(angle):
    square.speed(20)
    for i in range(3):
        square.forward(200)
        square.right(90)

    square.forward(200)
    square.right(90 + angle)


step = int(input("Input step:"))
angle = 360 / step
for i in range(step):
    draw_square(angle)

turtle.done()