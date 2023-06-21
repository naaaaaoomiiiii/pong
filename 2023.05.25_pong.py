import time
import turtle
import sys


# Fenster erstellen
window = turtle.Screen()
window.title("Startseite")
window.bgcolor("black")
window.setup(width=800, height=600)

# Turtle für den "Play"-Knopf erstellen
play_button = turtle.Turtle()
play_button.speed(0)
play_button.color("light blue")
play_button.penup()
play_button.hideturtle()
play_button.goto(0, 0)
play_button.write("Play", align="center", font=("Courier", 24, "normal"))



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



width=800
height=600
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width, height)
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
ball.speed(0)
ball.shape("square")
ball.color("light blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Keybord binding
wn.listen()
wn.onkeypress(balken_a_up, "w")
wn.onkeypress(balken_a_down, "s")
wn.onkeypress(balken_b_up, "Up")
wn.onkeypress(balken_b_down, "Down")


# main game loop
def play_game(x, y):
    # ergebnis
    ergebnis_a = 0
    ergebnis_b = 0
    # Diese Funktion wird aufgerufen, wenn der Benutzer auf den "Play"-Knopf klickt
    play_button.clear()
    print("Spiel startet!")
    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("light blue")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))

    while True:
        time.sleep(0.001)
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

        if ball.xcor() > 390:
           ball.goto(0, 0)
           ball.dx *= -1
           ergebnis_a += 1
           pen.clear()
           pen.write("Player 1: {} Player 2: {}".format(ergebnis_a, ergebnis_b), align="center", font=("Courier", 24, "normal"))
           if ergebnis_a > 8:
               pen.clear()
               pen.write("Winner: Player 1", align="center", font=("Courier", 24, "normal"))
               time.sleep(5)
               turtle.bye()



        if ball.xcor() < -390:
           ball.goto(0, 0)
           ball.dx *= -1
           ergebnis_b += 1
           pen.clear()
           pen.write("Player 1: {} Player 2: {}".format(ergebnis_a, ergebnis_b), align="center", font=("Courier", 24, "normal"))
           if ergebnis_b > 8:
               pen.clear()
               pen.write("Winner: Player 2", align="center", font=("Courier", 24, "normal"))
               time.sleep(5)
               turtle.bye()





        # Balken und Ball aufeinander prallen
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < balken_b.ycor() + 60 and ball.ycor() > balken_b.ycor() - 60):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < balken_a.ycor() + 40 and ball.ycor() > balken_a.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1

# Den "Play"-Knopf anklickbar machen
turtle.onscreenclick(play_game)

# Hauptprogrammschleife ausführen
turtle.mainloop()





