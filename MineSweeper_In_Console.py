import colorama, os
from time import sleep
from random import randint as random
import keyboard


size = 10
mines = 20 #mine chance per field in %



actualMines = 0
Lost = False
LastMove = ()
field = []
Curs = [0,0]
RetVal = True

class fieldObj():
    def __init__(self,metype,poscol,posrow):
        self.type = metype
        self.val = 0
        self.marked = False
        self.col = poscol
        self.row = posrow
        self.disc = False

        self.RelativeCheckFields = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        self.RelativeCheckFields2 = [[-1,0],[0,-1],[0,1],[1,0]]

    def GetVal(self):
        global field,size
        NearMines = 0
        if self.type == "mine":
            pass
        else:
            for checkfield in self.RelativeCheckFields:
                if self.col + checkfield[0] < 0 or self.col + checkfield[0] >= size or self.row+checkfield[1] < 0 or self.row+checkfield[1] >= size:
                    continue
                elif field[self.col + checkfield[0]][self.row+checkfield[1]].type == "mine":
                    NearMines += 1
                
        if self.type == "mine":
            self.val = "\u00F8"
        else:
            self.val = NearMines
    
    def Undiscover(self,selected):
        if self.disc == False:
            self.disc = True
            if self.type == "mine" and selected == True:
                return False
                
            else:
                
                for checkfield in self.RelativeCheckFields2:
                    if self.col + checkfield[0] < 0 or self.col + checkfield[0] >= size or self.row+checkfield[1] < 0 or self.row+checkfield[1] >= size:
                        pass
                    elif field[self.col + checkfield[0]][self.row+checkfield[1]].type != "mine" and field[self.col + checkfield[0]][self.row+checkfield[1]].val <= 1 :
                        field[self.col + checkfield[0]][self.row+checkfield[1]].Undiscover(False)
                
                return True
            




def CreateField(size):
    global field,mines,actualMines
    field = []
    actualMines = 0
    shortyArr = []
    for j in range(size):
        for i in range(size):
            if random(0,100) <= mines:
                obj = fieldObj("mine",j,i)
                actualMines += 1
            else:
                obj = fieldObj("",j,i)
            shortyArr.append(obj)

        field.append(shortyArr)
        shortyArr = []
    if actualMines == 0:
        CreateField(size)
    
def KeyUP():
    global Curs,size
    if Curs[0] > 0:
        Curs[0] -= 1

def KeyDOWN():
    global Curs,size
    if Curs[0] < size -1:
        Curs[0] += 1

def KeyLEFT():
    global Curs,size
    if Curs[1] > 0:
        Curs[1] -= 1

def KeyRIGHT():
    global Curs,size
    if Curs[1] < size -1:
        Curs[1] += 1

def KeyUndiscover():
    global Curs,RetVal
    RetVal = field[Curs[0]][Curs[1]].Undiscover(True)

def KeyMark():
    global Curs,field
    if field[Curs[0]][Curs[1]].marked == False:
        field[Curs[0]][Curs[1]].marked = True
    else:
        field[Curs[0]][Curs[1]].marked = False

def SetValues():
    global field
    for i in field:
        for j in i:
            j.GetVal()

def newMain():
    global field,Lost,LastMove,RetVal,size,Curs
    running = True
    Lost = False
    LastMove = []
    RetVal = True
    Curs = [int(size/2),int(size/2)]
    while running:
        PrintField()
        if Lost != True:
            
            LastMove = (Curs[1],Curs[0])

            keyboard.read_key()

            
            if RetVal == False:
                Lost = True
        else:
            PrintField()
            
            print("You Lost!")
            input("")
            running = False

def initGame():
    global size
    while True:
        CreateField(size)
        SetValues()
        newMain()

def main():
    global field,Lost,LastMove
    running = True
    Lost = False
    while running:
        PrintField()
        if Lost != True:
            print("Column: ",end="")
            usrCol = int(input(""))
            print("Row: ",end="")
            usrRow = int(input(""))
            LastMove = (usrRow-1,usrCol-1)

            RetVal = field[usrRow-1][usrCol-1].Undiscover(True)
            if RetVal == False:
                Lost = True
        else:
            PrintField()
            
            print("You Lost!")
            input("")


