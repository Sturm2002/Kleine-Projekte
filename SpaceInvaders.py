import turtle
from time import sleep
import os
import random

# Variables & Settings
# Settings
Intervall = 10
Intervall_Bullet = 10

# recomended range = 10-100
minspeed_enemy = 10
maxspeed_enemy = 100
startEnemys = 3
PlayRound = 0

# Variables
EnemyTick = 0
Tick2 = 0
Enemys = []
FlyingBullets = []
ShowLose = False
Left_Pressed = False
Right_Pressed = False
LTimer = 0
RTimer = 0

# Window setting
wn = turtle.Screen()
wn.title("Python Space Invaders")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)

# Paddle Setup
paddle = turtle.Turtle()
paddle.shape("classic")
paddle.tilt(90)
paddle.speed(0)
paddle.penup()
paddle.fillcolor("white")
paddle.goto(0,-300)
paddle.shapesize(6,4,0.3)

# Laser Setup
laser = turtle.Turtle()
laser.color("#dbd6d6")
laser.shape("square")
laser.shapesize(35,0.1)
laser.speed(0)
laser.penup()

# Round Showing Panel Setup
Round_Panel = turtle.Turtle()
Round_Panel.color("white")
Round_Panel.shape("square")
Round_Panel.penup()
Round_Panel.speed(0)
Round_Panel.shapesize(10,30)
Round_Panel.ht()

# Lose Screen Setup

Lose_txt = turtle.Turtle()
Lose_txt.color("red")
Lose_txt.shape("square")
Lose_txt.penup()
Lose_txt.speed(0)
Lose_txt.ht()

def SHLoseText():
    if ShowLose == False:
        Lose_txt.write("You Lost!",align="center",font=("Arial",30,"bold"))
        Lose_txt.ht()
        return
    if ShowLose == True:
        Lose_txt.clear()
        Lose_txt.ht()
        return

def HideAllTurtles():
    Lose_txt.ht()
    Round_Panel.ht()
    laser.ht()
    paddle.ht()


def GenNewEnemy():
    global minspeed_enemy
    global maxspeed_enemy
    Enemy = turtle.Turtle()
    Enemy.shape("triangle")
    Enemy.shapesize(2,2)
    Enemy.penup()
    Enemy.speed(0)
    Enemy.tilt(270)
    Enemy.fillcolor("red")
    Enemy.st()
    #Enemy.goto(100,100)
    RanEnemyIntervall = random.randint(minspeed_enemy,maxspeed_enemy)
    EnemyTick = 0
    RanX = random.randint(-38,38)
    Enemy.setx(RanX * 10)
    Enemy.sety(440)
    Enemys.append([EnemyTick,RanEnemyIntervall*2, Enemy])

def CheckTimer2():
    global Tick2
    global FlyingBullets
    global Intervall_Bullet
    if Tick2 >= Intervall_Bullet:
        if len(FlyingBullets) == 0:
            Tick2 = 0
            return
        elif len(FlyingBullets) == 1:
            FlyingBullets[0].sety(FlyingBullets[0].ycor() + 10)
            Tick2 = 0
            return
        else:
            for i in range(len(FlyingBullets)):
                FlyingBullets[i].sety(FlyingBullets[i].ycor() +10)
                Tick2 = 0
            


def Check_Enemy_Movement():
    global Enemys
    if len(Enemys) == 0:
        pass 

    elif len(Enemys) == 1:
        if Enemys[0][0] >= Enemys[0][1]:
            Enemys[0][2].sety(Enemys[0][2].ycor()-10)
            Enemys[0][0] = 0
    else:
        
        for i in range(len(Enemys)-1):
            if Enemys[i][0] >= Enemys[i][1]:
                Enemys[i][2].sety(Enemys[i][2].ycor()-10)
                Enemys[i][0] = 0
                
        
def AddEnemyCounter():
    global Enemys
    for i in range(len(Enemys)):
        Enemys[i][0] += 1

def Left_Pressed_False():
    global Left_Pressed
    Left_Pressed = False

def Right_Pressed_False():
    global Right_Pressed
    Right_Pressed = False

def Left_Pressed_True():
    global Left_Pressed
    Left_Pressed = True
    
def Right_Pressed_True():
    global Right_Pressed
    Right_Pressed = True




def shoot():
    global FlyingBullets
    if len(FlyingBullets) < ((PlayRound + 3) / 2):   
        bullet = turtle.Turtle()
        bullet.shape("circle")
        bullet.shapesize(1,0.2)
        bullet.penup()
        bullet.speed(0)
        bullet.fillcolor("grey")
        bullet.goto(paddle.xcor(),paddle.ycor()+5)

        FlyingBullets.append(bullet)

def lose():
    HideAllTurtles()
    SHLoseText()
    exit()


def CheckCollision():
    for i in range(len(FlyingBullets)):
        for j in range(len(Enemys)):

            if FlyingBullets[i].xcor() < Enemys[j][2].xcor() + 20 and FlyingBullets[i].xcor() > Enemys[j][2].xcor() - 20 and FlyingBullets[i].ycor() < Enemys[j][2].ycor() + 20 and FlyingBullets[i].ycor() > Enemys[j][2].ycor() - 20:
                FlyingBullets[i].ht()
                FlyingBullets.pop(i)
                Enemys[j][2].ht()
                Enemys.pop(j)
                return

            if FlyingBullets[i].ycor() > 410:
                FlyingBullets.pop(i)
                return

            if Enemys[j][2].ycor() < -300:
                lose()
            

def RoundEndStart():
    global PlayRound
    if len(Enemys) == 0:
        for i in range(len(FlyingBullets)-1):
            FlyingBullets[i].ht()
            FlyingBullets.pop(i)
        PlayRound += 1
        paddle.ht()
        laser.ht()
        paddle.goto(0,-300)
        for i in range(3):

            Round_Panel.write("Round {} ".format(PlayRound),align="center",font=("Arial",20,"bold"))
            wn.update()
            sleep(0.3)
            
            Round_Panel.clear()
            wn.update()
            sleep(0.3)
        paddle.st()
        laser.st()
        for i in range(PlayRound + 3):
            GenNewEnemy()


wn.listen()
wn.onkeypress(Left_Pressed_True,"Left")
wn.onkeyrelease(Left_Pressed_False,"Left")

wn.onkeypress(Right_Pressed_True,"Right")
wn.onkeyrelease(Right_Pressed_False,"Right")

wn.onkeypress(shoot,"space")

#for i in range(startEnemys):
#    GenNewEnemy()
# Main Loop
while True:

    if Right_Pressed == True:
        if RTimer >= 2:
            if paddle.xcor() < 370:
                paddle.setx(paddle.xcor() + 1)
                wn.update()
            RTimer = 0


    if Left_Pressed == True:
        if LTimer >= 2:
            if paddle.xcor() > -370:
                paddle.setx(paddle.xcor() - 1)
                wn.update()
            LTimer = 0


    RoundEndStart()

    laser.goto(paddle.xcor(),paddle.ycor() + 330)

    CheckCollision()
    Check_Enemy_Movement()
    AddEnemyCounter()

    #os.system("cls")
    CheckTimer2()

    Tick2 += 1
    RTimer += 1
    LTimer += 1

    wn.update()
    

