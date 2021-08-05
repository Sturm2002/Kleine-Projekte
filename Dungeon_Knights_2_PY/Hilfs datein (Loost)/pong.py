import turtle
import os
from time import sleep


# Settings

# Score needed to win
winscore = 3
# Player Names
playername_a = ("Spieler 1")
playername_b = ("Spieler 2")
# Paddle Sizes
paddle_size = 60
# Float digits
flt_dgt = 3
# Speed added after Point
pt_speed = 0.05
# Speed added after Paddle touch
tch_speed = 0.01
# Ball Speed

ball_speed = 0.2

wn = turtle.Screen()
wn.title("Python Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=(paddle_size / 10),stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=(paddle_size / 10),stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup()
ball.goto(0,0)
bspeed = 0.1
ball.dx = ball_speed
ball.dy = ball_speed



# Scoreboard
score_a = 0
score_b = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,240)
pen.write("{}: 0 | {}: 0 \n Speed : 0.1".format(playername_a, playername_b), align="center", font=("Courier",16,"bold"))

#punkt fuer b
los_a = turtle.Turtle()
los_a.speed(0)
los_a.color("white")
los_a.penup()
los_a.goto(0,0)
los_a.shape("square")
los_a.shapesize(stretch_wid=100, stretch_len=100)

#punkt fuer a
los_b = turtle.Turtle()
los_b.speed(0)
los_b.color("white")
los_b.penup()
los_b.goto(0,100)
los_b.shape("square")
los_b.shapesize(stretch_wid=100, stretch_len=100)

#a gewonnen
win_a = turtle.Turtle()
win_a.speed(0)
win_a.color("white")
win_a.penup()
win_a.goto(0,0)
win_a.shape("square")
win_a.shapesize(stretch_wid=100, stretch_len=100)

# b gewonnen
win_b = turtle.Turtle()
win_b.speed(0)
win_b.color("white")
win_b.penup()
win_b.goto(0,0)
win_b.shape("square")
win_b.shapesize(stretch_wid=100, stretch_len=100)


# Funktion
def paddle_a_up():
	if paddle_a.ycor() < (300 - paddle_size):
		y = paddle_a.ycor()
		y += 20
		paddle_a.sety(y)

def paddle_a_down():
	if paddle_a.ycor() > (-300 + paddle_size):
		y = paddle_a.ycor()
		y -= 20
		paddle_a.sety(y)

def paddle_b_up():
	if paddle_b.ycor() < (300 - paddle_size):
		y = paddle_b.ycor()
		y += 20
		paddle_b.sety(y)

def paddle_b_down():
	if paddle_b.ycor() > (-300 + paddle_size):
		y = paddle_b.ycor()
		y -= 20
		paddle_b.sety(y)

def a_los():
	paddle_b.sety(0)
	paddle_a.sety(0)
	for i in range(3):
		los_a.showturtle()
		wn.update()
		sleep(0.1)
		los_a.hideturtle()
		wn.update()
		sleep(0.1)


def b_los():
	paddle_b.sety(0)
	paddle_a.sety(0)
	for i in range(3):
		los_b.showturtle()
		wn.update()
		sleep(0.1)
		los_b.hideturtle()
		wn.update()
		sleep(0.1)

def win():
	if score_a == winscore:
		win_a.showturtle()
		wtxt_a = turtle.Turtle()
		wtxt_a.speed(0)
		wtxt_a.color("black")
		wtxt_a.penup()
		wtxt_a.hideturtle()
		wtxt_a.goto(0,0)
		wtxt_a.write("{} has won!".format(playername_a), align="center",font=("Courier",24,"bold"))
		wtxt_a.shape("square")
		wtxt_a.shapesize(stretch_wid=30,stretch_len=30)

	elif score_b == winscore:
		win_b.showturtle()
		wtxt_b = turtle.Turtle()
		wtxt_b.speed(0)
		wtxt_b.color("black")
		wtxt_b.penup()
		wtxt_b.hideturtle()
		wtxt_b.write("{} has won!".format(playername_b), align="center",font=("Courier",24,"bold"))
		wtxt_b.goto(0,0)
		wtxt_b.shape("square")
		wtxt_b.shapesize(stretch_wid=30,stretch_len=30)
	else:
		draw = turtle.Turtle
		draw.speed(0)
		draw.color("Black")
		draw.penup()
		draw.hideturtle()
		draw.write("Draw!")


#Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

# Main game loop
while True :

	if score_a < winscore and score_b < winscore:
		
		win_a.hideturtle()
		win_b.hideturtle()
		speed = round(bspeed, flt_dgt)
		los_a.hideturtle()
		los_b.hideturtle()

		wn.update()
		#Move the ball
		ball.setx(ball.xcor() + ball.dx)
		ball.sety(ball.ycor() + ball.dy)

		# Border checking

		#oben
		if ball.ycor() > 290:
			ball.sety(290)
			ball.dy *= -1
		
		#unten
		if ball.ycor() < -290:
			ball.sety(-290)
			ball.dy *= -1
		
		#rechte seite
		if ball.xcor() > 390:
			ball.goto(0,0)
			ball.dx *= -1
			score_a += 1
			b_los()
			bspeed += pt_speed
			pen.clear()
			pen.write("{}: {} | {}: {} \n Speed : {}  ".format(playername_a, score_a,playername_b, score_b, speed), align="center", font=("Courier",16,"bold"))

		#linke seite
		if ball.xcor() < -390:
			ball.goto(0,0)
			ball.dx *= -1
			score_b += 1
			a_los()
			bspeed += pt_speed
			pen.clear()
			pen.write("{}: {} | {}: {} \n Speed : {}  ".format(playername_a, score_a,playername_b,score_b, speed), align="center", font=("Courier",16,"bold"))

		#Paddle Collision
		if ball.xcor() > 340 and (ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + paddle_size and ball.ycor() > paddle_b.ycor() - paddle_size):
			ball.dx *= -1
			ball.setx(340)
			pen.clear()
			bspeed += tch_speed
			pen.write("{}: {} | {}: {} \n Speed : {}  ".format(playername_a, score_a,playername_b,score_b, speed), align="center", font=("Courier",16,"bold"))

		if ball.xcor() < -340 and (ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + paddle_size and ball.ycor() > paddle_a.ycor() - paddle_size):
			ball.dx *= -1
			ball.setx(-340)
			pen.clear()
			bspeed += tch_speed
			pen.write("{}: {} | {}: {} \n Speed : {}  ".format(playername_a, score_a,playername_b,score_b, speed), align="center", font=("Courier",16,"bold"))
	else :
		win()
		wn.update()
		# made by Sturm2002