prtStr = ""
def AddPrint(PrintNow,val):
    global prtStr
    if PrintNow == False:
        prtStr += val
    else:
        print(prtStr)
        prtStr = ""

def PrintField():
    global field,Lost,LastMove,Curs,actualMines
    AddPrint(False,"Total Mines: " + str(actualMines))
    for rowarr in field:
        AddPrint(False, colorama.Fore.WHITE + "\n"+(size*2+1)*"\u2501"+"\n\u2503")
        for val in rowarr:
            if val.col == Curs[0] and val.row == Curs[1]:
                if val.disc == True:
                    if Lost == False:
                        AddPrint(False,colorama.Fore.MAGENTA + str(val.val) + colorama.Fore.WHITE + "\u2503")
                    else: 
                        AddPrint(False,colorama.Fore.RED + str(val.val) + colorama.Fore.WHITE + "\u2503")
                else:
                    AddPrint(False,colorama.Fore.MAGENTA + "#" + colorama.Fore.WHITE + "\u2503")
            elif val.disc == True and Lost != True:
                if val.type == "mine":
                    AddPrint(False,colorama.Fore.RED + str(val.val) + colorama.Fore.WHITE + "\u2503")
                elif val.val == 0:
                    AddPrint(False,colorama.Fore.LIGHTGREEN_EX + str(val.val) + colorama.Fore.WHITE + "\u2503")
                elif val.val == 1:
                    AddPrint(False,colorama.Fore.LIGHTYELLOW_EX + str(val.val) + colorama.Fore.WHITE + "\u2503")
                elif val.val == 2:
                    AddPrint(False,colorama.Fore.LIGHTYELLOW_EX + str(val.val) + colorama.Fore.WHITE + "\u2503")
                elif val.val == 3:
                    AddPrint(False,colorama.Fore.YELLOW + str(val.val) + colorama.Fore.WHITE + "\u2503")
                elif val.val == 4:
                    AddPrint(False,colorama.Fore.YELLOW + str(val.val) + colorama.Fore.WHITE + "\u2503")
                elif val.val == 5:
                    AddPrint(False,colorama.Fore.LIGHTRED_EX + str(val.val) + colorama.Fore.WHITE + "\u2503")
                elif val.val == 6:
                    AddPrint(False,colorama.Fore.LIGHTRED_EX + str(val.val) + colorama.Fore.WHITE + "\u2503")
                elif val.val == 7:
                    AddPrint(False,colorama.Fore.LIGHTRED_EX + str(val.val) + colorama.Fore.WHITE + "\u2503")
                elif val.val == 8:
                    AddPrint(False,colorama.Fore.LIGHTRED_EX + str(val.val) + colorama.Fore.WHITE + "\u2503")
                else:
                    AddPrint(False,colorama.Fore.WHITE + str(val.val) + colorama.Fore.WHITE + "\u2503")
                colorama.Fore.WHITE
            elif Lost != True and val.disc == False:
                if val.marked == True:
                    AddPrint(False,colorama.Fore.RED + "?" + colorama.Fore.WHITE + "\u2503")
                else:
                    AddPrint(False,colorama.Fore.WHITE + "#" + colorama.Fore.WHITE + "\u2503")
            else:
                if val.row == LastMove[0] and val.col == LastMove[1]:
                    AddPrint(False,colorama.Fore.RED + str(val.val) + colorama.Fore.WHITE + "\u2503")
                else:
                    AddPrint(False,str(val.val) + "\u2503")

                
    AddPrint(False, colorama.Fore.WHITE + "\n" + (size*2+1)*"\u2501")
    os.system("cls")
    AddPrint(True,"")



if __name__ == "__main__":

    keyboard.add_hotkey('up',KeyUP)
    keyboard.add_hotkey('down',KeyDOWN)
    keyboard.add_hotkey('left',KeyLEFT)
    keyboard.add_hotkey('right',KeyRIGHT)
    keyboard.add_hotkey('space',KeyUndiscover)
    keyboard.add_hotkey('c',KeyMark)

    initGame()


#by Sturmy / 04.04.2022 22:00