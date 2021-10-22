import turtle
t = turtle.Turtle()
def rectangular(width, length, color):
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for x in range(2):
        t.fd(width)
        t.lt(90)
        t.fd(length)
        t.lt(90)
    t.end_fill()
    t.penup()
color_room = input("Input your color of room you want:")
color_window = input("Input your color of window you want:")
color_livingroom = input("Input your color of livingroom you want:")
color_door = input("Input your color of door you want:")
rectangular(140, 200, color_room)     #room1
t.goto(45,70)
rectangular(50, 60, color_window)
t.goto(140,0)
rectangular(140, 200, color_room)     #room2
t.goto(185,70)
rectangular(50, 60, color_window)
t.goto(140,200)
rectangular(140, 200, color_room)     #room3
t.goto(185,270)
rectangular(50, 60, color_window)
t.goto(0,200)
rectangular(140, 200, color_room)     #room4
t.goto(45,270)
rectangular(50, 60, color_window)
t.goto(280,0)
rectangular(200, 200, color_livingroom)#livingroom
t.goto(340,0)
rectangular(40, 90, color_door)
t.goto(380,0)
rectangular(40, 90, color_door)
turtle.done()