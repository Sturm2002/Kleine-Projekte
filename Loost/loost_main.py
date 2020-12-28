"""
->->->-Main Module for the Game Loost-<-<-<-


I'm gonna be Probably the only one who will

use this but hey, if you have no life

have fun, but i wont fucking write

a whole fucking Documentation

that's not my fucking job

Love
Sturmy

Sucker




>#>#>ToDo<#<#<

2/10 - More Enemys
1/10 - Death ?
6/10 - XP / lvl System
4/10 - Cheating Items
7/10 - Intense Enemy Fights
8/10 - Walls
9/10 - Story ?
8/10 - Bosses
8/10 - Trading / Coins
8/10 - Dungeons
10/10 - Multiplayer

<<<<Changelog>>>>
V0.1 / 10.12.2020
-Started this Changelog

V0.2 / 11.12.2020
-Minimap
-Rarity Grades for Items

V0.3 / 12.12.2020
-Random Map Generation

V0.4 / 15.12.2020
-Help Menu
-Show Items after Open Chest
-Item Draw after Rarity
-Duration Potions Work

V0.5 / 22.12.2020
-Multiple Objects on 1 Field
-Options Menu
-Changed Fight System x2
-New Map System (Buggy)

V0.6 / 23.12.2020
-Fixed New Map System
-Cheats

V0.7 / 26.12.2020
-Saving / Loading
-Fixed some Bugs

V0.8 / 28.12.2020
-Optimized the Map System
-Better Map Gen
-New "Undiscovered Fields"
-Splitted the File in 3 Parts
-Added a Main Menu

"""

from time import sleep
from os import system
from random import randint
from sturmysprint import printstr,InitPerfMode
import colorama
import json
import pathlib


StartString = colorama.Fore.WHITE+"""
    ██▓     ▒█████   ▒█████    ██████ ▄▄▄█████▓
    ▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒
    ▒██░    ▒██░  ██▒▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░
    ▒██░    ▒██   ██░▒██   ██░  ▒   ██▒░ """+colorama.Fore.RED+ """▓██▓ ░
    ░██████▒░ ████▓▒░░ ████▓▒░▒██████▒▒  ▒██▒ ░
    ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░
    ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒  ░ ░    ░
    ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░  ░  ░    ░
        ░  ░    ░ ░      ░ ░        ░\n
    """ +colorama.Fore.CYAN+ "By Sturm2002\n" + colorama.Fore.WHITE

LoostHelp = """
    <<<Help>>>

    """+colorama.Fore.WHITE+"""Command   |  Synonyms   | Description"""+colorama.Fore.LIGHTBLACK_EX+"""
    Help      | H,?         | Shows This screen
    Move      | mv          | Allows to Move
    Attack    | atk,atack   | As the Name Says
    Use Item  | ui,useitem  | Allows to Use an Item
    Inventory | inv         | Shows the Inventory
    Show Map  | sm,map      | Shows the map
    Statistics| stats,stat  | Shows your Statistics
    Save      | sv          | Saves the Game
    Load      | load        | Loads a Game
    Options   | opt,option  | Shows the Options
    CheatMenu | cm,cheat    | Opens the Cheat Menu

    """

PlayField = [
    [[],[],[],[],[]],
    [["ch"],["ch"],["ch","ch"],["ch"],["ch"]],
    [[],[],[],["z","z"],[]],
    [["z"],["z"],["z","z"],[],[]],
    [[],[],[],[],[]]
    ]

EnemysArr = []

ChestsArr = []

EventArr = []

InputOpt = [
    [["Move","Mv","MV","mv","move"],
        ["Up",["up","Up","uP","UP","u","U"]],
        ["Right",["Right","right","rIGHT","R","r"]],
        ["Down",["Down","down","d","D"]],
        ["Left",["Left","left","l","L"]],],
    [["Attack","Atk","attack","atack","Atack","atk"],   ],
    [["OpenChest","Open Chest","Open chest","openchest","open chest","oc","OC","Oc","oC"],],
    [["Inventory","Inv","inv","Inventory","Showinventory","showinventory","show inventory","Show Inventory","show inv","Show Inv"]],
    [["Use Item","useitem","UseItem","ui","Ui","uI","UI"]],
    [["Help","help","h","H","?"]],
    [["Stats","stat","Stat","stats","Statistics","statistics"]],
    [["Options","options","option","Option","opt","Opt"]],
    [["Show Map","show map","show Map","ShowMap","Sm","SM","sm","sM"]],
    [["Cheat Menu","cheatmenu","cheat menu","cheats","cheat","cm","Cm","CM"]],
    [["exit","Exit"]],
    [["save","Save","Save Game","save game","sg","SG","sG","Sg"]]
        ]

Items = [
    ["Swords",[# Name[0],Cat.[1],DmgMult[2],PenMult[3],Rarity[4]
        [colorama.Fore.WHITE+"Wooden Sword"+colorama.Fore.WHITE,"Swrd",0.1,0.1,1],
        [colorama.Fore.WHITE+"Stone Sword"+colorama.Fore.WHITE,"Swrd",0.3,0.3,1],
        [colorama.Fore.WHITE+"Cooper Sword"+colorama.Fore.WHITE,"Swrd",0.4,0.4,1],
        [colorama.Fore.LIGHTGREEN_EX+"Iron Sword"+colorama.Fore.WHITE,"Swrd",0.5,0.5,2],
        [colorama.Fore.LIGHTGREEN_EX+"Silver Sword"+colorama.Fore.WHITE,"Swrd",0.7,0.7,2],
        [colorama.Fore.CYAN+"Titanium Sword"+colorama.Fore.WHITE,"Swrd",1,1,3],
        [colorama.Fore.MAGENTA+"Demonic Sword"+colorama.Fore.WHITE,"Swrd",1.5,1.5,4],
        [colorama.Fore.LIGHTRED_EX+"Excalibur"+colorama.Fore.WHITE,"Swrd",2,2,5]
        ]],
    ["Shields",[# Name[0],Cat.[1],DefMult[2],Rarity[3]
        [colorama.Fore.WHITE+"Wooden Shield"+colorama.Fore.WHITE,"Shld",0.05,1],
        [colorama.Fore.LIGHTGREEN_EX+"Reinforced Wooden Shield"+colorama.Fore.WHITE,"Shld",0.1,2],
        [colorama.Fore.CYAN+"Iron Shield"+colorama.Fore.WHITE,"Shld",0.15,3],
        [colorama.Fore.MAGENTA+"Reinforced Iron Shield"+colorama.Fore.WHITE,"Shld",0.2,4],
        [colorama.Fore.LIGHTRED_EX+"Shield Of the Black Night"+colorama.Fore.WHITE,"Shld",0.5,5]
        ]],
    ["Potions",[# Name[0],Cat.[1],PotnType[2],Effect[3],Length[4],Rarity[5]
        [colorama.Fore.WHITE+"Small Health Potion"+colorama.Fore.WHITE,"Potn","Health",20,0,1],
        [colorama.Fore.LIGHTGREEN_EX+"Medium Health Potion"+colorama.Fore.WHITE,"Potn","Health",50,0,2],
        [colorama.Fore.CYAN+"Big Health Potion"+colorama.Fore.WHITE,"Potn","Health",100,0,3],
        [colorama.Fore.WHITE+"Weak Regeneration Potion"+colorama.Fore.WHITE,"Potn","Regen",10,3,1],
        [colorama.Fore.CYAN+"Strong Regeneration Potion"+colorama.Fore.WHITE,"Potn","Regen",25,3,3],
        [colorama.Fore.CYAN+"Toughness Potion"+colorama.Fore.WHITE,"Potn","ArmorPen",0.2,5,3]
        ]],
    ["Misc",[# Name[0],Cat.[1],Type[2],Rarity[3],Res.Value1[4],Res.Value2[5]
        [colorama.Fore.MAGENTA + "Better Flashlight"+colorama.Fore.WHITE,"Misc","Flashlight",4,1]
    ]]
    ]

