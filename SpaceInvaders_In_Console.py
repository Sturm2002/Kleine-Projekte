from time import sleep
import os
import keyboard
import random

PlayField_Height = 15
PlayField_Lenght = 30

CurrentRound = 1

Output_String = str("""""")
Enemys = []
Bullets = []

def FieldToString():
    global Output_String,Bullets,Enemys

    
    for y in range(1,PlayField_Height+1):
        if y == 1 or y == PlayField_Height:
            Output_String += PlayField_Lenght * "#"
            Output_String += "\n"

        else:
            for x in range(1,PlayField_Lenght+1):
                    

                    if x == 1 :
                        Output_String += "#"

                    elif x == PlayField_Lenght:
                        Output_String += "#\n"

                    else:

                        if (User.Xpos == x and User.Ypos == y) or (User.Xpos +1 == x and User.Ypos == y) or (User.Xpos -1  == x and User.Ypos == y) or (User.Xpos == x and User.Ypos - 1 == y):
                            Output_String += "Ä"
                        else:

                            for E1 in Enemys:
                                
                                if (x == E1.Xpos and y == E1.Ypos) or (x -1 == E1.Xpos and y == E1.Ypos) or (x + 1 == E1.Xpos and y == E1.Ypos) or (x == E1.Xpos and y -1 == E1.Ypos) :
                                    
                                    for BulletI in Bullets:
                                        if (BulletI.Xpos == x and BulletI.Ypos == y):
                                            Output_String += "X"
                                            
                                            E1.Goto(100,100)
                                            BulletI.Goto(100,100)
                                            Enemys.pop(Enemys.index(E1))
                                            Bullets.pop(Bullets.index(BulletI))
                                            
                                            del BulletI
                                            del E1


                                            break
                                    else:
                                        Output_String += "$"
                                        break
                                    break
                            else:
                                for BulletI in Bullets:
                                    if (BulletI.Xpos == x and BulletI.Ypos == y):
                                        Output_String += "I"
                                        break
                                else:
                                    Output_String += " "
    Output_String += """Move with <- / -> \nShoot with Space """

pressed = False
AllowShoot = True

tick = 0
tickBull = 0
tickshoot = 0

def SetPressedFalse():
    global pressed
    pressed = False

def ListenKeyboard():
    global pressed,tickshoot,AllowShoot
    if keyboard.is_pressed("left"):
        User.MoveLeft()

    elif keyboard.is_pressed("right"):
        User.MoveRight()

    if AllowShoot == True:
        if keyboard.is_pressed("space"):
            User.Shoot()
            tickshoot = 0
            AllowShoot = False
            return

class Bullet():
    def __init__(self,StartPosX,StartPosY):
        self.Xpos = StartPosX
        self.Ypos = StartPosY
        self.Living = True

    def MoveUp(self):
        self.Ypos -= 1

    def Goto(self,NewX, NewY):
        self.Xpos = NewX
        self.Ypos = NewY

class Enemy():

    def __init__(self,StartPosX,StartPosY):
        self.Ypos = StartPosY
        self.Xpos = StartPosX
        self.Living = True

    def Goto(self,NewXpos, NewYpos):
        self.Ypos = NewYpos
        self.Xpos = NewXpos

class Player():
    def __init__(self,StartPosX,StartPosY):
        self.Xpos = StartPosX
        self.Ypos = StartPosY

    def MoveLeft(self):
        if self.Xpos >3:
            self.Xpos -= 1

    def MoveRight(self):
        if self.Xpos < PlayField_Lenght -2:
            self.Xpos += 1

    def Shoot(self):
        bull = Bullet(self.Xpos,self.Ypos)
        Bullets.append(bull)

def Clear():
    global Output_String
    Output_String = """"""
    os.system("cls")

def CheckTick():
    global tick,tickBull,tickshoot,AllowShoot
    tick += 1
    tickBull += 1
    tickshoot += 1
    if tick >= 20:
        for i in Enemys:
            i.Goto(i.Xpos,i.Ypos +1)
        tick = 0
        return
    if tickBull >= 10:
        for i in Bullets:
            i.MoveUp()
        tickBull = 0
        return

    if tickshoot >= 20:
        AllowShoot = True

    else:
        AllowShoot = False

def CheckCollision():
    for En in Enemys:
        for Bull in Bullets:
            if En.Xpos -1 >= Bull.Xpos and En.Xpos +1 <= Bull.Xpos and En.Ypos == Bull.Ypos:
                En.Living = False
                del En
                
                del Bull
        if En.Xpos >= 30 or En.Ypos >= 30:
            En.Living = False
            del En

def NextRound():
    global Output_String,Enemys,Bullets
    Bullets.clear()
    Enemys.clear()
    NoCol = True

    Output_String = """
    _   _  _______   _______  ______ _____ _   _ _   _______ 
    | \ | ||  ___\ \ / /_   _| | ___ \  _  | | | | \ | |  _ |
    |  \| || |__  \ V /  | |   | |_/ / | | | | | |  \| | | | |
    | . ` ||  __| /   \  | |   |    /| | | | | | | . ` | | | |
    | |\  || |___/ /^\ \ | |   | |\ \ \_/ / |_| | |\  | |/ /  
    \_| \_/\____/\/   \/ \_/   \_| \_|\___/ \___/\_| \_/___/                                           
        """
    for i in range(3):
        print(Output_String)
        sleep(0.3)
        os.system("cls")

    for i in range(CurrentRound +3):
        Randx = random.randint(3,PlayField_Lenght-3)
        Randy = random.randint(-6,2)
        
        while NoCol == True:  
            if len(Enemys) >= 1:
                for En in Enemys:
                    if (Randx >= En.Xpos -1 and Randx <= En.Xpos +1) and (Randy == En.Ypos or Randy == En.Ypos + 1 or Randy == En.Ypos -1):
                        NoCol = True
                        Randx = random.randint(3,PlayField_Lenght-3)
                        Randy = random.randint(-6,2)    
                    else:
                        NoCol = False
            else:
                NoCol = False
                    
        En = Enemy(Randx,Randy)
        Enemys.append(En)
        
        

def CheckAlive():
    global Enemys,Bullets
    AmountLivingEn = 0
    AmountLivingBull = 0
    for En in Enemys:
        if En.Living == True:
            AmountLivingEn += 1
    for Bull in Bullets:
        if Bull.Living == True:
            AmountLivingBull += 1
    return AmountLivingEn,AmountLivingBull
    
for i in range(3):
    En = Enemy(random.randint(3,PlayField_Lenght),random.randint(-6,2))
    Enemys.append(En)

User = Player(PlayField_Lenght/2,PlayField_Height - 2)

running = True
while running:
    if CheckAlive()[0] > 0:
        ListenKeyboard()
        CheckTick()
        CheckCollision()
        FieldToString()
        print(Output_String)
        sleep(0.01)
        Clear()
    else:
        NextRound()