import turtle
from time import sleep
import random
import os

#window
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#snake
snk = turtle.Turtle()
snk.speed(0)
snk.shape("square")
snk.color("grey")
snk.shapesize(stretch_wid=1, stretch_len=1)
snk.penup()
snk.goto(0,0)
snk.direction = ("up")
snk.dx = 0.1
snk.dy = 0.1


#vars 
lst = 0
x = 0
y = 0
notlost = True
showpos = True

# lost text
def lose():
	pen = turtle.Turtle()
	pen.speed(0)
	pen.color("black")
	pen.penup()
	pen.hideturtle()
	pen.shape("square")
	pen.shapesize(stretch_wid=3,stretch_len=6)
	pen.goto(0,0)
	pen.write("You've lost!", align="center",font=("Courier",40,"bold"))
	wn.bgcolor("red")
	
#pos text
pos = turtle.Turtle()
pos.speed(0)
pos.color("white")
pos.penup()
pos.hideturtle()
pos.shape("square")
pos.shapesize(stretch_wid=3,stretch_len=6)
pos.goto(250,250)
#pos.write("x = 0\ny = 0", align="right", font=("Courier", 24))

	#Food
food = turtle.Turtle()
food.speed(0)
food.color("red")
food.penup()
food.shape("circle")
food.shapesize(stretch_wid=1,stretch_len=1)

ranfoodposx = (random.randint(-14,14)* 20)
ranfoodposy = (random.randint(-14,14)* 20)

food.goto(ranfoodposx, ranfoodposy)

bodys = []
# body
def newbody():
	
	foodfree = False
	body = turtle.Turtle()
	body.speed(0)
	body.color("grey")
	body.penup()
	body.shape("square")
	bodys.append(body)
	newfoodx = random.randint(-14,14)* 20
	newfoody = random.randint(-14,14)* 20
	while foodfree == False:
		for i in range(len(bodys)):
			if (newfoodx < snk.xcor() + 10 and newfoodx > snk.xcor() - 10 and newfoody < snk.ycor() + 10 and newfoody > snk.ycor() - 10) or (newfoodx < bodys[i].xcor() + 10 and newfoodx > bodys[i].xcor() - 10 and newfoody < bodys[i].ycor() + 10 and newfoody > bodys[i].ycor() - 10):
				newfoody = random.randint(-14,14)* 20
				newfoodx = random.randint(-14,14)* 20

			else:
				foodfree = True

	food.goto(newfoodx,newfoody)
	

def PullBody():
	
	for i in range(len(bodys) -1, 0, -1):
		
		x = bodys[i-1].xcor()
		y = bodys[i-1].ycor()
		bodys[i].goto(x,y)
	if len(bodys) > 0:
		bodys[0].goto(snk.xcor(),snk.ycor())
		
			
		

		
		


#funktion
def move():
	if snk.direction == ("up"):
		y = snk.ycor()
		snk.sety(y + 20)
	if snk.direction == ("left"):
		x = snk.xcor()
		snk.setx(x - 20)
	if snk.direction == ("down"):
		y = snk.ycor()
		snk.sety(y - 20)
	if snk.direction == ("right"):
		x = snk.xcor()
		snk.setx(x + 20)

def snk_up():
	if snk.direction != ("down"):
		snk.direction = ("up")

def snk_left():
	if snk.direction != ("right"):
		snk.direction = ("left")

def snk_down():
	if snk.direction != ("up"):
		snk.direction = ("down")

def snk_right():
	if snk.direction != ("left"):
		snk.direction = ("right")


#Keyboard input
wn.listen()
wn.onkeypress(snk_up,"Up")
wn.onkeypress(snk_down,"Down")
wn.onkeypress(snk_left,"Left")
wn.onkeypress(snk_right,"Right")


# Main Game
while True:
	while notlost == True:
		PullBody()
		wn.update()
		if (snk.xcor() <= food.xcor() + 10 and snk.xcor() >= food.xcor() - 10) and (snk.ycor() <= food.ycor() + 10 and snk.ycor() >= food.ycor() - 10):
			if len(bodys) == 0:
				newbody()			
			newbody()

		for i in range(len(bodys) -1, 0, -1):
			if ((snk.ycor() < (bodys[i].ycor() + 10 )) and (snk.ycor() > (bodys[i].ycor() - 10))) and ((snk.xcor() < (bodys[i].xcor() + 10)) and (snk.xcor() > (bodys[i].xcor() - 10))):
				lose()
				notlost = False

		if snk.xcor() < -299 or snk.xcor() > 299 or snk.ycor() < -299 or snk.ycor() > 299:
			lose()
			snk.ht()
			pos.ht()
			pos.clear()
			pos.write("")
			wn.update()
		else :
			sleep(0.1)
			posx = snk.xcor()
			posy = snk.ycor()
			if showpos == True:
				pos.clear()
				pos.write("x = {} \n y = {}".format(posx, posy), align="center", font=("Courier", 12))

			move()

# Made By Alex Bruksch / Sturm2002
# Somewhere end 2019 