SaveName = "07Save.json"
MapGenValueMin = 0
MapGenValueMax = 3
GameEnd = False

class Player():
    def __init__(self,StartPosX=0,StartPosY=0,Health=100,StandDmg=10,StandDefense=20,ArmorPen=1):
        self.Xpos = StartPosX
        self.Ypos = StartPosY
        self.MaxHealth = 100
        self.Health = Health
        self.AmountKeys = 4
        self.StandDmg = StandDmg
        self.StandDefense = StandDefense
        self.DefenseMultShield = 1
        self.DefenseMultPotion = 1
        self.DmgMultiplier = 1
        self.MapRange = 2
        self.ArmorPenMult = 1
        self.StandArmorPen = ArmorPen
        self.PotionEffects = []
        #self.Inventory = []
        self.GenedFields = []

        self.Inventory = [[colorama.Fore.WHITE+"Wooden Sword"+colorama.Fore.WHITE,"Swrd",0.1,0.1,1],
        [colorama.Fore.WHITE+"Stone Sword"+colorama.Fore.WHITE,"Swrd",0.3,0.3,1],
        [colorama.Fore.WHITE+"Cooper Sword"+colorama.Fore.WHITE,"Swrd",0.4,0.4,1],
        [colorama.Fore.LIGHTGREEN_EX+"Iron Sword"+colorama.Fore.WHITE,"Swrd",0.5,0.5,2],
        [colorama.Fore.LIGHTGREEN_EX+"Silver Sword"+colorama.Fore.WHITE,"Swrd",0.7,0.7,2],
        [colorama.Fore.CYAN+"Titanium Sword"+colorama.Fore.WHITE,"Swrd",1,1,3],
        [colorama.Fore.MAGENTA+"Demonic Sword"+colorama.Fore.WHITE,"Swrd",1.5,1.5,4],
        [colorama.Fore.LIGHTRED_EX+"Excalibur"+colorama.Fore.WHITE,"Swrd",2,2,5],
        [colorama.Fore.WHITE+"Wooden Shield"+colorama.Fore.WHITE,"Shld",0.05,1],
        [colorama.Fore.LIGHTGREEN_EX+"Reinforced Wooden Shield"+colorama.Fore.WHITE,"Shld",0.1,2],
        [colorama.Fore.CYAN+"Iron Shield"+colorama.Fore.WHITE,"Shld",0.15,3],
        [colorama.Fore.MAGENTA+"Reinforced Iron Shield"+colorama.Fore.WHITE,"Shld",0.2,4],
        [colorama.Fore.LIGHTRED_EX+"Shield Of the Black Night"+colorama.Fore.WHITE,"Shld",0.5,5],
        [colorama.Fore.WHITE+"Small Health Potion"+colorama.Fore.WHITE,"Potn","Health",20,0,1],
        [colorama.Fore.LIGHTGREEN_EX+"Medium Health Potion"+colorama.Fore.WHITE,"Potn","Health",50,0,2],
        [colorama.Fore.CYAN+"Big Health Potion"+colorama.Fore.WHITE,"Potn","Health",100,0,3],
        [colorama.Fore.WHITE+"Weak Regeneration Potion"+colorama.Fore.WHITE,"Potn","Regen",10,3,1],
        [colorama.Fore.CYAN+"Strong Regeneration Potion"+colorama.Fore.WHITE,"Potn","Regen",25,3,3],
        [colorama.Fore.CYAN+"Toughness Potion"+colorama.Fore.WHITE,"Potn","ArmorPen",0.2,5,3],
        [colorama.Fore.MAGENTA + "Better Flashlight"+colorama.Fore.WHITE,"Misc","Flashlight",4,1]]

        self.StatKilledEnemys = 0
        self.StatAttacks = 0
        self.StatDmgDealt = 0
        self.StatOpenedChests = 0
        self.StatFoundItems = 0
        self.StatDmgGot = 0
        self.StatPotionsDrank = 0
        self.StatMovesDone = 0
        self.StatUsedItems = 0

        self.OptPerfMode = True
        self.OptCheatMode = False

    def Goto(self,NewXpos,NewYPos):
        self.Xpos = NewXpos
        self.Ypos = NewYPos

    def Move(self,Dir="Right"):
        ClearCons()
        CheckEnemys()
        #ClearCons()
        if CheckInpInArr(Dir,0,1,1):
            self.Ypos += 1
            #GenMap("u",randint(MapGenValueMin,MapGenValueMax))
            self.GenedFields.append([self.Xpos,self.Ypos])
            

        elif CheckInpInArr(Dir,0,2,1):
            self.Xpos += 1
            #GenMap("r",randint(MapGenValueMin,MapGenValueMax))
            self.GenedFields.append([self.Xpos,self.Ypos])

        elif CheckInpInArr(Dir,0,3,1):
            self.Ypos -= 1
            #GenMap("d",randint(MapGenValueMin,MapGenValueMax))
            self.GenedFields.append([self.Xpos,self.Ypos])

        elif CheckInpInArr(Dir,0,4,1):
            self.Xpos -= 1
            #GenMap("l",randint(MapGenValueMin,MapGenValueMax))
            self.GenedFields.append([self.Xpos,self.Ypos])


        else:
            print("Faulty Input!")

    def GetDamage(self,Dmg,ArmorPen):
       
        DmgGot = int((Dmg-((self.StandDefense * self.DefenseMultShield*self.DefenseMultPotion)-ArmorPen)))
        if DmgGot <= 0 or DmgGot == None:
            DmgGot = 0
        self.Health -= DmgGot
        self.StatDmgGot += DmgGot

        return DmgGot
        
    def GetStatus(self):
        Outstring = ""
        global EnemysArr,ChestsArr
        for i in EnemysArr:
            if self.Ypos == i.Ypos and self.Xpos == i.Xpos and i.alive == True:
                Outstring += "There's an "+ i.Name + " in your Area!\n"
        for i in ChestsArr:
            if self.Ypos == i.Ypos and self.Xpos == i.Xpos and i.empty == False:
                Outstring += "There's an "+colorama.Fore.YELLOW +"Chest"+colorama.Fore.WHITE + " in your Area!\n"
            if self.Ypos == i.Ypos and self.Xpos == i.Xpos and i.empty == True:
                Outstring += "There's an "+colorama.Fore.RED+"empty " +colorama.Fore.YELLOW +"Chest"+colorama.Fore.WHITE + " in your Area!\n"
        if Outstring != "":
            Outstring += "\n"
        return Outstring

    def Attack(self):
        global EnemysArr
        ClearCons()
        AmountEnemys = 0

        for enem in EnemysArr:
            if self.Ypos == enem.Ypos and self.Xpos == enem.Xpos and enem.alive == True:
                AmountEnemys += 1
        if not AmountEnemys >= 1:
            return "There are no Enemys in your Area !"
        ClearCons()
        printstr("There are "+str(AmountEnemys)+" Enemys in your Area,\nWhich one to attack?\n")
        for enem in EnemysArr:
            if self.Ypos == enem.Ypos and self.Xpos == enem.Xpos and enem.alive == True:
                printstr(enem.Name+" | "+colorama.Fore.RED+str(enem.Health)+" HP "+colorama.Fore.LIGHTBLUE_EX+str(enem.Defense)+"Def"+colorama.Fore.WHITE+"\n")

        inp = input()
        ClearCons()
        if not inp.isnumeric or inp == "" or inp == " ":
            return "Faulty Input!\n"

        enemCounter = 0
        for enem in EnemysArr:
            if self.Ypos == enem.Ypos and self.Xpos == enem.Xpos and enem.alive == True:
                enemCounter += 1
                #for enem2 in EnemysArr:
                    #if self.Ypos == enem2.Ypos and self.Xpos == enem2.Xpos and enem2.alive == True:
                       # PlayerGotDmg = enem2.AttackPlayer()
                        #if PlayerGotDmg <= 0 or PlayerGotDmg == None:
                        #    printstr("You got " +colorama.Fore.RED+str()+"0 Dmg"+colorama.Fore.WHITE+"!\n")

                       # else:
                        #self.StatDmgGot += PlayerGotDmg
                         #   printstr("You got " +colorama.Fore.RED+str(PlayerGotDmg)+" Dmg"+colorama.Fore.WHITE+"! By "+enem2.LatestAttack+colorama.Fore.WHITE)
                CheckEnemys()
                if enemCounter == int(inp):
                
                    enem.GetAttacked()
                    self.StatAttacks += 1
                    
                    if enem.Health <= 0:
                        enem.alive = False
                        #PlayField[enem.Ypos][enem.Xpos] = ""
                        if len(enem.Inventory) <= 0 and enem.AmountKeys <= 0:
                            self.StatDmgDealt += (self.StandDmg * self.DmgMultiplier-(enem.Defense-(self.StandArmorPen*self.ArmorPenMult)))
                            self.StatKilledEnemys += 1
                            return str(enem.Name) + " Got " + str((self.StandDmg * self.DmgMultiplier-(enem.Defense-(self.StandArmorPen*self.ArmorPenMult)))) + " Dmg! And is Dead!\n"
                        elif len(enem.Inventory) > 0 and enem.AmountKeys <= 0:
                            returnStr = ""
                            for j in enem.Inventory:
                                User.Inventory.append(j)
                                User.StatFoundItems += 1
                            
                            self.StatDmgDealt += (self.StandDmg * self.DmgMultiplier-(enem.Defense-(self.StandArmorPen*self.ArmorPenMult)))
                            self.StatKilledEnemys += 1
                            returnStr += str(enem.Name) + " Got " + str((self.StandDmg * self.DmgMultiplier-(enem.Defense-(self.StandArmorPen*self.ArmorPenMult)))) + " Dmg! And is Dead!\nThe "+enem.Name+" dropped :\n"
                            for j in enem.Inventory:
                                returnStr += "- "+str(j[0]) + "\n"
                                self.StatFoundItems += 1
                            del enem
                            return returnStr
                        elif len(enem.Inventory) <= 0 and enem.AmountKeys > 0:
                            User.AmountKeys += enem.AmountKeys
                            if enem.AmountKeys == 1:
                                returnStr2 = ""                    
                                returnStr2 = str(enem.Name) + " Got " + str((self.StandDmg * self.DmgMultiplier-(enem.Defense-(self.StandArmorPen*self.ArmorPenMult)))) + " Dmg! And is Dead!\nThe "+str(enem.Name)+" dropped :\n"+ colorama.Fore.YELLOW + str(enem.AmountKeys)+colorama.Fore.WHITE +" Key"
                                self.StatDmgDealt += (self.StandDmg * self.DmgMultiplier-(enem.Defense-(self.StandArmorPen*self.ArmorPenMult)))
                                self.StatKilledEnemys += 1
                                
                                del enem
                                return returnStr2
                            else:
                                self.StatDmgDealt += (self.StandDmg * self.DmgMultiplier-(enem.Defense-(self.StandArmorPen*self.ArmorPenMult)))
                                self.StatKilledEnemys += 1
                                returnStr3 = ""                       
                                returnStr3 = str(enem.Name) + " Got " + str((self.StandDmg * self.DmgMultiplier-(enem.Defense-(self.StandArmorPen*self.ArmorPenMult)))) + " Dmg! And is Dead!\nThe "+str(enem.Name)+" dropped :\n"+ colorama.Fore.YELLOW + str(enem.AmountKeys)+colorama.Fore.WHITE +" Keys"
                                del enem
                                return returnStr3

                    else:
                        #for enem in EnemysArr:
                            #if enem.Xpos == User.Xpos and enem.Ypos == User.Ypos:
                                #printstr("You got " +colorama.Fore.RED+str(enem.AttackPlayer())+" Dmg"+colorama.Fore.WHITE+"!\n")
                        self.StatDmgDealt += (self.StandDmg * self.DmgMultiplier-(enem.Defense-(self.StandArmorPen*self.ArmorPenMult)))
                        return str(enem.Name) + " Got " + str((self.StandDmg * self.DmgMultiplier-(enem.Defense-(self.StandArmorPen*self.ArmorPenMult)))) + " Dmg! And has Now " + str(enem.Health) + " Hp\n"
                        


                if enem.alive == False:
                    self.StatKilledEnemys += 1
                    del enem
            else:
                pass       
            
        return "There are no Enemys in your Area !"
        
    def OpenChest(self):
        global ChestsArr
        ClearCons()
        CheckEnemys()
        ClearCons()
        OutString = ""
        for i in ChestsArr:
            if self.Ypos == i.Ypos and self.Xpos == i.Xpos and i.empty == False:
                if self.AmountKeys <= 0:
                    return "You Don't have a Key for That!\n"
                if self.AmountKeys > 0:
                    self.StatOpenedChests += 1
                    for j in i.Inventory: 
                        self.StatFoundItems += 1
                        self.Inventory.append(j)
                        OutString += "- "+ j[0] + "\n"
                    if len(OutString) == 0:
                        OutString += "The Chest was Empty!\n"
                    i.Inventory.clear()
                    i.empty = True
                    self.AmountKeys -= 1
                    ClearCons()
                    return OutString
        else:
            return "There is no chest nearby!\n"

    def ShowInventory(self):
        ClearCons()
        CheckEnemys()
        ClearCons()
        OutString = ""
        OutString += (">>Inventory<<\n\nKeys:  "+colorama.Fore.YELLOW+str(self.AmountKeys)+colorama.Fore.WHITE+"\n")
        for i in range(len(self.Inventory)):
            OutString += str(i)+"- "+self.Inventory[i][0] + "\n"
        return OutString

    def UseItem(self):
        CheckEnemys()
        ClearCons()
        Outstr = ""
        printstr(self.ShowInventory())
        printstr("Which item to use?\n")
        ItemToUse = input()

        if ItemToUse == "" or ItemToUse == " ":
            return ""
        CorrectInput = False

        while CorrectInput != True:
            if not ItemToUse.isnumeric:
                printstr("Faulty Input!")

            CorrectInput = True
            self.StatUsedItems += 1

        if self.Inventory[int(ItemToUse)][1] == "Swrd":
            self.DmgMultiplier = 1
            self.ArmorPenMult = 1
            self.DmgMultiplier += self.Inventory[int(ItemToUse)][2]
            self.ArmorPenMult += self.Inventory[int(ItemToUse)][3]
            Outstr += str(self.Inventory[int(ItemToUse)][0])
            del self.Inventory[int(ItemToUse)]

        elif self.Inventory[int(ItemToUse)][1] == "Shld":
            self.DefenseMultShield = 1
            self.DefenseMultShield += self.Inventory[int(ItemToUse)][2]
            Outstr += str(self.Inventory[int(ItemToUse)][0])
            del self.Inventory[int(ItemToUse)]

        elif self.Inventory[int(ItemToUse)][1] == "Misc":
            if self.Inventory[int(ItemToUse)][2] == "Flashlight":
                if self.MapRange >= 4:
                    return "Already Maximum!"
                self.MapRange += self.Inventory[int(ItemToUse)][4]
                Outstr += str(self.Inventory[int(ItemToUse)][0])
                del self.Inventory[int(ItemToUse)]

        elif self.Inventory[int(ItemToUse)][1] == "Potn":
            self.StatPotionsDrank += 1

            if self.Inventory[int(ItemToUse)][2] == "Health":
                self.Health += self.Inventory[int(ItemToUse)][3]
                if self.Health >= self.MaxHealth:
                    self.Health = self.MaxHealth


            elif self.Inventory[int(ItemToUse)][2] == "Regen":
                self.PotionEffects.append(self.Inventory[int(ItemToUse)])
                self.MaxHealth += self.Inventory[int(ItemToUse)][3]

            elif self.Inventory[int(ItemToUse)][2] == "ArmorPen":
                self.PotionEffects.append(self.Inventory[int(ItemToUse)])
                self.ArmorPenMult = 1
                self.ArmorPenMult += self.Inventory[int(ItemToUse)][3]
            
            Outstr += str(self.Inventory[int(ItemToUse)][0])
            del self.Inventory[int(ItemToUse)]
            #elif self.Inventory[int(ItemToUse)][2] == "Health":
        
        
        return "Used : " + Outstr
        
    def CheckPotions(self):
        for potn in self.PotionEffects:
            if potn[4] <= 0:
                del potn
            else:
                potn[4] -= 1
                self.DmgMultiplier = 1
                self.ArmorPenMult = 1
                self.DefenseMultPotion = 1

                if potn[2] == "Regen":
                    self.Health += potn[3]
                    return potn[2]
                elif potn[2] == "ArmorPen":
                    self.ArmorPenMult += potn[2]

