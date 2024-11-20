from turtle import *

bgcolor("black")
pencolor("white")
fillcolor("red")
pensize(5)

def heart(f, c):
    begin_fill()
    lt(40)
    fd(f)
    circle(c, 210)
    rt(138)
    circle(c, 210)
    fd(f)
    end_fill()

penup()
goto(-50, -70)
pendown()
heart(140, 70)

penup()
goto(70, 70)
pendown()
left(40)
heart(100, 50)

style = ("arial", 50, "bold")
penup()
goto(-175, -150)
pendown()
write("I Love You", font=style, move=True)

hideturtle()
done()