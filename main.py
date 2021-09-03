import turtle
t= turtle.Turtle()
def draw_polygon(a,b):
# a là số cạnh của đa giác
# b là cd các cạnh
    c = 180 - (1 - 2/a)*180
    for x in range(a):
        t.fd(b)
        t.rt(c)

draw_polygon(5,100)