class Chest():
    def __init__(self,StartXpos,StartYpos,Value):
        self.Xpos = StartXpos
        self.Ypos = StartYpos
        self.Value = Value
        self.Inventory = []
        self.empty = False

        gr1 = 35
        gr2 = 65
        gr3 = 85
        gr4 = 95
        gr5 = 100
        #AmountGrades = 5
        RemainGrades = self.Value

        while RemainGrades>0:
            randnum = randint(1,100)
            if randnum <= gr1:
                RarGrade = 1
            elif randnum > gr1 and randnum <= gr2:
                RarGrade = 2
            elif randnum > gr2 and randnum <= gr3:
                RarGrade = 3
            elif randnum > gr3 and randnum <= gr4:
                RarGrade = 4
            elif randnum > gr4 and randnum <= gr5:
                RarGrade = 5

            if RemainGrades - RarGrade >= 0:
                randCat = randint(0,2)
                randIt = randint(1,len(Items[randCat][1])) -1
                if Items[randCat][1][randIt][1] == "Swrd":
                    if Items[randCat][1][randIt][4] == RarGrade:
                        self.Inventory.append(Items[randCat][1][randIt])
                        RemainGrades -= RarGrade

                elif Items[randCat][1][randIt][1] == "Shld":
                    if Items[randCat][1][randIt][3] == RarGrade:
                        self.Inventory.append(Items[randCat][1][randIt])
                        RemainGrades -= RarGrade

                elif Items[randCat][1][randIt][1] == "Potn":
                    if Items[randCat][1][randIt][5] == RarGrade:
                        self.Inventory.append(Items[randCat][1][randIt])
                        RemainGrades -= RarGrade

                elif Items[randCat][1][randIt][1] == "Misc":
                    if Items[randCat][1][randIt][3] == RarGrade:
                        self.Inventory.append(Items[randCat][1][randIt])
                        RemainGrades -= RarGrade
   
