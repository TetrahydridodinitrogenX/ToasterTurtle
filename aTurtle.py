import turtle

def draw_circle(turtle, color, size, x, y)
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.pendown()

toaster = turtle.Turtle()
toaster.shape(turtle)
toaster.speed(10)

draw_circle(toaster, green, 50, 25, 0)
draw_circle(toaster, blue, 50, 0, 0)
draw_circle(toaster, yellow, 50, -25, 0)