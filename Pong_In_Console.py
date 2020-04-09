from time import sleep
import os
import keyboard
import random

lenght = 60
height = 20
lenpaddles = 7

ypospaddlea = height / 2 - lenpaddles
ypospaddleb = height / 2 - lenpaddles

ballheight = 3
ballwidth = 3

ballxdir = 1
ballydir = 1

points_a = 0
points_b = 0

ballx = 0
bally = 0

ballchar = "X"

paddlewidth = 2
paddlechar = "0"

Intervall = 5

FullLine = (lenght * "#")


def RandomDir():
    global ballxdir,ballydir,lenght,height,ballheight,bally,ballx,paddlewidth

    ballydirrand = random.randint(1,2)
    ballxdirrand = random.randint(1,2)

    ballx = random.randint(paddlewidth + 5, lenght-paddlewidth-5)
    bally = random.randint(1,height - ballheight)


    if ballydirrand == 1:
        ballydir = 1
    else :
        ballydir = -1

    if ballxdirrand == 1:
        ballxdir = 1
    else:
        ballxdir = -1

RandomDir()

def printscreen():
    # Aktualisiert den kompletten "Bildschirm"
    ToPrintLine = ""
    os.system("cls")

    print("Player 1 has : {} Points | Player 2 has : {} Points".format(points_a,points_b))
    print(FullLine)
    for i in range(height):
        if ypospaddlea < i and ypospaddlea > i-lenpaddles and not (ypospaddleb < i and ypospaddleb > i- lenpaddles) :
            ToPrintLine += paddlewidth*paddlechar

            if bally < i and bally > i - ballheight:
                #print("jay")
                for j in range(lenght):
                    j += paddlewidth

                    if ballx > j and ballx < j + ballwidth:
                        #print("jup")
                        ToPrintLine += ballchar
                      

                    else:
                        ToPrintLine += " "
            print(ToPrintLine)
            ToPrintLine = ""
        
        elif (ypospaddlea < i and ypospaddlea > i-lenpaddles) and (ypospaddleb < i and ypospaddleb > i-lenpaddles):
            ToPrintLine += paddlewidth*paddlechar

            if bally < i and bally > i - ballheight:

                for j in range(paddlewidth,lenght - paddlewidth):

                    if ballx > j and ballx < j + ballwidth:
                        ToPrintLine += ballchar

                    else:
                        ToPrintLine += " "

            else:
                ToPrintLine += (lenght-2*paddlewidth) * " "

            ToPrintLine += paddlewidth * paddlechar
            print(ToPrintLine)
            ToPrintLine = ""

        elif ypospaddleb < i and ypospaddleb > i-lenpaddles and not (ypospaddlea < i and ypospaddlea > i- lenpaddles):
            
            if bally < i and bally > i-ballheight:
                for j in range(lenght - paddlewidth):
                    if ballx > j and ballx < j + ballwidth:
                        ToPrintLine += ballchar
                    else:
                        ToPrintLine += " "

            else:
                ToPrintLine += (lenght-paddlewidth)* " "

            ToPrintLine += paddlewidth * paddlechar
            print(ToPrintLine)
            ToPrintLine = ""

        else:
            if bally < i and bally > i-ballheight:
                for j in range(lenght):
                    if ballx > j and ballx < j + ballwidth:
                        ToPrintLine += ballchar
                    else:
                        ToPrintLine += " "
            print(ToPrintLine)
            ToPrintLine = ""
        
    print(FullLine)    


def listenkeyboard():
    global ypospaddlea,ypospaddleb

    if keyboard.is_pressed("down"):
        if ypospaddleb < height-lenpaddles:
            ypospaddleb += 1

    if keyboard.is_pressed("up"):
        if ypospaddleb > -1:
            ypospaddleb -= 1

    if keyboard.is_pressed("s"):
        if ypospaddlea < height - lenpaddles:
            ypospaddlea += 1

    if keyboard.is_pressed("w"):
        if ypospaddlea > -1:
            ypospaddlea -= 1
    
def MoveBall():
    global ballx,ballxdir,ballheight,ballwidth,lenpaddles,bally,ballydir,ypospaddlea,ypospaddleb

    ballx += ballxdir
    bally += ballydir

    if bally < 0 or bally > (height - (ballheight + 1)):
        ballydir *= -1

    if ballx == 2 + paddlewidth and bally < ypospaddlea - 2 +lenpaddles and bally > ypospaddlea - 3:
        ballxdir *= -1

    elif ballx == lenght - paddlewidth and bally < ypospaddleb - 2 + lenpaddles and bally > ypospaddleb -3:
        ballxdir *= -1


def CheckTimer():
    global timer,Intervall
    if timer == Intervall:
        MoveBall()
        timer = 0

def ResetBall():
    global ballx,bally,ballxdir,ballydir

    RandomDir()
    printscreen()
    sleep(2)

timer = 0

running = True
while running:
    if ballx < 1:
        points_b += 1
        ResetBall()

    if ballx > lenght - 1:
        points_a += 1
        ResetBall()

    timer += 1
    CheckTimer()

    sleep(0.0001)

    printscreen()
    listenkeyboard()

# By Alex / Sturm2002 
# 3th April 2020
# 23:41
# 234 Lines
# Version 1.0 