class Enemy():
    def __init__(self,StartXpos,StartYpos,Health,Dmg,Name,StandArmorPen=0,Standdefense=5):
        self.Name = Name
        self.Xpos = StartXpos
        self.Ypos = StartYpos
        self.Health = Health
        self.Defense = Standdefense
        self.Dmg = Dmg
        self.ArmorPen = StandArmorPen
        self.alive = True
        self.Inventory = []
        self.AmountKeys = 0
        self.AmountCoins = 0
        self.LatestAttack = "None"

        randnum = randint(1,10)
        if randnum >= 9:

            #self.Inventory.append(NewItem)
            randCat = randint(0,2)
            randIt = randint(1,len(Items[randCat][1])) -1
            self.Inventory.append(Items[randCat][1][randIt])
        elif randnum <= 8 and randnum >= 6:
            randAmountKeys = randint(1,2)
            self.AmountKeys += randAmountKeys

    def AttackPlayer(self):
        if User.Xpos == self.Xpos and User.Ypos == self.Ypos:
            randnum = randint(1,100)

            if randnum >0 and randnum <=50:
                return self.LightAttack()

            elif randnum >50 and randnum <= 80:
                return self.MediumAttack()

            elif randnum >80 and randnum <= 95:
                return self.HeavyAttack()

            elif randnum > 95 and randnum <= 100:
                return self.CritAttack()

    def GetAttacked(self):
        self.Health -= int(User.StandDmg*User.DmgMultiplier)-(self.Defense-(User.StandArmorPen*User.ArmorPenMult))

    def LightAttack(self):
        self.LatestAttack = colorama.Fore.LIGHTBLUE_EX + "Light Attack"
        return User.GetDamage(int(self.Dmg*2),self.ArmorPen)

    def MediumAttack(self):
        self.LatestAttack = colorama.Fore.LIGHTYELLOW_EX + "Medium Attack"
        return User.GetDamage(int(self.Dmg*2.5),self.ArmorPen)

    def HeavyAttack(self):
        self.LatestAttack = colorama.Fore.LIGHTRED_EX + "Heavy Attack"
        return User.GetDamage(int(self.Dmg*3),self.ArmorPen)
    
    def CritAttack(self):
        self.LatestAttack = colorama.Fore.RED + "Critical Attack"
        return User.GetDamage(int(self.Dmg*5),self.ArmorPen)

