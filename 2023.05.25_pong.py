import time
import turtle
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Balken A
balken_a = turtle.Turtle()
balken_a.speed(0)
balken_a.shape("square")
balken_a.color("light blue")
balken_a.shapesize(stretch_wid=5, stretch_len=0.5)
balken_a.penup()
balken_a.goto(-350, 0)

# Balken B
balken_b = turtle.Turtle()
balken_b.speed(0)
balken_b.shape("square")
balken_b.color("light blue")
balken_b.shapesize(stretch_wid=5, stretch_len=0.5)
balken_b.penup()
balken_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0.01)
ball.shape("square")
ball.color("light blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2


# Function
def balken_a_up():
    y = balken_a.ycor()
    y += 20
    balken_a.sety(y)

def balken_a_down():
    y = balken_a.ycor()
    y -= 20
    balken_a.sety(y)

def balken_b_up():
    y = balken_b.ycor()
    y += 20
    balken_b.sety(y)

def balken_b_down():
    y = balken_b.ycor()
    y -= 20
    balken_b.sety(y)

# Keybord binding
wn.listen()
wn.onkeypress(balken_a_up, "w")
wn.onkeypress(balken_a_down, "s")
wn.onkeypress(balken_b_up, "Up")
wn.onkeypress(balken_b_down, "Down")


# main game loop
while True:
    time.sleep(1)
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1



