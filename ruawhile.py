import turtle
import random
t = turtle.Turtle()
t.shape("turtle")
t.hideturtle()
t.pensize(3)
t.color("blue")
t.speed(1)
t.penup()
t.goto(-400, 0)
t.showturtle()
dem = 0
while dem < 10:
    # sinh hai giá trị ngẫu nhiên
    down = random.randint(20, 50)
    up = random.randint(20, 50)
    t.pendown()
    '''rùa tiến về phía trước với giá trị ngẫu
        nhiên ở trên, có để lại nét vẽ'''
    t.forward(down)
    t.penup()
    ''' rùa tiến về phía trước với giá trị ngẫu
        nhiên ở trên, không để lại nét vẽ'''
    t.forward(up)
    dem += 1
turtle.done()