def RandItem():
    global Items
    randCat = randint(0,2)
    randIt = randint(1,len(Items[randCat][1])) -1
    return Items[randCat][1][randIt]

def InitPlayfield():
    global PlayField
    for i in range(0,len(PlayField)):
        #print("in i")
        for j in range(0,len(PlayField[i])):
            if len(PlayField[i][j])<=1:
                if PlayField[i][j] == ['z']:
                # print("Found zomb")
                    NewZomb = Enemy(j,i,50,10,(colorama.Fore.GREEN +"Zombie"+colorama.Fore.WHITE))
                    EnemysArr.append(NewZomb)
                if PlayField[i][j] == ['ch']:
                    NewChest = Chest(j,i,randint(1,4))
                    ChestsArr.append(NewChest)
            else:
                for k in range(0,len(PlayField[i][j])):
                #print(PlayField[i][j])
                    if PlayField[i][j][k] == 'z':
                    # print("Found zomb")
                        NewZomb = Enemy(j,i,50,10,(colorama.Fore.GREEN +"Zombie"+colorama.Fore.WHITE))
                        EnemysArr.append(NewZomb)
                    if PlayField[i][j][k] == 'ch':
                        NewChest = Chest(j,i,randint(1,4))
                        ChestsArr.append(NewChest)

def GetInput(inp):
    global GameEnd
    if inp == "" or inp == " ":
        return
    
    if CheckInpInArr(inp,0,0):
        
        GetMoveInput(inp)
    elif CheckInpInArr(inp,1,0):
        printstr(User.Attack())
        pass
    elif CheckInpInArr(inp,2,0):
        printstr(User.OpenChest())
        pass
    elif CheckInpInArr(inp,3,0):
        printstr(User.ShowInventory())
        pass
    elif CheckInpInArr(inp,4,0):
        printstr(User.UseItem())
        pass
    elif CheckInpInArr(inp,5,0):
        ClearCons()
        printstr(LoostHelp)
        pass
    elif CheckInpInArr(inp,6,0):
        ClearCons()
        printstr(Statistics())
        pass
    elif CheckInpInArr(inp,7,0):
        ClearCons()
        ShowOptions()
    elif CheckInpInArr(inp,8,0):
        ClearCons()
        printstr(ShowMap(True))
    elif CheckInpInArr(inp,9,0):
        ClearCons()
        ShowCheats()
    elif CheckInpInArr(inp,10,0):
        ClearCons()
        GameEnd = True
    elif CheckInpInArr(inp,11,0):
        ClearCons
        printstr(SaveGame())
        
