import turtle


t = turtle.Turtle()
# For circle...
# t.color("red")
# t.fillcolor("blue")
# t.begin_fill()
# t.circle(50)
# t.end_fill()

# for polygone

points = [(10, 10), (15, 30), (140, 10), (10, 100)]

t.fillcolor("red")
t.begin_fill()

t.penup()
t.goto(points[0])
t.pendown()


for point in points[1:]:
    t.goto(point)

t.end_fill()

t.penup()
t.goto(100, 0)
t.pendown()

for _ in range(4):
    t.forward(100)
    t.right(90)

t.penup()
t.goto(-100, -220)
t.pendown()

for _ in range(2):
    t.forward(150)
    t.right(90)
    t.forward(75)
    t.right(90)


t.hideturtle()

turtle.done()
