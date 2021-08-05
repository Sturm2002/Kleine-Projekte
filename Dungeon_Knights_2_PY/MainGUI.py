import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as MsgBox
from tkinter import filedialog

from globalVars import *
import Start_Game
from NewGame import StartNewGame
from assets import PixelSz
from time import sleep
import json

def Shorty():
    pass

def InitTK():
    
    root = tk.Tk()
    #root.geometry("800x600+300+300")
    root.title("Main Menu")
    
    root.configure(background=DARKRED)
    return root

class BackButton(tk.Frame):
    def __init__(self,master):
        self.btn_back = tk.Button(master,text="Back",font="Forte " + str(PixelSz(15)) +" bold",bg="black",fg="white",command=master.BackPressed)
        self.btn_back.place(x=PixelSz(20),y=PixelSz(980),width=PixelSz(150),height=PixelSz(50))

class MainWindow(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.configure(width=PixelSz(1920),height=PixelSz(1080),bg=DARKRED)
        self.master.attributes("-fullscreen",True)
        
        self.pack()
        self.InitMainMenuWidgets()

        ComboStyle = ttk.Style()

        ComboStyle.theme_create('combostyle',parent='alt',
            settings = {'TCombobox':
                        {'configure':
                         {'selectbackground':'black',
                          'fieldbackground':'black',
                          'background':'black',
                          'foreground':'white'
                         }}})

        ComboStyle.theme_use('combostyle') 

        #print(ComboStyle.theme_names())

    def InitMainMenuWidgets(self):

        StartPosButtons = 200
        DistPosButtons = 150

        lbl_Title = tk.Label(self,text="Dungeon Knights",bg=DARKRED,fg="white",font="Forte " + str(PixelSz(80)) +" bold")
        lbl_Title.configure(justify="center",anchor="c")
        lbl_Title.place(x=PixelSz(420),y=PixelSz(30),width=PixelSz(1000),height=PixelSz(300))

        btn_NewGame = tk.Button(self,text="New Game",font="Forte " + str(PixelSz(20)) +" bold",bg="black",fg="white",command=self.NewGamePressed)
        btn_NewGame.place(x=PixelSz(750),y=PixelSz(StartPosButtons + (DistPosButtons * 1)),width=PixelSz(400),height=PixelSz(100))

        btn_LoadGame = tk.Button(self,text="Load Game",font="Forte " + str(PixelSz(20)) +" bold",bg="black",fg="white",command=self.LoadGamePressed)
        btn_LoadGame.place(x=PixelSz(750),y=PixelSz(StartPosButtons + (DistPosButtons * 2)),width=PixelSz(400),height=PixelSz(100))

        btn_StartEditor = tk.Button(self,text="Start Editor",font="Forte " + str(PixelSz(20)) +" bold",bg="black",fg="white",command=self.StartEditorPressed)
        btn_StartEditor.place(x=PixelSz(750),y=PixelSz(StartPosButtons + (DistPosButtons * 3)),width=PixelSz(400),height=PixelSz(100))

        btn_Exit = tk.Button(self,text="Exit",font="Forte " + str(PixelSz(20)) +" bold",bg="black",fg="white",command=self.ExitPressed)
        btn_Exit.place(x=PixelSz(750),y=PixelSz(StartPosButtons + (DistPosButtons * 4)),width=PixelSz(400),height=PixelSz(100))

        lbl_CreatorTitle = tk.Label(self,text="By Sturmy & Gabriel",bg=DARKRED,fg="white",font="Forte " + str(PixelSz(10)) +" bold")
        lbl_CreatorTitle.configure(justify="center",anchor="c")
        lbl_CreatorTitle.place(x=PixelSz(1730),y=PixelSz(1000),width=PixelSz(200),height=PixelSz(50))

    def LoadingScreen(self,NextWindow):
        self.ClearFrame()
        self.InitLoadingScreenWidgets()
        self.master.update()
        self.ClearFrame()
        if NextWindow == "PlayGui":
            self.InitPlayGuiWidgets()

        elif NextWindow == "NewGameGui":
            self.InitNewGameGuiWidgets()

        elif NextWindow == "LoadGameGui":
            self.InitLoadGameGuiWidgets()

        elif NextWindow == "EditorGui":
            self.InitEditorGuiWidgets()

        elif NextWindow == "MainMenuGui":
            self.InitMainMenuWidgets()

        else:
            raise Exception("NextWindowNotFound")

    def InitLoadingScreenWidgets(self):
        lbl_LoadTitle = tk.Label(self,text="Loading...",bg=DARKRED,fg="white",font="Forte " + str(PixelSz(80)) +" bold")
        lbl_LoadTitle.configure(justify="center",anchor="nw")
        lbl_LoadTitle.place(x=PixelSz(50),y=PixelSz(50),width=PixelSz(600),height=PixelSz(200))

    def InitNewGameGuiWidgets(self):
        global AmountPlayers,Max_Players,PlayersArray,AmountPlayersShowText,Characters,NewPlayerNameStr,NewPlayerCharStr,CharsArr0
        global cmb_NewPlayerChar,txt_NewPlayerName,PlayerNamesStr,PlayerCharsStr,Difficulty

        Difficulty = tk.IntVar()
        
        PlayerNamesStr = tk.StringVar()
        PlayerCharsStr = tk.StringVar()

        NewPlayerNameStr,NewPlayerCharStr = tk.StringVar(),tk.StringVar()

        

        lbl_PlayerNames = tk.Label(self,textvariable=PlayerNamesStr,font="Forte " +str(PixelSz(40))+" bold",bg=DARKRED,fg="white",justify="left",anchor="nw")
        lbl_PlayerChars = tk.Label(self,textvariable=PlayerCharsStr,font="Forte " +str(PixelSz(40))+" bold",bg=DARKRED,fg="white",justify="left",anchor="nw")

        lbl_PlayerNames.place(x=PixelSz(100),y=PixelSz(200),width=PixelSz(400),height=PixelSz(600))
        lbl_PlayerChars.place(x=PixelSz(400),y=PixelSz(200),width=PixelSz(700),height=PixelSz(600))

        btn_NewPlayer = tk.Button(self,text="New Player",command=self.NewPlayerPressed,font="Forte " +str(PixelSz(10))+" bold",bg="black",fg="white")
        btn_NewPlayer.place(x=PixelSz(1050),y=PixelSz(350),width=PixelSz(190),height=PixelSz(50))

        btn_DelLastPlayer = tk.Button(self,text="Delete Player",command=self.DeleteLastPlayer,font="Forte " +str(PixelSz(10))+" bold",bg="black",fg="white")
        btn_DelLastPlayer.place(x=PixelSz(1250),y=PixelSz(350),width=PixelSz(100),height=PixelSz(50))


        txt_NewPlayerName = tk.Entry(self,textvariable=NewPlayerNameStr,font="Forte " +str(PixelSz(20))+" bold",bg="black",fg="white",justify="left")
        txt_NewPlayerName.place(x=PixelSz(1050),y=PixelSz(210),width=PixelSz(300),height=PixelSz(50))

        cmb_NewPlayerChar = ttk.Combobox(self,textvariable=NewPlayerCharStr,state="readonly",values=CharsArr0,font="Forte " +str(PixelSz(15))+" bold",background="black",foreground="white")
        cmb_NewPlayerChar.place(x=PixelSz(1050),y=PixelSz(280),width=PixelSz(300),height=PixelSz(50))

        btn_GetMapPath = tk.Button(self,text="Select Map",command=self.GetMapPathPressed,font="Forte " +str(PixelSz(10))+" bold",bg="black",fg="white")
        btn_GetMapPath.place(x=PixelSz(1600),y=PixelSz(200),width=PixelSz(200),height=PixelSz(80))

        lbl_PlayersTitle = tk.Label(self,text="Players",font="Forte " +str(PixelSz(60))+" bold",bg=DARKRED,fg="white",justify="left",anchor="nw")
        lbl_PlayersTitle.place(x=PixelSz(200),y=PixelSz(80),width=PixelSz(400),height=PixelSz(100))

        lbl_NewPlayerTitle = tk.Label(self,text="New Player",font="Forte " +str(PixelSz(40))+" bold",bg=DARKRED,fg="white",justify="left",anchor="nw")
        lbl_NewPlayerTitle.place(x=PixelSz(1050),y=PixelSz(100),width=PixelSz(280),height=PixelSz(60))

        lbl_SettingsTitle = tk.Label(self,text="Settings",font="Forte " +str(PixelSz(50))+" bold",bg=DARKRED,fg="white",justify="left",anchor="nw")
        lbl_SettingsTitle.place(x=PixelSz(1580),y=PixelSz(80),width=PixelSz(250),height=PixelSz(75))

        rdb_radioDiff0 = tk.Radiobutton(self,text="Hardcore",variable=Difficulty,value=0,justify="left",anchor="nw",font="Forte "+str(PixelSz(20)) + " bold",foreground="white",bg=DARKRED)
        rdb_radioDiff1 = tk.Radiobutton(self,text="Hard",variable=Difficulty,value=1,justify="left",anchor="nw",font="Forte "+str(PixelSz(20)) + " bold",foreground="white",bg=DARKRED)
        rdb_radioDiff2 = tk.Radiobutton(self,text="Normal",variable=Difficulty,value=2,justify="left",anchor="nw",font="Forte "+str(PixelSz(20)) + " bold",foreground="white",bg=DARKRED)
        rdb_radioDiff3 = tk.Radiobutton(self,text="Easy",variable=Difficulty,value=3,justify="left",anchor="nw",font="Forte "+str(PixelSz(20)) + " bold",foreground="white",bg=DARKRED)
        rdb_radioDiff4 = tk.Radiobutton(self,text="Noob",variable=Difficulty,value=4,justify="left",anchor="nw",font="Forte "+str(PixelSz(20)) + " bold",foreground="white",bg=DARKRED)

        firstRadioPosY = 320
        DistRadioPosY = 50

        rdb_radioDiff0.place(x=PixelSz(1600),y=PixelSz(firstRadioPosY + (DistRadioPosY*0)),width=PixelSz(200),height=PixelSz(50))
        rdb_radioDiff1.place(x=PixelSz(1600),y=PixelSz(firstRadioPosY + (DistRadioPosY*1)),width=PixelSz(200),height=PixelSz(50))
        rdb_radioDiff2.place(x=PixelSz(1600),y=PixelSz(firstRadioPosY + (DistRadioPosY*2)),width=PixelSz(200),height=PixelSz(50))
        rdb_radioDiff3.place(x=PixelSz(1600),y=PixelSz(firstRadioPosY + (DistRadioPosY*3)),width=PixelSz(200),height=PixelSz(50))
        rdb_radioDiff4.place(x=PixelSz(1600),y=PixelSz(firstRadioPosY + (DistRadioPosY*4)),width=PixelSz(200),height=PixelSz(50))

        

        lbl_NewGameTitle = tk.Label(self,text="New Game",font="Forte " +str(PixelSz(40))+" bold",bg=DARKRED,fg="black",justify="left",anchor="nw")
        lbl_NewGameTitle.place(x=PixelSz(2),y=PixelSz(2),width=PixelSz(400),height=PixelSz(100))

        btn_Play = tk.Button(self,text="Play",command=self.PlayPressed,font="Forte " +str(PixelSz(20))+" bold",bg="black",fg="white",justify="center",anchor="c")
        btn_Play.place(x=PixelSz(1600),y=PixelSz(900),width=PixelSz(400),height=PixelSz(100))

    
        btn_back = BackButton(self)

    def PlayPressed(self):
        self.ClearFrame()
        StartNewGame(MapFilePath)

    def GetMapPathPressed(self):
        global MapFilePath
        MapFilePath = filedialog.askopenfilename()
        print(MapFilePath)

    def NewPlayerPressed(self):
        global PlayerCharsStr,PlayerNamesStr,NewGamePlayers,cmb_NewPlayerChar,txt_NewPlayerName,AmountPlayers,Max_Players
        if not AmountPlayers >= Max_Players:
            if txt_NewPlayerName.get() != "" and cmb_NewPlayerChar.get() != "":
                NewGamePlayers.append([txt_NewPlayerName.get(),cmb_NewPlayerChar.get(),(Characters[CharsArr0.index(cmb_NewPlayerChar.get())][1])])     
                CachePlayerNames = ""
                CachePlayerChars = ""

                AmountPlayers = len(NewGamePlayers)

                for i in NewGamePlayers:
                    ind = CharsArr0.index(i[1])
                    CachePlayerNames += i[0] + "\n"
                    CachePlayerChars += i[1] + "\n"
                    
                PlayerNamesStr.set(CachePlayerNames)
                PlayerCharsStr.set(CachePlayerChars)
            else:
                MsgBox.showwarning("Error","Nothing Entered")
        else:
            MsgBox.showwarning("Error","Too Many Players")

    def DeleteLastPlayer(self):
        global PlayerCharsStr,PlayerNamesStr,NewGamePlayers,cmb_NewPlayerChar,txt_NewPlayerName,AmountPlayers,Max_Players
        if not AmountPlayers < 1:

            NewGamePlayers.pop()

            AmountPlayers = len(NewGamePlayers)

            CachePlayerNames = ""
            CachePlayerChars = ""

            for i in NewGamePlayers:
                CachePlayerNames += i[0] + "\n"
                CachePlayerChars += i[1] + "\n"

            PlayerNamesStr.set(CachePlayerNames)
            PlayerCharsStr.set(CachePlayerChars)
        else:
            MsgBox.showwarning("Error","Not Enough Players")

    def InitPlayGuiWidgets(self):
        btn_back = BackButton(self)

    def InitLoadGameGuiWidgets(self):
        btn_back = BackButton(self)

    def InitEditorGuiWidgets(self):
        btn_back = BackButton(self)

        lbl_mainTitle = tk.Label(self,text="Editor",font="Forte " +str(PixelSz(30))+" bold",bg=DARKRED,fg="black",justify="left",anchor="nw")

    def ClearFrame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def NewGamePressed(self):
        self.ClearFrame()
        self.LoadingScreen("NewGameGui")

    def LoadGamePressed(self):
        self.ClearFrame()
        self.LoadingScreen("LoadGameGui")

    def StartEditorPressed(self):
        self.ClearFrame()
        self.LoadingScreen("EditorGui")

    def BackPressed(self):
        self.ClearFrame()
        self.LoadingScreen("MainMenuGui")
    
    def ExitPressed(self):
        self.quit()


if __name__ == "__main__":
    Start_Game.Go()