def GetMoveInput(inp):
    print("Please Direction!")
    NewInp = input()
    if NewInp == "" or NewInp == " ":
        return
    if CheckInpInArr(NewInp,0,1,1):
            User.Move("Up")
            printstr("Moving Up")
            return

    elif CheckInpInArr(NewInp,0,2,1):
            User.Move("Right")
            printstr("Moving Right")
            return

    elif CheckInpInArr(NewInp,0,3,1):
            User.Move("Down")
            printstr("Moving Down")
            return

    elif CheckInpInArr(NewInp,0,4,1):
            User.Move("Left")
            printstr("Moving Left")
            return
    
def CheckInpInArr(Inp,index1=0,index2=0,index3=100):
    if index3 != 100:
        for i in InputOpt[index1][index2][index3]:
            if i == Inp:
                return True
        return False

    elif index3 == 100:
        for i in InputOpt[index1][index2]:
            if i == Inp:
                return True
        return False

def ClearCons():
    system("cls")

def ChoosePlayerClass():
    global User
    print("Please Choose a Class\n"+colorama.Fore.BLUE+"1.Assassin"+colorama.Fore.WHITE+" | "+colorama.Fore.RED+"2.Attaker"+colorama.Fore.WHITE+" | "+colorama.Fore.YELLOW+"3.Knight"+colorama.Fore.WHITE+"\n\n")
    inp = input()
    if inp == "Assassin" or inp == "1":
        User = Player(Health=60,StandDmg=30,StandDefense=5)
    elif inp == "Attacker" or inp == "2": 
        User = Player(Health=70,StandDmg=25,StandDefense=10)
    elif inp == "Knight" or inp == "3": 
        User = Player(Health=100,StandDmg=10,StandDefense=15)

    else:
        User = Player()

def GenOnCor(Xpos,Ypos):
    global MapGenValueMax,MapGenValueMin,EnemysArr,ChestsArr,User
    
    val = randint(MapGenValueMin,MapGenValueMax)
    
    for field in User.GenedFields:
        if field == [Xpos,Ypos]:
            return
    else:
        User.GenedFields.append([Xpos,Ypos])
        for i in range(val):
            i= i
            enRandNum = randint(1,5)
            randnum = randint(1,7)
            if randnum == 1:
                NewChest = Chest(Xpos,Ypos,randint(0,4))
                ChestsArr.append(NewChest)
                #User.GenedFields.append([Xpos,Ypos])
                val -= 1

            elif enRandNum == 1:
                NewZombie = Enemy(Xpos,Ypos,50,10,(colorama.Fore.GREEN +"Zombie"+colorama.Fore.WHITE))
                EnemysArr.append(NewZombie)
                #User.GenedFields.append([Xpos,Ypos])
                val -= 1
            if val <= 0:
                return
        pass

def ShowMap(full=False):
    global EnemysArr,User
    if full == True:
        Shorty = User.MapRange
        User.MapRange = 10
    MMap = [["#" for i in range(User.MapRange*2+1)] for j in range(User.MapRange*2+1)]
    Outstr = "   "
    
    PosCheckX = 0
    PosCheckY = 0 
    for y in range(0,User.MapRange*2+1):
        PosCheckY = y - User.MapRange
        for x in range(0,User.MapRange*2+1):
            PosCheckX = x - User.MapRange
            MMap[y][x] = colorama.Fore.LIGHTBLACK_EX + "#"+colorama.Fore.WHITE

            for fld in User.GenedFields:
                if fld[0] == User.Xpos + PosCheckX and fld[1] == User.Ypos + (PosCheckY)*-1:
                    MMap[y][x] = colorama.Fore.WHITE + "#" + colorama.Fore.WHITE
                    break
            else:
                if full == True:
                    pass
                else:
                    GenOnCor(User.Xpos + PosCheckX,User.Ypos + PosCheckY*-1)
                    MMap[y][x] = colorama.Fore.WHITE + "#" + colorama.Fore.WHITE
            for enem in EnemysArr:
                if enem.alive == True and enem.Xpos == User.Xpos + PosCheckX and enem.Ypos == User.Ypos + (PosCheckY)*-1:
                    MMap[y][x] = colorama.Fore.RED+"#"+colorama.Fore.WHITE

            for chest in ChestsArr:
                if chest.empty == False and chest.Xpos == User.Xpos + PosCheckX and chest.Ypos == User.Ypos + (PosCheckY)*-1:
                        MMap[y][x] = colorama.Fore.YELLOW+"#"+colorama.Fore.WHITE
            

            if y == User.MapRange and x == User.MapRange:
                MMap[y][x] = colorama.Fore.LIGHTGREEN_EX + "#" + colorama.Fore.WHITE
                    
    for y in range(len(MMap)):
        for x in range(len(MMap)):
            Outstr += MMap[y][x]
        Outstr += "\n   "
    if full == True:
        User.MapRange = Shorty
    return Outstr

