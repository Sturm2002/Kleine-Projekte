from time import sleep
import os
import keyboard
import random

PlayField_Height = 30
PlayField_Lenght = 60

CurrentRound = 1

Output_String = str("""""")
Enemys = []
Bullets = []
PowerUps = []

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
                                            RandPowerUp(x,y)

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
                                        Output_String += "!"
                                        break
                                else:
                                    for Pu in PowerUps:
                                        if Pu.Xpos == x and Pu.Ypos == y:
                                            if Pu.Type == "SB":
                                                Output_String += "I"
                                                break   
                                            elif Pu.Type == "SLE":
                                                Output_String += "S"
                                                break
                                            elif Pu.Type == "SS":
                                                Output_String += "§"
                                                break
                                            elif Pu.Type == "SBS":
                                                Output_String += "V"
                                                break
                                            elif Pu.Type == "Ultra":
                                                Output_String += "+"
                                                break
                                    else:
                                        Output_String += " "




    Output_String += """Move with <- / -> \nShoot with Space """

pressed = False
AllowShoot = True

IntervallEnemyMove = 20
MultEnemyMove = 1

IntervallShootSpeed = 10
MultShootSpeed = 1

IntervallBullSpeed = 10
MultBullSpeed = 1

tick = 0
tickBull = 0
tickshoot = 0
tickPu = 0

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
        if self.Ypos <= 0:
            del self

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

    def CheckHome(self):
        global Enemys
        for En in Enemys:
            if En.Ypos >= PlayField_Height -2:
                return False
        else:
            return True

class PowerUp():
    
    def __init__(self,InpShootSpeed=1, InpEnemySpeed=1, InpBullSpeed=1,StartX=100,StartY=100,Type="None"):
        
        self.Xpos = StartX
        self.Ypos = StartY

        self.Tick = 0
        self.Used = False
        self.EffectDuration = 300
        
        self.SMultShootSpeed = InpShootSpeed
        self.SEnemySpeed = InpEnemySpeed
        self.SBulletSpeed = InpBullSpeed

        self.Type = Type

    def Use(self):
        global IntervallBullSpeed,IntervallEnemyMove,IntervallShootSpeed,MultBullSpeed,MultEnemyMove,MultShootSpeed

        MultShootSpeed = self.SMultShootSpeed
        MultEnemyMove = self.SEnemySpeed
        MultBullSpeed = self.SBulletSpeed
        self.Used = True

        self.Xpos = 100
        self.Ypos = 100

    def Goto(self,PosX,PosY):
        self.Xpos = PosX
        self.Ypos = PosY
        if self.Ypos >= PlayField_Height:
            del self

    def CheckUsed(self):
        global MultBullSpeed,MultEnemyMove,MultShootSpeed
        if self.Used == True:
            if self.Tick >= self.EffectDuration:
                self.Used = False
                self.Tick = 0
                MultBullSpeed = 1
                MultEnemyMove = 1
                MultShootSpeed = 1
                del self

            else:
                MultShootSpeed = self.SMultShootSpeed
                MultEnemyMove = self.SEnemySpeed
                MultBullSpeed = self.SBulletSpeed

def RandPowerUp(StartPosX,StartPosY):
    PURand = random.randint(0,4)
    ChancePU = random.randint(0,4)
    if ChancePU == 4:
        if PURand == 0:
            NewPU = PowerUp(1,1,0.2,StartPosX,StartPosY,"SB")
        elif PURand == 1:
            NewPU = PowerUp(1,1.5,1,StartPosX,StartPosY,"SLE")
        elif PURand == 2:
            NewPU = PowerUp(0.2,1.5,1,StartPosX,StartPosY,"SS")
        elif PURand == 3:
            NewPU = PowerUp(0.2,1,0.2,StartPosX,StartPosY,"SBS")
        elif PURand == 4:
            NewPU = PowerUp(0.2,1.5,0.2,StartPosX,StartPosY,"Ultra")
        PowerUps.append(NewPU)
    else:
        return

def Clear():
    global Output_String
    Output_String = """"""
    os.system("cls")

def CheckTick():
    global tick,tickBull,tickshoot,tickPu,AllowShoot,MultBullSpeed,MultEnemyMove,MultShootSpeed
    tick += 1
    tickBull += 1
    tickshoot += 1
    tickPu += 1

    for Pu in PowerUps:
        Pu.CheckUsed()

    if tick >= IntervallEnemyMove * MultEnemyMove:
        for i in Enemys:
            i.Goto(i.Xpos,i.Ypos +1)
        tick = 0
        return
    if tickBull >= IntervallBullSpeed * MultBullSpeed:
        for i in Bullets:
            i.MoveUp()
        tickBull = 0
        return

    if tickshoot >= IntervallShootSpeed * MultShootSpeed:
        AllowShoot = True

    else:
        AllowShoot = False

    if tickPu >= 5:
        for Pu in PowerUps:
            Pu.Goto(Pu.Xpos,Pu.Ypos+1)
        tickPu = 0
        return

def CheckCollision():
    for En in Enemys:
        for Bull in Bullets:
            if En.Xpos -1 >= Bull.Xpos and En.Xpos +1 <= Bull.Xpos and En.Ypos == Bull.Ypos:
                En.Living = False
                RandPowerUp(En.Xpos,En.Ypos)
                del En
                del Bull

        if En.Xpos >= 30 or En.Ypos >= 30:
            En.Living = False
            del En
    for Pu in PowerUps:
        if Pu.Xpos <= User.Xpos +1 and Pu.Xpos >= User.Xpos -1 and Pu.Ypos == User.Ypos or Pu.Ypos == User.Ypos +1:
            Pu.Use()

def NextRound():
    global Output_String,Enemys,Bullets,MultBullSpeed,MultEnemyMove,MultShootSpeed,PlayField_Lenght
    Bullets.clear()
    Enemys.clear()
    PowerUps.clear()
    User.Xpos = PlayField_Lenght / 2
    MultBullSpeed = 1
    MultEnemyMove = 1
    MultShootSpeed = 1
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
        sleep(0.3)

    for i in range(CurrentRound +int(PlayField_Lenght/10) + int(PlayField_Height/10)):
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
        
def Lost():
    global Bullets,Enemys
    LostString = """
                            .-')    .-') _   ,---. 
                           ( OO ). (  OO) )  |   | 
    ,--.      .-'),-----. (_)---\_)/     '._ |   | 
    |  |.-') ( OO'  .-.  '/    _ | |'--...__)|   | 
    |  | OO )/   |  | |  |\  :` `. '--.  .--'|   | 
    |  |`-' |\_) |  |\|  | '..`''.)   |  |   |  .' 
   (|  '---.'  \ |  | |  |.-._)   \   |  |   `--'  
    |      |    `'  '-'  '\       /   |  |   .--.  
    `------'      `-----'  `-----'    `--'   '--'  """
    print(LostString)
    answer = False
    while answer != True:
        print("Restart Game?\n Yes | No\n")
        rest = input()
        if rest == "Yes":
            answer = True
            Bullets.clear()
            Enemys.clear()
            PowerUps.clear()
            Main()
            
            return
        elif rest == "No":
            answer = True
            exit
        os.system("cls")

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


User = Player(PlayField_Lenght/2,PlayField_Height - 2)

def Main():
    global Enemys,Bullets

    for i in range(3):
        En = Enemy(random.randint(3,PlayField_Lenght),random.randint(-6,2))
        Enemys.append(En)
        
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
            if User.CheckHome() == False:
                running = False
                
        else:
            NextRound()
    Lost()

Main() 