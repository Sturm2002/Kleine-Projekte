from time import sleep
import os

T1mEstr = str("""
 _________  __                 ______   
|  _   _  |/  |               / ____ `. 
|_/ | | \_|`| |   _ .--..--.  `'  __) | 
    | |     | |  [ `.-. .-. | _  |__ '. 
   _| |_   _| |_  | | | | | || \____) | 
  |_____| |_____|[___||__||__]\______.' 
    """)

startstr = ("By Alex Bruksch")

Xpos = 0
Ypos = 0



Events = [[1,1,"Chest"]]

def clearS():
    os.system("cls")

def CheckPosForEvents(UserXpos,UserYpos):
    FoundEvent = ""
    for i in Events:
        if UserXpos == i[0] and UserYpos == i[1]:
            FoundEvent = i[2]

    CheckEvents(FoundEvent)

def WaitPress():
    kurz = input()

def CheckEvents(EvName):
    if EvName == "Chest":
        
        while True:
            clearS 
            Printtxt("You've Found a Small Chest do you want to open it?\n Yes | No\n")
            inp = str(input())
            if inp == "Yes":
                for i in User.Inventory:
                    if i == "Key":
                        User.Inventory.remove("Key")
                        Printtxt("You Used Your Key")
                        WaitPress()
                        return

                Printtxt("You Don't Have a Key to open the chest!")
                WaitPress()
                return

            if inp == "No":
                Printtxt("You're ignoring the Chest")
                WaitPress()
                return


clearS()
def Start():
    print(T1mEstr)
    print("     ",end="")
    Printtxt(startstr,0.15)
    sleep(2)
    clearS()

    #User.Inventory.append("Key")


def Printtxt(inp,speed = 0.05):
    for i in inp:
        sleep(speed)
        print(i, end="")

class Player():
    def __init__(self,HealthInp, XposInp,YposInp):
        self.Health = HealthInp
        self.Inventory = []
        self.Xpos = XposInp
        self.Ypos = YposInp
    
    def Move(self,direc):
        if direc == "Up":
            self.Ypos += 1
        elif direc == "Right":
            self.Xpos += 1
        elif direc == "Down":
            self.Ypos -= 1
        elif direc == "Left":
            self.Xpos -= 1

        elif direc == "Key":
            self.Inventory.append("Key")
        else:
            pass
User = Player(100,0,0)

Start()
#Printtxt("Vor langer zeit gab es einmal\neinen guten test um diese function zu probieren!\n\n")


running = True
while running: 
    clearS()
    Printtxt(str(User.Inventory) +"\nWolang willst du ? " + str(User.Xpos)+ " | " + str(User.Ypos) +"\n")
    User.Move(str(input()))
    CheckPosForEvents(User.Xpos,User.Ypos)