def GenMap(dire,value):
    if dire == "u":
        for NewY in range(User.Ypos-User.MapRange-1,User.Ypos+User.MapRange+1):
            for x in range(User.Xpos-User.MapRange-1,User.Xpos+User.MapRange+1):
            
                #NewY = User.Ypos + User.MapRange 
                val = value

                for field in User.GenedFields:
                    if field == [x,NewY]:
                        break
                else:
                    User.GenedFields.append([x,NewY])
                    for i in range(val):
                        i=i
                        enRandNum = randint(1,5)
                        randnum = randint(1,7)
                        if randnum == 1:
                            NewChest = Chest(x,NewY,randint(0,4))
                            ChestsArr.append(NewChest)
                            #User.GenedFields.append([x,NewY,randint(0,10)])
                            val -= 1

                        elif enRandNum == 1:
                            NewZombie = Enemy(x,NewY,50,10,(colorama.Fore.GREEN +"Zombie"+colorama.Fore.WHITE))
                            EnemysArr.append(NewZombie)
                            #User.GenedFields.append([x,NewY])
                            val -= 1
                        if val <= 0:
                            return

    elif dire == "r":
        for NewY in range(User.Ypos-User.MapRange,User.Ypos+User.MapRange):
            x = User.Xpos + User.MapRange 
            val = value

            for field in User.GenedFields:
                if field == [x,NewY]:
                    break
            else:
                User.GenedFields.append([x,NewY])
                for i in range(val):
                    enRandNum = randint(1,5)
                    randnum = randint(1,7)
                    if randnum == 1:
                        NewChest = Chest(x,NewY,randint(0,4))
                        ChestsArr.append(NewChest)
                        #User.GenedFields.append([x,NewY])
                        val -= 1

                    elif enRandNum == 1:
                        NewZombie = Enemy(x,NewY,50,10,(colorama.Fore.GREEN +"Zombie"+colorama.Fore.WHITE))
                        EnemysArr.append(NewZombie)
                        #User.GenedFields.append([x,NewY])
                        val -= 1

                    if val <= 0:
                        return
                    
                

                    

    elif dire == "d":
        for x in range(User.Xpos-User.MapRange,User.Xpos+User.MapRange):
            NewY = User.Ypos - User.MapRange  
            val = value

            for field in User.GenedFields:
                if field == [x,NewY]:
                    break
            else:
                User.GenedFields.append([x,NewY])
                for i in range(val):
                    enRandNum = randint(1,5)
                    randnum = randint(1,7)
                    if randnum == 1:
                        NewChest = Chest(x,NewY,randint(0,4))
                        ChestsArr.append(NewChest)
                        #User.GenedFields.append([x,NewY])
                        val -= 1

                    elif enRandNum == 1:
                        NewZombie = Enemy(x,NewY,50,10,(colorama.Fore.GREEN +"Zombie"+colorama.Fore.WHITE))
                        EnemysArr.append(NewZombie)
                        #User.GenedFields.append([x,NewY])
                        val -= 1
                    if val <= 0:
                        return

    elif dire == "l":
        for NewY in range(User.Ypos-User.MapRange,User.Ypos+User.MapRange):
            x = User.Xpos - User.MapRange 
            val = value

            for field in User.GenedFields:
                if field == [x,NewY]:
                    break
            else:
                User.GenedFields.append([x,NewY])
                for i in range(val):
                    enRandNum = randint(1,5)
                    randnum = randint(1,7)
                    if randnum == 1:
                        NewChest = Chest(x,NewY,randint(0,4))
                        ChestsArr.append(NewChest)
                        #User.GenedFields.append([x,NewY])
                        val -= 1

                    elif enRandNum == 1:
                        NewZombie = Enemy(x,NewY,50,10,(colorama.Fore.GREEN +"Zombie"+colorama.Fore.WHITE))
                        EnemysArr.append(NewZombie)
                        #User.GenedFields.append([x,NewY])
                        val -= 1
                    if val <= 0:
                        return

def CheckEnemys():
    ClearCons()
    Outstr = ""
    FoundEnem = False
    FoundEnem = FoundEnem
    for enem2 in EnemysArr:
        if User.Ypos == enem2.Ypos and User.Xpos == enem2.Xpos and enem2.alive == True:
            FoundEnem = True
            PlayerGotDmg = enem2.AttackPlayer()
            if PlayerGotDmg <= 0 or PlayerGotDmg == None:
                Outstr += ("You got " +colorama.Fore.RED+str()+"0 Dmg"+colorama.Fore.WHITE+"!"+"\n")

            else:
                #self.StatDmgGot += PlayerGotDmg
                Outstr+= ("You got " +colorama.Fore.RED+str(PlayerGotDmg)+" Dmg"+colorama.Fore.WHITE+"! By "+enem2.LatestAttack+colorama.Fore.WHITE+"\n")
    printstr(Outstr)
    #if FoundEnem == True:
        #input() 
    #Outstr

def ShowOptions():
    InCorrectInput = True
    while InCorrectInput:
        ClearCons()
        printstr(f"""
    0 - Exit
    1 - Change Performance Mode - {str(User.OptPerfMode)}
    2 - Change Cheat Mode - {str(User.OptCheatMode)}

    """)
        inp = input()
        if inp == "0":
            InCorrectInput = False
        elif inp == "1":
            if User.OptPerfMode == True:
                User.OptPerfMode = False
                InitPerfMode(User.OptPerfMode)
                
            elif User.OptPerfMode == False:
                User.OptPerfMode = True
                InitPerfMode(User.OptPerfMode)
        elif inp == "2":
            if User.OptCheatMode == True:
                User.OptCheatMode = False
            elif User.OptCheatMode == False:
                User.OptCheatMode = True

def ShowCheats():
    InCorInp = True
    while InCorInp:
        ClearCons()
        printstr("""
    0- Exit
    1- Give Item
    2- Set Attribute

    """)
        inp = input()
        if inp == "0":
            InCorInp = False
        elif inp == "1":
            printstr("Coming Soon!")
        elif inp == "2":
            CheatChangeAttributes()

def GetNumInp():
    InCorInp = True
    while InCorInp:
        inp = input("Value : ")
        if not inp.isnumeric or inp == None or inp == "" or inp == " ":
            printstr("Faulty Input!\n")
        else:
            InCorInp = False
    return int(inp)

def CheatChangeAttributes():
    InCorInp = True
    while InCorInp:
        ClearCons()
        printstr("""
    0- Exit
    1- Health
    2- Max Health
    3- Map Range
    4- Stand Damage
    5- Stand Defense
    6- Amount Keys
    """)   
        inp = GetNumInp()
        
        if inp == 0:
            InCorInp = False
        elif inp == 1:
            ClearCons()
            User.Health = GetNumInp()
        elif inp == 2:
            ClearCons()
            User.MaxHealth = GetNumInp()
        elif inp == 3:
            ClearCons()
            User.MapRange = GetNumInp()
        elif inp == 4:
            ClearCons()
            User.StandDmg = GetNumInp()
        elif inp == 5:
            ClearCons()
            User.StandDefense = GetNumInp()
        elif inp == 6:
            ClearCons()
            User.AmountKeys = GetNumInp()

def Statistics():
    OutString = f"""
    Killed Enemys   : {User.StatKilledEnemys}
        DMG Dealt       : {User.StatDmgDealt}
    Amount Attacks  : {User.StatAttacks}
    DMG Got         : {User.StatDmgGot}
    Openend Chests  : {User.StatOpenedChests}
    Found Items     : {User.StatFoundItems}
    Used Items      : {User.StatUsedItems}
    Potions Drinked : {User.StatPotionsDrank}
    Total Moves     : {User.StatMovesDone}


    Loost by Sturmy
    """
    return OutString

def LoadGame():
    global User,SaveName,EnemysArr,ChestsArr
    FileCheck = pathlib.Path(SaveName)
    if FileCheck.exists():
        User = Player()
        SaveFile = open(SaveName,"rt")
        savetxt = SaveFile.read()
        savejson = json.loads(savetxt)
        User.Xpos = savejson['PXpos']
        User.Ypos = savejson['PYpos']
        User.MaxHealth = savejson['PMaxHealth']
        User.Health = savejson['PHealth']
        User.AmountKeys = savejson['PAmountKeys']
        User.StandDmg = savejson['PStandDmg']
        User.StandDefense = savejson['PStandDef']
        User.DefenseMultShield = savejson['PDefMultShd']
        User.DefenseMultPotion = savejson['PDefMultPotn']
        User.DmgMultiplier = savejson['PDmgMult']
        User.MapRange = savejson['PMapRange']
        User.ArmorPenMult = savejson['PArmorPenMult']
        User.StandArmorPen = savejson['PStandArmorPen']
        User.PotionEffects = savejson['PPotionEffects']
        User.GenedFields = savejson['PGendFields']
        User.Inventory = savejson['PInventory']
        
        User.StatKilledEnemys = savejson['PStatKilledEnemys']
        User.StatAttacks = savejson['PStatAttacks']
        User.StatDmgDealt = savejson['PStatDmgDealt']
        User.StatOpenedChests = savejson['PStatOpenedChests']
        User.StatFoundItems = savejson['PStatFoundItems']
        User.StatDmgGot = savejson['PStatDmgGot']
        User.StatPotionsDrank = savejson['PStatPotionsDrank']
        User.StatMovesDone = savejson['PStatMovesDone']
        User.StatUsedItems = savejson['PStatUsedItems']
        User.OptPerfMode = savejson['POptPerfMode']
        User.OptCheatMode = savejson['POptCheatMode']

        for enem in savejson['Enemys']:
            Newenem = Enemy(0,0,0,0,"")

            Newenem.Name = enem[0]
            Newenem.Xpos = enem[1]
            Newenem.Ypos = enem[2]
            Newenem.Health = enem[3]
            Newenem.Defense = enem[4]
            Newenem.Dmg = enem[5]
            Newenem.ArmorPen = enem[6]
            Newenem.alive = enem[7]
            Newenem.AmountKeys = enem[8]
            Newenem.AmountCoins = enem[9]
            Newenem.Inventory = enem[10]
            EnemysArr.append(Newenem)

        for chest in savejson['Chests']:
            NewChest = Chest(0,0,0)

            NewChest.Xpos = chest[0]
            NewChest.Ypos = chest[1]
            NewChest.Value = chest[2]
            NewChest.empty = chest[3]
            NewChest.Inventory = chest[4]

            ChestsArr.append(NewChest)

        return "Loaded Game!\n"
    else:
        return "Fail"

def SaveGame():
    global User,EnemysArr,ChestsArr,SaveName

    jsFile = open(SaveName,"wt")
    JsonStr = {
        "PXpos" : User.Xpos,
        "PYpos" : User.Ypos,
        "PMaxHealth" : User.MaxHealth,
        "PHealth" : User.Health,
        "PAmountKeys" : User.AmountKeys,
        "PStandDmg" : User.StandDmg,
        "PStandDef" : User.StandDefense,
        "PDefMultShd" : User.DefenseMultShield,
        "PDefMultPotn" : User.DefenseMultPotion,
        "PDmgMult" : User.DmgMultiplier,
        "PMapRange" : User.MapRange,
        "PArmorPenMult" : User.ArmorPenMult,
        "PStandArmorPen" : User.StandArmorPen,
        "PPotionEffects":User.PotionEffects,
        "PGendFields":User.GenedFields,
        "PInventory":User.Inventory,
        "PStatKilledEnemys": User.StatKilledEnemys,
        "PStatAttacks":User.StatAttacks,
        "PStatDmgDealt":User.StatDmgDealt,
        "PStatOpenedChests":User.StatOpenedChests,
        "PStatFoundItems":User.StatFoundItems,
        "PStatDmgGot":User.StatDmgGot,
        "PStatPotionsDrank":User.StatPotionsDrank,
        "PStatMovesDone":User.StatMovesDone,
        "PStatUsedItems":User.StatUsedItems,
        "POptPerfMode":User.OptPerfMode,
        "POptCheatMode":User.OptCheatMode,
        "Enemys":[

        ],
        "Chests":[

        ]

    }
    for enem in EnemysArr:
        JsonStr["Enemys"] += [[enem.Name,enem.Xpos,enem.Ypos,enem.Health,enem.Defense,enem.Dmg,enem.ArmorPen,enem.alive,enem.AmountKeys,enem.AmountCoins,enem.Inventory]]

    for chest in ChestsArr:
        JsonStr["Chests"] += [[chest.Xpos,chest.Ypos,chest.Value,chest.empty,chest.Inventory]]

    jsFile.write(json.dumps(JsonStr,indent=4))
    return "Game Saved!\n"

def NewGame():
    ClearCons()
    ChoosePlayerClass()

def GameStart(state="load"):
    if state == "load":
        shorty = LoadGame()
        shorty = shorty
        if shorty != "Fail":
            Main()
            return "Exiting!\n"
        else:
            return "There's no save to load!\n"
    elif state == "new":
        NewGame()
        Main()
        return "Exiting!\n"

def Main():
    global GameEnd
    ClearCons()
    GameEnd = False
    running = True
    while running:
        ClearCons()
        PotnStr = ""
        PotnStr += "+"+colorama.Fore.LIGHTRED_EX+str(User.CheckPotions())
        #ShowMap()
        printstr(f"""
    Status :  {colorama.Fore.RED+str(int(User.Health))+colorama.Fore.WHITE} Hp | {User.Xpos}x / {User.Ypos}y
            {colorama.Fore.LIGHTRED_EX+ str(int(User.StandDmg*User.DmgMultiplier))+colorama.Fore.WHITE} Dmg | {colorama.Fore.LIGHTBLUE_EX+str(int(User.StandDefense * User.DefenseMultShield))+colorama.Fore.WHITE} Def | {colorama.Fore.MAGENTA+str(int(User.StandArmorPen*User.ArmorPenMult))+colorama.Fore.WHITE} Armor Pen\n\n"""+
    str(ShowMap())

    +"""                            

    Move | Attack | Open Chest | Use Item | Show Map | Inventory

    Help | Options

    """
        )
        printstr(User.GetStatus())

        printstr(">>Please Choose Action<<\n")
        
        GetInput(input())
        User.StatMovesDone += 1
        if GameEnd == True:
            return
        #print(EnemysArr)
        input()