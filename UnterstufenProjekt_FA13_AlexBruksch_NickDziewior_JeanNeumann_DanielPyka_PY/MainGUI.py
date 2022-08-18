# pip3.9 tkinter;hashlib;pip3.9 install pygame;pip3.9 install time;pip3.9 install PIL;pip3.9 install os;pip3.9 install copy;pip3.9 install sys;pip3.9 install webbrowser

# pip3.9 install hashlib,random,pygame,webbrowser,globalVars,Datenbank,os,sys,copy,tkinter,PIL,time,
import hashlib,random,pygame,webbrowser,globalVars,Datenbank,os,sys,copy
import tkinter as tk
from tkinter import StringVar, image_names, ttk
from tkinter import messagebox as MsgBox
from tkinter import filedialog
from tkinter.constants import DISABLED, NORMAL
from algorithmus import runAlgorithm
from globalVars import *
from assets import PixelSz
from time import sleep
from PIL import Image,ImageTk

ScreenSizeMult = ScreenSizeMultiplicator


def InitTK():
    
    root = tk.Tk()
    #root.geometry("800x600+300+300")
    root.title(WindowTitle)
    root.configure(background=WindowBGColor)
    return root

class MainWindow(tk.Frame):
    
    def __init__(self,master):
        """Wird Ausgeführt wenn man eine instanz von MainWindow Erstellt"""
        super().__init__(master)
        self.master = master
        self.configure(width=1920,height=1080,bg=WindowBGColor)
        #master.attributes("-fullscreen",True)

        self.CurrentMove = True
        self.lastscreen = ""
        self.activescreen = ""
        self.DragObj = ""
        self.AvailablePositions = []
        self.lastfield = []
        self.PasswordConfirm = True
        self.snd_MainVol = copy.deepcopy(snd_MainVolume)
        pygame.mixer.init()
        pygame.mixer.fadeout(1)
        

        self.playfield_startx = copy.deepcopy(PixelSz(playfield_startx))
        self.playfield_distx = copy.deepcopy(PixelSz(playfield_distx))
        self.playfield_starty = copy.deepcopy(PixelSz(playfield_starty))
        self.playfield_disty = copy.deepcopy(PixelSz(playfield_disty))

        self.algo_StandardSearchDepth = copy.deepcopy(algo_StandardSearchDepth)

        self.playfield1StartPos = playfield_startPosGame1

        self.LoggedIn = False
        self.CurrentUsername = ""

        self.StatsMoves = 0
        self.StatsPunkte = 0
        self.StatsKiPunkte = 0
        self.StatsKiMoves = 0

        self.KiChars = 0
        self.UserChars = 0

        

        self.pack()
        os.system("cls")
        self.InitLoadingScreen("main")
    

    def btn_play_pressed(self):
        self.PlaySound("pop")
        self.InitLoadingScreen("play")

    def btn_options_pressed(self):
        self.PlaySound("pop")
        self.InitLoadingScreen("options")

    def btn_help_pressed(self):
        self.PlaySound("pop")
        self.InitLoadingScreen("help")

    def btn_stats_pressed(self):
        self.PlaySound("pop")
        self.InitLoadingScreen("stats")
 
    def btn_exit_pressed(self): 
        exit()

    def btn_credits_pressed(self):
        self.PlaySound("pop")
        self.InitLoadingScreen("credits")


    def btn_back_pressed(self):
        self.InitLoadingScreen("main")
        self.PlaySound("pop")

    def btn_back_sure_pressed1(self):
        self.btn_backs.configure(text="Sicher?",command=self.btn_back_sure_pressed2)

    def btn_back_sure_pressed2(self):
        self.ClearCanv()
        self.InitLoadingScreen("main")
        self.PlaySound("pop")
        pass     

    def btn_register_pressed(self):    
        self.PlaySound("pop")
        self.InitLoadingScreen("register")
        

    def btn_LoginSubmit_pressed(self):
        """Password Hashen und in der Datenbank überprüfen"""
        self.PasswordHash = hashlib.sha256()
        self.PasswordHash.update(str(self.LoginPassword.get()).encode())
        self.PasswordHash = str(self.PasswordHash.hexdigest())

        self.Username = self.LoginUsername.get()
        # @daniel
        if Datenbank.CheckCredentialsDB(self.Username, self.PasswordHash, True) == True:
            self.LoggedIn = True
            self.CheckLoggedIn()
            self.CurrentUsername = self.Username
            pass # user gefunden
    
        else:
            self.LoggedIn = False
            self.txt_LoginUsername.config(bg='#FF0000')
            self.txt_LoginPassword.config(bg='#FF0000')
            self.CheckLoggedIn()
        
            pass # user nicht gefunden
        pass

        # self.Username | self.PasswordHash
        #SQL

    def btn_LoginGuest_pressed(self):
        self.LoggedIn = True
        self.CurrentUsername = "gast"
        self.CheckLoggedIn()

    def btn_RegisterSubmit_Pressed(self):
        """
        Nutzer Registrieren wenn noch nicht vorhanden (Email Verifizierung?)
        """
        """
        self.btn_RegisterSubmit.config(text="Bestätigen")

        self.EmailCodeVar = tk.StringVar()

        lbl_Code = tk.Label(self,text="Verifizierungs Code:",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(13)) +" bold",anchor="nw")
        lbl_Code.place(x=PixelSz(800),y=PixelSz(725),width=PixelSz(200),height=PixelSz(50))

        self.txt_Code = tk.Entry(self,textvariable=self.EmailCodeVar,bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(25)) +" bold")
        self.txt_Code.place(x=PixelSz(800),y=PixelSz(750),width=PixelSz(400),height=PixelSz(75))

        

        if self.EmailCodeCorrect == False:
            if self.EmailSend == False:
                self.EmailValidation()
                
            elif self.EmailSend == True:
                if str(self.EmailCodeVar.get()) == str(self.emailCode):
                    self.EmailCodeCorrect = True
                else:
                    self.EmailCodeCorrect = False
                #self.EmailValidation_CheckCode()

        if self.EmailCodeCorrect == True:
        """
        self.RegPasswordHash = hashlib.sha256()
        self.RegPasswordHash.update(str(self.RegisterPassword.get()).encode())
        self.RegPasswordHash = str(self.RegPasswordHash.hexdigest())

        self.RegUsername = self.RegisterUsername.get()

        if Datenbank.CheckCredentialsDB(self.RegUsername, self.RegPasswordHash, False) == True:
            #@daniel
            
            self.LoggedIn = True
            self.CurrentUsername = self.RegUsername

            self.InitLoadingScreen("main")
        
        else:
            self.txt_RegisterUsername.configure(bg='#FF0000')
            self.txt_RegisterPassword.configure(bg='#FF0000')
            self.txt_RegisterConfirmPassword.configure(bg='#FF0000')
            self.txt_RegisterEmail.configure(bg='#FF0000')
        #self.InitLoadingScreen("main")
        


    def btn_ScreenMultSizeUp_pressed(self):
        """Vergrößert alle elemente von Tkinter"""
        global ScreenSizeMult
        if ScreenSizeMult <= 2:
            ScreenSizeMult += 0.05
            globalVars.ScreenSizeMultiplicator += 0.05
            self.ClearFrame()
            self.InitLoadingScreen("options")

    def btn_ScreenMultSizeDown_pressed(self):
        """Verkleinert alle Elemente von Tkinter"""
        global ScreenSizeMult
        if ScreenSizeMult >= 0.5:
            ScreenSizeMult -= 0.05
            globalVars.ScreenSizeMultiplicator -= 0.05
            self.ClearFrame()
            self.InitLoadingScreen("options")

    def btn_super_secret_button_pressed(self):
        """wenn ich das erklären würde wärs nicht secret"""
        webbrowser.open(SuperDuperSecretButtonLink)


    def btn_Game1_pressed(self):
        self.PlaySound("pop")
        self.InitLoadingScreen("game1")
        
    def btn_Game2_pressed(self):
        self.PlaySound("pop")
        self.InitLoadingScreen("game2")

    def btn_Game3_pressed(self):
        self.PlaySound("pop")
        webbrowser.open("https://www.paypal.com/de/home")


    def InitLoadingScreen(self,nextframe):
        """Wird zum ändern des screens genutzt, nextframe argument gibt das neue Screen an\n
        Möglichkeiten für nextframe:\n
        stats,help,options,play,credits,main,register,game1,game2,game3

        """
        self.ClearFrame()
        # https://gifer.com/en/H8B2

        self.load = Image.open(loading)
        self.load = self.load.resize((PixelSz(150),PixelSz(150)))
        self.loading = ImageTk.PhotoImage(self.load)


        lbl_loadTitle = tk.Label(self,image=self.loading,bg=WindowBGColor,anchor="c")
        lbl_loadTitle.place(x=PixelSz(50),y=PixelSz(50),width=PixelSz(150),height=PixelSz(150))
        self.master.update()
        #sleep(2)
        self.ClearFrame()
        self.CurrentGame = 0

        if nextframe == "stats":
            self.InitStatsScreen()
        elif nextframe == "help":
            self.InitHelpScreen()
        elif nextframe == "options":
            self.InitOptionsScreen()
        elif nextframe == "play":
            self.InitPlayScreen()
        elif nextframe == "credits":
            self.InitCreditsScreen()
        elif nextframe == "main":
            self.InitMainMenu()
        elif nextframe == "register":
            self.InitRegisterScreen()
        elif nextframe == "game1":
            self.StartGame1()
        elif nextframe == "game2":
            self.StartGame2()
        elif nextframe == "game3":
            self.StartGame3()
        else:
            self.InitLoadingScreen("main")
        self.CurrentScreen = nextframe

    def InitMainMenu(self):
        FirstButtonPosY = 400
        ButtonDist = 120

        self.LoginUsername = tk.StringVar()
        self.LoginPassword = tk.StringVar()

        #PasswordHash = LoginPassword.get()
        
        self.lbl_loginUsername = tk.Label(self,text="Username",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(15)) +" bold",anchor="c")
        self.lbl_loginUsername.place(x=PixelSz(1800),y=PixelSz(50),width=PixelSz(200),height=PixelSz(50))

        self.txt_LoginUsername = tk.Entry(self,textvariable=self.LoginUsername,bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(20)) +" bold")
        self.txt_LoginUsername.place(x=PixelSz(1800),y=PixelSz(100),width=PixelSz(200),height=PixelSz(50))

        self.txt_LoginPassword = tk.Entry(self,textvariable=self.LoginPassword,bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(20)) +" bold",show="*")
        self.txt_LoginPassword.place(x=PixelSz(1800),y=PixelSz(200),width=PixelSz(200),height=PixelSz(50))

        self.lbl_loginPassword = tk.Label(self,text="Passwort",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(15)) +" bold",anchor="c")
        self.lbl_loginPassword.place(x=PixelSz(1800),y=PixelSz(150),width=PixelSz(200),height=PixelSz(50))


        self.btn_LoginSubmit = tk.Button(self,text="Login",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(20)) +" bold",command=self.btn_LoginSubmit_pressed)
        self.btn_LoginSubmit.place(x=PixelSz(1825),y=PixelSz(275),width=PixelSz(150),height=PixelSz(40))

        self.btn_LoginRegister = tk.Button(self,text="Registieren",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(17)) +" bold",command=self.btn_register_pressed)
        self.btn_LoginRegister.place(x=PixelSz(1825),y=PixelSz(325),width=PixelSz(150),height=PixelSz(40))

        self.btn_LoginGuest = tk.Button(self,text="Als Gast",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(17)) +" bold",command=self.btn_LoginGuest_pressed)
        self.btn_LoginGuest.place(x=PixelSz(1825),y=PixelSz(375),width=PixelSz(150),height=PixelSz(40))


        self.lbl_Title = tk.Label(self,text="Sudoku-Prototyp",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(60)) +" bold",anchor="c")
        self.lbl_Title.place(x=PixelSz(HalfScreenX-275),y=PixelSz(200),width=PixelSz(700),height=PixelSz(100))

        self.lbl_SubTitle = tk.Label(self,text="Alex.B | Nick.D | Jean.N | Daniel.P",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(20)) +" bold",anchor="c")
        self.lbl_SubTitle.place(x=PixelSz(HalfScreenX-250),y=PixelSz(300),width=PixelSz(600),height=PixelSz(50))

        self.btn_play = tk.Button(self,text="Spielen",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(20)) +" bold",anchor="c",command=self.btn_play_pressed)
        self.btn_play.place(x=PixelSz(HalfScreenX-150),y=PixelSz(FirstButtonPosY + (0*ButtonDist)),width=PixelSz(400),height=PixelSz(100))

        self.btn_options = tk.Button(self,text="Optionen",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(20)) +" bold",anchor="c",command=self.btn_options_pressed)
        self.btn_options.place(x=PixelSz(HalfScreenX-150),y=PixelSz(FirstButtonPosY + (1*ButtonDist)),width=PixelSz(400),height=PixelSz(100))

        self.btn_help = tk.Button(self,text="Hilfe",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(20)) +" bold",anchor="c",command=self.btn_help_pressed)
        self.btn_help.place(x=PixelSz(HalfScreenX-150),y=PixelSz(FirstButtonPosY + (2*ButtonDist)),width=PixelSz(400),height=PixelSz(100))

        self.btn_stats = tk.Button(self,text="Statistik",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(20)) +" bold",anchor="c",command=self.btn_stats_pressed)
        self.btn_stats.place(x=PixelSz(HalfScreenX-150),y=PixelSz(FirstButtonPosY + (3*ButtonDist)),width=PixelSz(400),height=PixelSz(100))

        self.btn_exit = tk.Button(self,text="Verlassen",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(20)) +" bold",anchor="c",command=self.btn_exit_pressed)
        self.btn_exit.place(x=PixelSz(HalfScreenX-150),y=PixelSz(FirstButtonPosY + (4*ButtonDist)),width=PixelSz(400),height=PixelSz(100))

        self.btn_credits = tk.Button(self,text="Credits",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(15)) +" bold",anchor="c",command=self.btn_credits_pressed)
        self.btn_credits.place(x=PixelSz(HalfScreenX-25),y=PixelSz(FirstButtonPosY + (5*ButtonDist)),width=PixelSz(150),height=PixelSz(30))

        self.CheckLoggedIn()



        #btn_secret = tk.Button(self,text="Secret Button",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(20)) +" bold",anchor="c",command=self.btn_super_secret_button_pressed)
        #btn_secret.place(x=PixelSz(HalfScreenX-150),y=PixelSz(FirstButtonPosY + (5*ButtonDist)),width=PixelSz(400),height=PixelSz(100))

    def InitPlayScreen(self):
        FirstButtonPosY = 400
        ButtonDist = 120


        lbl_PlayScreenTitle = tk.Label(self,text="Spiel Auswählen",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(50)) +" bold",anchor="c")
        lbl_PlayScreenTitle.place(x=PixelSz(HalfScreenX-250),y=PixelSz(150),width=PixelSz(600),height=PixelSz(200))

        
        btn_Game1 = tk.Button(self,text="Bauernschach",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(40)) +" bold",anchor="c",command=self.btn_Game1_pressed)
        btn_Game1.place(x=PixelSz(HalfScreenX-150),y=PixelSz(FirstButtonPosY + (0* ButtonDist)),width=PixelSz(400),height=PixelSz(100))
        
        btn_Game2 = tk.Button(self,text="Dame",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(40)) +" bold",anchor="c",command=self.btn_Game2_pressed)
        btn_Game2.place(x=PixelSz(HalfScreenX-150),y=PixelSz(FirstButtonPosY + (1* ButtonDist)),width=PixelSz(400),height=PixelSz(100))
        
        btn_Game3 = tk.Button(self,text="Tic-Tac-Toe (DLC 60€)",bg="grey",fg="dark grey",font="Rockwell " + str(PixelSz(20)) +" bold",anchor="c",command=self.btn_Game3_pressed)
        btn_Game3.place(x=PixelSz(HalfScreenX-150),y=PixelSz(FirstButtonPosY + (2* ButtonDist)),width=PixelSz(400),height=PixelSz(100))

        self.ShowBtn_Back()

    def InitOptionsScreen(self):
        
        #TabsStartPosX = 150
        #TabsPosXDist = 600

        self.VolumeVar = tk.IntVar()
        self.DiffVar = tk.IntVar()
        self.canv = tk.Canvas(self,bg=WindowBGColor)
        self.canv.place(x=-5,y=-5,width=PixelSz(4000),height=PixelSz(3000))

        self.canv.create_line(PixelSz(2020),PixelSz(1130),PixelSz(1810),PixelSz(1130),width=5,fill=WindowAccentColor)
        self.canv.create_line(PixelSz(2020),PixelSz(1130),PixelSz(2020),PixelSz(910),width=5,fill=WindowAccentColor)

        self.canv.create_line(PixelSz(10),PixelSz(10),PixelSz(210),PixelSz(10),width=5,fill=WindowAccentColor)
        self.canv.create_line(PixelSz(10),PixelSz(10),PixelSz(10),PixelSz(210),width=5,fill=WindowAccentColor)

        btn_ScreenMultSizeUp = tk.Button(self,text="Größer",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(20)) +" bold",anchor="c",command=self.btn_ScreenMultSizeUp_pressed)
        btn_ScreenMultSizeDown = tk.Button(self,text="Kleiner",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(20)) +" bold",anchor="c",command=self.btn_ScreenMultSizeDown_pressed)

        btn_ScreenMultSizeUp.place(x=PixelSz(100),y=PixelSz(100),width=PixelSz(400),height=PixelSz(100))
        btn_ScreenMultSizeDown.place(x=PixelSz(100),y=PixelSz(250),width=PixelSz(400),height=PixelSz(100))

        scl_Volume = tk.Scale(self,label="Lautstärke",variable=self.VolumeVar,bg=WindowBGColor,fg=WindowAccentColor,troughcolor=WindowAccentColor,relief=tk.SOLID,from_=0,to_=100,resolution=5,orient=tk.HORIZONTAL,length=PixelSz(400),width=PixelSz(100),borderwidth=0,sliderlength=PixelSz(100),command=self.RefreshVolume)
        scl_Volume.set(self.snd_MainVol*100)
        scl_Volume.place(x=PixelSz(100),y=PixelSz(400),width=PixelSz(400),height=PixelSz(100))

        scl_Difficulty = tk.Scale(self,label="Schwierigkeit",variable=self.DiffVar,bg=WindowBGColor,fg=WindowAccentColor,troughcolor=WindowAccentColor,relief=tk.SOLID,from_=1,to_=8,resolution=1,orient=tk.HORIZONTAL,length=PixelSz(400),width=PixelSz(100),borderwidth=0,sliderlength=PixelSz(100),command=self.RefreshDiff)
        scl_Difficulty.set(self.algo_StandardSearchDepth)
        scl_Difficulty.place(x=PixelSz(100),y=PixelSz(550),width=PixelSz(400),height=PixelSz(100))

        

        self.ShowBtn_Back() 

    def InitHelpScreen(self):

        TabsStartPosX = 150
        TabsPosXDist = 600

        lbl_TitleGame1 = tk.Label(self,text="Schach",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(60)) +" bold",anchor="c")
        lbl_TitleGame1.place(x=PixelSz(TabsStartPosX + (0*TabsPosXDist)),y=PixelSz(150),width=PixelSz(500),height=PixelSz(150))

        lbl_Game1Text = tk.Label(self,text=StatsScreenTextGame1,bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(17)) +" bold",anchor="n")
        lbl_Game1Text.place(x=PixelSz(TabsStartPosX + (0*TabsPosXDist)),y=PixelSz(300),width=PixelSz(500),height=PixelSz(900))

        lbl_TitleGame2 = tk.Label(self,text="Dame",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(60)) +" bold",anchor="c")
        lbl_TitleGame2.place(x=PixelSz(TabsStartPosX + (1*TabsPosXDist)),y=PixelSz(150),width=PixelSz(500),height=PixelSz(150))

        lbl_Game2Text = tk.Label(self,text=StatsScreenTextGame2,bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(17)) +" bold",anchor="n")
        lbl_Game2Text.place(x=PixelSz(TabsStartPosX + (1*TabsPosXDist)),y=PixelSz(300),width=PixelSz(500),height=PixelSz(900))

        lbl_TitleGame3 = tk.Label(self,text="Tic-Tac-Toe",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(60)) +" bold",anchor="c")
        lbl_TitleGame3.place(x=PixelSz(TabsStartPosX + (2*TabsPosXDist)),y=PixelSz(150),width=PixelSz(500),height=PixelSz(150))
        
        lbl_Game3Text = tk.Label(self,text=StatsScreenTextGame3,bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(17)) +" bold",anchor="n")
        lbl_Game3Text.place(x=PixelSz(TabsStartPosX + (2*TabsPosXDist)),y=PixelSz(300),width=PixelSz(500),height=PixelSz(900))

        self.ShowBtn_Back() 

    def InitStatsScreen(self):
        #Datenbank.stats(self.CurrentUsername)
        TabsStartPosY = 100
        TabsPosYDist = 120

        StatsTitlesX = 100
        StatsTitlesWidth = 400
        StatsTitlesHeight = 150
        StatsTitlesFontSize = 30

        ValuesTitlesX = 500
        ValuesTitlesWidth = 400
        ValuesTitlesHeight = 150
        ValuesTitlesFontSize = 30


        DBValues = Datenbank.stats(self.CurrentUsername)
        print(str(DBValues))
        ValuesAllValues = [self.CurrentUsername,DBValues[2],DBValues[0],DBValues[1],DBValues[3]]
        if DBValues[0] != 0 or DBValues[1] != 0:
            try:
                ValuesAllValues.append(round(DBValues[0]/DBValues[1],2))
            except ZeroDivisionError:
                if DBValues[1] == 0:
                    ValuesAllValues.append(DBValues[0])
                elif DBValues[0] == 0:
                    ValuesAllValues.append(DBValues[1])
        else:
            ValuesAllValues.append(1)
        ValuesAllValues.append(DBValues[4])
            
        

        # [0, 0, 1, 0, 0, '0']
        # [wins,loses,runde,allrating,allusermoves,kimoves]

        Values1 = tk.StringVar() # Username
        Values2 = tk.StringVar() # All games
        Values3 = tk.StringVar() # Wins
        Values4 = tk.StringVar() # Loses
        Values5 = tk.StringVar() # Gesamt Punktzahl
        Values6 = tk.StringVar() # W/L (wird berechnet einfach ignorieren)
        Values7 = tk.StringVar() # Insgesamte Züge

        Values1.set(ValuesAllValues[0])
        Values2.set(str(ValuesAllValues[1]))
        Values3.set(str(ValuesAllValues[2]))
        Values4.set(str(ValuesAllValues[3]))
        Values5.set(str(ValuesAllValues[4]))
        Values6.set(str(ValuesAllValues[5]))
        Values7.set(str(ValuesAllValues[6]))



        self.canv = tk.Canvas(self,bg=WindowBGColor)

        self.canv.create_line(PixelSz(1025),PixelSz(100),PixelSz(1025),PixelSz(1000),fill=WindowAccentColor,width=10,smooth=True)
        self.canv.place(x=-5,y=-5,width=4000,height=3000)
        
        lbl_Stats1 = tk.Label(self,text="Name",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(StatsTitlesFontSize)) +" bold",anchor="nw")
        lbl_Stats1.place(x=PixelSz(StatsTitlesX),y=PixelSz(TabsStartPosY + (0*TabsPosYDist)),width=PixelSz(StatsTitlesWidth),height=PixelSz(StatsTitlesHeight))

        lbl_Stats2 = tk.Label(self,text="Insgesamte Spiele",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(StatsTitlesFontSize)) +" bold",anchor="nw")
        lbl_Stats2.place(x=PixelSz(StatsTitlesX),y=PixelSz(TabsStartPosY + (1*TabsPosYDist)),width=PixelSz(StatsTitlesWidth),height=PixelSz(StatsTitlesHeight))

        lbl_Stats3 = tk.Label(self,text="Siege",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(StatsTitlesFontSize)) +" bold",anchor="nw")
        lbl_Stats3.place(x=PixelSz(StatsTitlesX),y=PixelSz(TabsStartPosY + (2*TabsPosYDist)),width=PixelSz(StatsTitlesWidth),height=PixelSz(StatsTitlesHeight))

        lbl_Stats4 = tk.Label(self,text="Niederlagen",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(StatsTitlesFontSize)) +" bold",anchor="nw")
        lbl_Stats4.place(x=PixelSz(StatsTitlesX),y=PixelSz(TabsStartPosY + (3*TabsPosYDist)),width=PixelSz(StatsTitlesWidth),height=PixelSz(StatsTitlesHeight))

        lbl_Stats5 = tk.Label(self,text="Gesamtpunktzahl",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(StatsTitlesFontSize)) +" bold",anchor="nw")
        lbl_Stats5.place(x=PixelSz(StatsTitlesX),y=PixelSz(TabsStartPosY + (4*TabsPosYDist)),width=PixelSz(StatsTitlesWidth),height=PixelSz(StatsTitlesHeight))

        lbl_Stats6 = tk.Label(self,text="Win/Lose-Ratio",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(StatsTitlesFontSize)) +" bold",anchor="nw")
        lbl_Stats6.place(x=PixelSz(StatsTitlesX),y=PixelSz(TabsStartPosY + (5*TabsPosYDist)),width=PixelSz(StatsTitlesWidth),height=PixelSz(StatsTitlesHeight))

        lbl_Stats7 = tk.Label(self,text="Insgesamte Züge",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(StatsTitlesFontSize)) +" bold",anchor="nw")
        lbl_Stats7.place(x=PixelSz(StatsTitlesX),y=PixelSz(TabsStartPosY + (6*TabsPosYDist)),width=PixelSz(StatsTitlesWidth),height=PixelSz(StatsTitlesHeight))
        


        lbl_Values1 = tk.Label(self,textvariable=Values1,bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(ValuesTitlesFontSize)) +" bold",anchor="ne")
        lbl_Values1.place(x=PixelSz(ValuesTitlesX),y=PixelSz(TabsStartPosY + (0*TabsPosYDist)),width=PixelSz(ValuesTitlesWidth),height=PixelSz(ValuesTitlesHeight))

        lbl_Values2 = tk.Label(self,textvariable=Values2,bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(ValuesTitlesFontSize)) +" bold",anchor="ne")
        lbl_Values2.place(x=PixelSz(ValuesTitlesX),y=PixelSz(TabsStartPosY + (1*TabsPosYDist)),width=PixelSz(ValuesTitlesWidth),height=PixelSz(ValuesTitlesHeight))

        lbl_Values3 = tk.Label(self,textvariable=Values3,bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(ValuesTitlesFontSize)) +" bold",anchor="ne")
        lbl_Values3.place(x=PixelSz(ValuesTitlesX),y=PixelSz(TabsStartPosY + (2*TabsPosYDist)),width=PixelSz(ValuesTitlesWidth),height=PixelSz(ValuesTitlesHeight))

        lbl_Values4 = tk.Label(self,textvariable=Values4,bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(ValuesTitlesFontSize)) +" bold",anchor="ne")
        lbl_Values4.place(x=PixelSz(ValuesTitlesX),y=PixelSz(TabsStartPosY + (3*TabsPosYDist)),width=PixelSz(ValuesTitlesWidth),height=PixelSz(ValuesTitlesHeight))

        lbl_Values5 = tk.Label(self,textvariable=Values5,bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(ValuesTitlesFontSize)) +" bold",anchor="ne")
        lbl_Values5.place(x=PixelSz(ValuesTitlesX),y=PixelSz(TabsStartPosY + (4*TabsPosYDist)),width=PixelSz(ValuesTitlesWidth),height=PixelSz(ValuesTitlesHeight))

        lbl_Values6 = tk.Label(self,textvariable=Values6,bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(ValuesTitlesFontSize)) +" bold",anchor="ne")
        lbl_Values6.place(x=PixelSz(ValuesTitlesX),y=PixelSz(TabsStartPosY + (5*TabsPosYDist)),width=PixelSz(ValuesTitlesWidth),height=PixelSz(ValuesTitlesHeight))

        lbl_Values7 = tk.Label(self,textvariable=Values7,bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(ValuesTitlesFontSize)) +" bold",anchor="ne")
        lbl_Values7.place(x=PixelSz(ValuesTitlesX),y=PixelSz(TabsStartPosY + (6*TabsPosYDist)),width=PixelSz(ValuesTitlesWidth),height=PixelSz(ValuesTitlesHeight))
        
        
        lbl_Leaderboard12 = tk.Label(self,text=str(DBValues[6][0][1]),bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(70)) +" bold",anchor="nw")
        lbl_Leaderboard12.place(x=PixelSz(1800),y=PixelSz(300),width=PixelSz(500),height=PixelSz(100))

        lbl_Leaderboard1 = tk.Label(self,text=str(DBValues[6][0][0]),bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(70)) +" bold",anchor="ne")
        lbl_Leaderboard1.place(x=PixelSz(1200),y=PixelSz(300),width=PixelSz(500),height=PixelSz(100))

        if len(DBValues[6]) >= 2:

            lbl_Leaderboard22 = tk.Label(self,text=str(DBValues[6][1][1]),bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(50)) +" bold",anchor="nw")
            lbl_Leaderboard22.place(x=PixelSz(1810),y=PixelSz(500),width=PixelSz(500),height=PixelSz(100))

            lbl_Leaderboard2 = tk.Label(self,text=str(DBValues[6][1][0]),bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(50)) +" bold",anchor="ne")
            lbl_Leaderboard2.place(x=PixelSz(1210),y=PixelSz(500),width=PixelSz(500),height=PixelSz(100))

        if len(DBValues[6]) >= 3:

            lbl_Leaderboard32 = tk.Label(self,text=str(DBValues[6][2][1]),bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(30)) +" bold",anchor="nw")
            lbl_Leaderboard32.place(x=PixelSz(1820),y=PixelSz(700),width=PixelSz(500),height=PixelSz(100))

            lbl_Leaderboard3 = tk.Label(self,text=str(DBValues[6][2][0]),bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(30)) +" bold",anchor="ne")
            lbl_Leaderboard3.place(x=PixelSz(1200),y=PixelSz(700),width=PixelSz(500),height=PixelSz(100))



        self.ShowBtn_Back()

        
        
        pass

    def InitCreditsScreen(self):
        
        self.creds = Image.open(CreditsPic)
        self.creds = self.creds.resize((PixelSz(1280),PixelSz(720)))
        self.Credits = ImageTk.PhotoImage(self.creds)

        btn_secret = tk.Button(self,text="Geheim Knopf",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(10)) +" bold",anchor="c",command=self.btn_super_secret_button_pressed)
        btn_secret.place(x=PixelSz(1900),y=PixelSz(1100),width=PixelSz(100),height=PixelSz(25))

        lbl_credits = tk.Label(self,image=self.Credits)
        lbl_credits.place(x=PixelSz(400),y=PixelSz(200),width=PixelSz(1280),height=PixelSz(720))

        
        self.ShowBtn_Back()

    def InitRegisterScreen(self):
        self.ShowBtn_Back()

        self.EmailSend = False
        self.EmailCodeCorrect = False

        self.RegisterUsername = tk.StringVar()
        self.RegisterPassword = tk.StringVar()
        self.RegisterConfirmPassword = tk.StringVar()
        self.RegisterEmail = tk.StringVar()
        

        lbl_Username = tk.Label(self,text="Nutzername:",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(13)) +" bold",anchor="nw")
        lbl_Username.place(x=PixelSz(800),y=PixelSz(150),width=PixelSz(200),height=PixelSz(50))

        lbl_Password = tk.Label(self,text="Passwort:",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(13)) +" bold",anchor="nw")
        lbl_Password.place(x=PixelSz(800),y=PixelSz(300),width=PixelSz(200),height=PixelSz(50))

        lbl_PasswordConfirm = tk.Label(self,text="Passwort Bestätigen:",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(13)) +" bold",anchor="nw")
        lbl_PasswordConfirm.place(x=PixelSz(800),y=PixelSz(450),width=PixelSz(200),height=PixelSz(50))

        lbl_PasswordConfirm = tk.Label(self,text="E-Mail Adresse:",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(13)) +" bold",anchor="nw")
        lbl_PasswordConfirm.place(x=PixelSz(800),y=PixelSz(600),width=PixelSz(200),height=PixelSz(50))



        self.txt_RegisterUsername = tk.Entry(self,textvariable=self.RegisterUsername,bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(25)) +" bold")
        self.txt_RegisterUsername.place(x=PixelSz(800),y=PixelSz(175),width=PixelSz(400),height=PixelSz(75))

        self.txt_RegisterPassword = tk.Entry(self,textvariable=self.RegisterPassword,bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(25)) +" bold",show="*")
        self.txt_RegisterPassword.place(x=PixelSz(800),y=PixelSz(325),width=PixelSz(400),height=PixelSz(75))  

        self.txt_RegisterConfirmPassword = tk.Entry(self,textvariable=self.RegisterConfirmPassword,bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(25)) +" bold",show="*")
        self.txt_RegisterConfirmPassword.place(x=PixelSz(800),y=PixelSz(475),width=PixelSz(400),height=PixelSz(75))  

        self.txt_RegisterEmail = tk.Entry(self,textvariable=self.RegisterEmail,bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(25)) +" bold")
        self.txt_RegisterEmail.place(x=PixelSz(800),y=PixelSz(625),width=PixelSz(400),height=PixelSz(75))  



        self.btn_RegisterSubmit = tk.Button(self,text="Registrieren",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(20)) +" bold",anchor="c",command=self.btn_RegisterSubmit_Pressed)
        self.btn_RegisterSubmit.place(x=PixelSz(800),y=PixelSz(900),width=PixelSz(400),height=PixelSz(100))
        

        self.txt_RegisterPassword.bind("<KeyRelease>",self.RegisterPWKey)
        self.txt_RegisterConfirmPassword.bind("<KeyRelease>",self.RegisterPWKey)
        pass



    def ClearCanv(self):
        """Leert alle Tkinter.Canvas Elemente"""
        self.CurrentGame = 0
        self.lastfield = []
        self.newfield = []
        self.NewCoords = []
        self.lastPos = []
        self.playfield_Coords = []
        self.Playfield_Current = []
        #print(sys.getrefcount(playfield_startPosGame1))
        self.canv.delete("all")
        #self.canv.delete("bauerW")
        #self.canv.delete("bauerS")

    def ClearFrame(self):
        """leert alle Tkinter Elemente (Canvas mit eingeschlossen)"""
        for child in self.winfo_children():
            child.destroy()

    def ShowBtn_Back(self):
        """führt zurück ins hauptmenu"""
        self.btn_back = tk.Button(self,text="Zurück..",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(20)) +" bold",anchor="c",command=self.btn_back_pressed)
        self.btn_back.place(x=PixelSz(50),y=PixelSz(975),width=PixelSz(200),height=PixelSz(100))

    def ShowBtn_Sure_Back(self):
        self.btn_backs = tk.Button(self,text="Zurück..",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(20)) +" bold",anchor="c",command=self.btn_back_sure_pressed1)
        self.btn_backs.place(x=PixelSz(50),y=PixelSz(975),width=PixelSz(200),height=PixelSz(100))


    def PlaySound(self,sound):
        """Funktion zum abspielen von Sounds durch angabe von sound(str)\n
        Möglichkeiten für Sound:\n
        charup,chardown,charkill,pop,voltick,win,lose
        """
        if sound == "charup":
            self.snd_CharUp = pygame.mixer.music.load(snd_CharUp)
            pygame.mixer.music.set_volume(self.snd_MainVol)
            pygame.mixer.music.play(0)

        elif sound == "chardown":
            self.snd_CharDown = pygame.mixer.music.load(snd_CharDown)
            pygame.mixer.music.set_volume(self.snd_MainVol)
            pygame.mixer.music.play(0)

        elif sound == "charkill":
            self.snd_CharKill = pygame.mixer.music.load(snd_CharKill)
            pygame.mixer.music.set_volume(self.snd_MainVol)
            pygame.mixer.music.play(0)
        
        elif sound == "pop":
            self.snd_pop = pygame.mixer.music.load(snd_pop)
            pygame.mixer.music.set_volume(self.snd_MainVol)
            pygame.mixer.music.play(0)

        elif sound == "voltick":
            self.snd_VolTick = pygame.mixer.music.load(snd_VolTick)
            pygame.mixer.music.set_volume(self.snd_MainVol)
            pygame.mixer.music.play(0)

        elif sound == "win":
            self.snd_win = pygame.mixer.music.load(snd_win)
            pygame.mixer.music.set_volume(self.snd_MainVol)
            pygame.mixer.music.play(0)

        elif sound == "lose":
            self.snd_lose = pygame.mixer.music.load(snd_lose)
            pygame.mixer.music.set_volume(self.snd_MainVol)
            pygame.mixer.music.play(0)

    def RefreshVolume(self,event):
        """wird zum erneuern der lautstärke genutzt"""
        self.snd_MainVol = (self.VolumeVar.get() / 100)
        self.PlaySound("voltick")

    def RefreshDiff(self,event):
        """wird zum erneuern des schwierigkeitsgrads genutzt"""
        self.algo_StandardSearchDepth = self.DiffVar.get()
        self.PlaySound("voltick")

    def CreatePlayField(self):
        """zeichnet NUR das spielfeld"""

        self.playfield_startx = copy.deepcopy(PixelSz(playfield_startx))
        self.playfield_distx = copy.deepcopy(PixelSz(playfield_distx))
        self.playfield_starty = copy.deepcopy(PixelSz(playfield_starty))
        self.playfield_disty = copy.deepcopy(PixelSz(playfield_disty))

        self.playfield_Coords = []
        playfieldyCache = []
        self.canv = tk.Canvas(self,bg=WindowBGColor)#,highlightcolor=WindowBGColor)
        toskip = False
        rowtype = True
        
        for y in range(playfield_size):
            for x in range(playfield_size):
                if toskip == True:
                    toskip = False
                else:
                    self.canv.create_rectangle(self.playfield_startx + (x * self.playfield_distx)+2,self.playfield_starty + (y * self.playfield_disty)+2,self.playfield_startx + (x * self.playfield_distx)+self.playfield_distx-2,self.playfield_starty + (y * self.playfield_disty)+self.playfield_disty-2,fill=WindowAccentColor,tags="playfield")
                    toskip = True
            if rowtype == True:
                rowtype = False
                toskip = True
            else:
                rowtype = True
                toskip = False

        for x in range(playfield_size + 1):
            self.canv.create_line(self.playfield_startx,self.playfield_starty + (x * self.playfield_disty),self.playfield_startx + (playfield_size * self.playfield_distx),self.playfield_starty + (x * self.playfield_disty),fill=WindowAccentColor,width=3,tags="playfield")

        for x in range(playfield_size + 1):
            self.canv.create_line(self.playfield_startx + (x * self.playfield_distx),self.playfield_starty,self.playfield_startx + (x * self.playfield_distx),self.playfield_starty + (playfield_size * self.playfield_disty),fill=WindowAccentColor,width=3,tags="playfield")
        
        


        for y in range(playfield_size):
            for x in range(playfield_size):
                playfieldyCache.append([self.playfield_startx+(self.playfield_distx/2)+(x * self.playfield_distx),self.playfield_starty+(self.playfield_disty/2)+(y * self.playfield_disty)])
            
            self.playfield_Coords.append(playfieldyCache)
            playfieldyCache = []
        

        self.ShowBtn_Sure_Back()

    def CheckLoggedIn(self):
        if self.LoggedIn == True:
            self.txt_LoginUsername.config(state=DISABLED)
            self.txt_LoginPassword.config(state=DISABLED)
            self.btn_LoginSubmit.config(state=DISABLED)
            self.btn_LoginRegister.config(state=DISABLED)
            self.btn_LoginGuest.config(state=DISABLED)

            self.btn_play.config(state=NORMAL)
            self.btn_stats.config(state=NORMAL)

        elif self.LoggedIn == False:
            self.btn_play.config(state=DISABLED)
            self.btn_stats.config(state=DISABLED)

            self.txt_LoginUsername.config(state=NORMAL)
            self.txt_LoginPassword.config(state=NORMAL)
            self.btn_LoginSubmit.config(state=NORMAL)
            self.btn_LoginRegister.config(state=NORMAL)
            self.btn_LoginGuest.config(state=NORMAL)

        if self.CurrentUsername == "gast":
            self.btn_stats.config(state=DISABLED)

    def Validation_Move(self):
        """hauptfunktion zum überprüfen des spielzuges"""
        self.ValidMove = False
        self.AvailablePositions = []
        self.lastfield = []
        self.newfield = []
        self.KilledEnemyField = []
        self.Validation_GetNearestField()
        self.AvailablePositions = self.Validation_GetAvailablePos()
        

        #if len(self.AvailablePositions) <= 0:
            #self.Validation_KiWin()
            #return

        for field in self.AvailablePositions:
            if self.newfield == field:
                self.ValidMove = True

        if self.ValidMove == False:
            self.canv.coords(self.DragObj,self.lastPos[0],self.lastPos[1])
        elif self.ValidMove == True:
            self.StatsMoves += 1
            self.canv.coords(self.DragObj,self.NewCoords[0],self.NewCoords[1])

            if self.CurrentGame == 1:
                if self.Playfield_Current[self.newfield[1]][self.newfield[0]] == 1:
                    self.PlaySound("charkill")
                self.Playfield_Current[self.newfield[1]][self.newfield[0]] = 2
                self.Playfield_Current[self.lastfield[1]][self.lastfield[0]] = 0
                self.canv.delete("char")
                self.canv.delete("waydot")
                self.CurrentMove = False
                self.Game1SetPlayer()
                self.master.update()
                RowI = -1
                CellI = -1

                AmountUserChars = 0
                AmountKiChars = 0

                for row in self.Playfield_Current:
                    RowI += 1

                    for cell in row:
                        CellI += 1
                        if RowI == 0:
                            if cell == 2:
                                self.Validation_UserWin()
                                return
                                #break
                        
                        if cell == 2:
                            
                            AmountUserChars += 1
                            self.UserChars = AmountUserChars

                        if cell == 1:
                            AmountKiChars += 1
                            self.KiChars = AmountKiChars
                if AmountKiChars <= 0:
                    self.Validation_UserWin()
                    return
                elif AmountUserChars <=0:
                    self.Validation_KiWin()
                    return

                

                BeforeKiMovePlayfield_Current = copy.deepcopy(self.Playfield_Current)

                self.PlayerKill = False

                self.Validation_BlackMove()

                RowI = -1
                CellI = -1

                AmountUserChars = 0
                AmountKiChars = 0

                for row in self.Playfield_Current:
                    RowI += 1

                    for cell in row:
                        CellI += 1
                        if RowI == len(self.Playfield_Current)-1:
                            if cell == 1:
                                self.Validation_KiWin()
                                return

                        if cell == 2:
                            AmountUserChars += 1

                        elif cell == 1:
                            AmountKiChars += 1

                if AmountKiChars <= 0:
                    self.Validation_UserWin()
                    return
                elif AmountUserChars <=0:
                    self.Validation_KiWin()
                    return
                if BeforeKiMovePlayfield_Current == self.Playfield_Current:
                    self.Validation_UserWin()
                    return
                elif self.PlayerKill == False:
                    self.PlaySound("chardown")

                TotalAvailableMoves_User = []

                for lastfieldy in range(0,len(self.Playfield_Current)):
                    for lastfieldx in range(0,len(self.Playfield_Current[lastfieldy])):
                        if self.Playfield_Current[lastfieldy][lastfieldx] == 2:
                            self.lastfield= [lastfieldx,lastfieldy]
                            poses = self.Validation_GetAvailablePos()
                            if len(poses) >= 1:
                                TotalAvailableMoves_User.append(self.Validation_GetAvailablePos())

                if len(TotalAvailableMoves_User) <= 0:
                    self.Validation_KiWin()
                    return
                
            elif self.CurrentGame == 2:
                self.Playfield_Current[self.newfield[1]][self.newfield[0]] = 2
                self.Playfield_Current[self.lastfield[1]][self.lastfield[0]] = 0

                if len(self.KilledEnemyField) == 0:
                    pass
                elif len(self.KilledEnemyField) == 1:
                    self.Playfield_Current[self.KilledEnemyField[0][1]][self.KilledEnemyField[0][0]] = 0
                    self.PlaySound("charkill")
                else:
                    if self.newfield[0] <= self.lastfield[0]:
                        self.Playfield_Current[self.KilledEnemyField[0][1]][self.KilledEnemyField[0][0]] = 0
                        self.PlaySound("charkill")
                    else:
                        self.Playfield_Current[self.KilledEnemyField[1][1]][self.KilledEnemyField[1][0]] = 0
                        self.PlaySound("charkill")
                
                self.canv.delete("char")
                self.canv.delete("waydot")
                self.CurrentMove = False
                self.Game2SetPlayer()
                self.master.update()

                RowI = -1
                CellI = -1

                AmountUserChars = 0
                AmountKiChars = 0

                for row in self.Playfield_Current:
                    RowI += 1

                    for cell in row:
                        CellI += 1
                        if RowI == 0:
                            if cell == 2:
                                self.Validation_UserWin()
                                return
                                #break
                        
                        if cell == 2:
                            AmountUserChars += 1

                        if cell == 1:
                            AmountKiChars += 1
                if AmountKiChars <= 0:
                    self.Validation_UserWin()
                    return
                elif AmountUserChars <=0:
                    self.Validation_KiWin()
                    return

                BeforeKiMovePlayfield_Current = copy.deepcopy(self.Playfield_Current)

                self.PlayerKill = False

                self.Validation_BlackMove()

                RowI = -1
                CellI = -1

                AmountUserChars = 0
                AmountKiChars = 0

                for row in self.Playfield_Current:
                    RowI += 1

                    for cell in row:
                        CellI += 1
                        if RowI == len(self.Playfield_Current)-1:
                            if cell == 1:
                                self.Validation_KiWin()
                                return

                        if cell == 2:
                            AmountUserChars += 1

                        elif cell == 1:
                            AmountKiChars += 1

                if AmountKiChars <= 0:
                    self.Validation_UserWin()
                    return
                elif AmountUserChars <=0:
                    self.Validation_KiWin()
                    return
                if BeforeKiMovePlayfield_Current == self.Playfield_Current:
                    self.Validation_UserWin()
                    return
                elif self.PlayerKill == False:
                    self.PlaySound("chardown")

                TotalAvailableMoves_User = []
                for lastfieldy in range(0,len(self.Playfield_Current)):
                    for lastfieldx in range(0,len(self.Playfield_Current[lastfieldy])):
                        if self.Playfield_Current[lastfieldy][lastfieldx] == 2:
                            self.lastfield= [lastfieldx,lastfieldy]
                            poses = self.Validation_GetAvailablePos()
                            if len(poses) >= 1:
                                TotalAvailableMoves_User.append(self.Validation_GetAvailablePos())
                
                if len(TotalAvailableMoves_User) <= 0:
                    self.Validation_KiWin()
                    return

        else:
            raise Exception("Invalid Valid ... LOl")
        self.lastPos = (0,0)
        self.DragObj = ""
        self.canv.delete("waydot")
    
    def Validation_GetAvailablePos(self):
        """findet die möglichen züge für einen bestimmten spielcharakter"""
        OutArr = []
        self.KilledEnemyField = []

        self.wydt = Image.open(waydot)
        self.wydt = self.wydt.resize((PixelSz(CharSize),PixelSz(CharSize)))
        self.waydot = ImageTk.PhotoImage(self.wydt)

        if self.CurrentGame == 1:
            if self.lastfield[0] > 0:
                if self.Playfield_Current[self.lastfield[1]-1][self.lastfield[0]-1] == 1:
                    self.canv.create_image(self.playfield_Coords[self.lastfield[1]-1][self.lastfield[0]-1][0],self.playfield_Coords[self.lastfield[1]-1][self.lastfield[0]-1][1],image=self.waydot,tags="waydot")
                    OutArr.append([self.lastfield[0]-1,self.lastfield[1]-1])

            if self.lastfield[0] < playfield_size-1:
                if self.Playfield_Current[self.lastfield[1]-1][self.lastfield[0]+1] == 1:
                    self.canv.create_image(self.playfield_Coords[self.lastfield[1]-1][self.lastfield[0]+1][0],self.playfield_Coords[self.lastfield[1]-1][self.lastfield[0]+1][1],image=self.waydot,tags="waydot")
                    OutArr.append([self.lastfield[0]+1,self.lastfield[1]-1])


            
            if self.Playfield_Current[self.lastfield[1]-1][self.lastfield[0]] == 0:
                self.canv.create_image(self.playfield_Coords[self.lastfield[1]-1][self.lastfield[0]][0],self.playfield_Coords[self.lastfield[1]-1][self.lastfield[0]][1],image=self.waydot,tags="waydot")
                OutArr.append([self.lastfield[0],self.lastfield[1]-1])
        
        elif self.CurrentGame == 2:

            if self.lastfield[0] > 1:
                if self.Playfield_Current[self.lastfield[1]-2][self.lastfield[0]-2] == 0:
                    if self.Playfield_Current[self.lastfield[1]-1][self.lastfield[0]-1] == 1:
                        self.KilledEnemyField.append([self.lastfield[0]-1,self.lastfield[1]-1])
                        self.canv.create_image(self.playfield_Coords[self.lastfield[1]-2][self.lastfield[0]-2][0],self.playfield_Coords[self.lastfield[1]-2][self.lastfield[0]-2][1],image=self.waydot,tags="waydot")
                        OutArr.append([self.lastfield[0]-2,self.lastfield[1]-2])
                
                """if self.lastfield[0] < playfield_size-2:
                    if self.Playfield_Current[self.lastfield[1]+2][self.lastfield[0]-2] == 0:
                        if self.Playfield_Current[self.lastfield[1]-1][self.lastfield[0]+1] == 1:
                            self.KilledEnemyField.append([self.lastfield[0]-1,self.lastfield[1]-1])
                            #self.canv.create_image(self.playfield_Coords[self.lastfield[1]-2][self.lastfield[0]-2][0],self.playfield_Coords[self.lastfield[1]-2][self.lastfield[0]-2][1],image=self.waydot,tags=("waydot"))
                            OutArr.append([self.lastfield[0]-2,self.lastfield[1]+2])"""
                    

            if self.lastfield[0] < playfield_size-2:
                if self.Playfield_Current[self.lastfield[1]-2][self.lastfield[0]+2] == 0:
                    if self.Playfield_Current[self.lastfield[1]-1][self.lastfield[0]+1] == 1:
                        self.KilledEnemyField.append([self.lastfield[0]+1,self.lastfield[1]-1])
                        self.canv.create_image(self.playfield_Coords[self.lastfield[1]-2][self.lastfield[0]+2][0],self.playfield_Coords[self.lastfield[1]-2][self.lastfield[0]+2][1],image=self.waydot,tags="waydot")
                        OutArr.append([self.lastfield[0]+2,self.lastfield[1]-2])

            if len(OutArr) == 0:

                if self.lastfield[0] > 0:
                    if self.Playfield_Current[self.lastfield[1]-1][self.lastfield[0]-1] == 0:
                        self.canv.create_image(self.playfield_Coords[self.lastfield[1]-1][self.lastfield[0]-1][0],self.playfield_Coords[self.lastfield[1]-1][self.lastfield[0]-1][1],image=self.waydot,tags="waydot")
                        OutArr.append([self.lastfield[0]-1,self.lastfield[1]-1])

                if self.lastfield[0] < playfield_size-1:
                    if self.Playfield_Current[self.lastfield[1]-1][self.lastfield[0]+1] == 0:
                        self.canv.create_image(self.playfield_Coords[self.lastfield[1]-1][self.lastfield[0]+1][0],self.playfield_Coords[self.lastfield[1]-1][self.lastfield[0]+1][1],image=self.waydot,tags="waydot")
                        OutArr.append([self.lastfield[0]+1,self.lastfield[1]-1])

        elif self.CurrentGame == 3:
            pass
        else:
            pass
        return OutArr
        
    def Validation_GetNearestField(self):
        """findet das nächste spielfeld anhand der coordinaten des aktuell bewegten objekts"""
        ObjX = self.canv.coords(self.DragObj)[0]
        ObjY = self.canv.coords(self.DragObj)[1]
        for y in range(0,len(self.playfield_Coords)):
            for x in range(0,len(self.playfield_Coords[y])):
                if ObjX >= self.playfield_Coords[y][x][0]-playfield_FindFieldTolerance and ObjX <= self.playfield_Coords[y][x][0]+playfield_FindFieldTolerance and ObjY >= self.playfield_Coords[y][x][1] - playfield_FindFieldTolerance and ObjY <= self.playfield_Coords[y][x][1]+playfield_FindFieldTolerance:
                    #self.ValidMove = True
                    self.NewCoords = [self.playfield_Coords[y][x][0],self.playfield_Coords[y][x][1]]
                    self.newfield = [x,y]
                
                if self.lastPos[0] >= self.playfield_Coords[y][x][0]-playfield_FindFieldTolerance and self.lastPos[0] <= self.playfield_Coords[y][x][0]+playfield_FindFieldTolerance and self.lastPos[1] >= self.playfield_Coords[y][x][1] - playfield_FindFieldTolerance and self.lastPos[1] <= self.playfield_Coords[y][x][1]+playfield_FindFieldTolerance:
                    self.lastfield = [x,y]
                else:
                    pass
                    #self.ValidMove = False
    
    def Validation_CurrentFieldArr(self):
        """findet das feld ab welchem der spielcharakter gezogen wird"""
        for y in range(0,len(self.playfield_Coords)):
            for x in range(0,len(self.playfield_Coords[y])):
                if self.lastPos[0] >= self.playfield_Coords[y][x][0]-playfield_FindFieldTolerance and self.lastPos[0] <= self.playfield_Coords[y][x][0]+playfield_FindFieldTolerance and self.lastPos[1] >= self.playfield_Coords[y][x][1] - playfield_FindFieldTolerance and self.lastPos[1] <= self.playfield_Coords[y][x][1]+playfield_FindFieldTolerance:
                    self.lastfield = [x,y]

    def Validation_BlackMove(self):
        """wird zum ausführen des zuges von der ki genutzt"""
        os.system("cls")
        self.Playfield_Last = copy.deepcopy(self.Playfield_Current)
        if runWithAlgo == True:
            self.Playfield_Current =  runAlgorithm(self.CurrentGame,self.Playfield_Current,self.algo_StandardSearchDepth)[0]


        self.canv.delete("char")
        self.CurrentMove = True
        self.StatsKiMoves += 1
        
        if self.Playfield_Current == None:
            self.Playfield_Current = copy.deepcopy(self.Playfield_Last)

        firstRun = 0
        secondRun = 0

        for i in self.Playfield_Current:
            for j in i:
                if j == 2:
                    firstRun += 1

        for i in self.Playfield_Last:
            for j in i:
                if j == 2:
                    secondRun += 1
        if firstRun < secondRun:
            self.PlayerKill = True
            self.PlaySound("charkill")


        if self.CurrentGame == 1:
            self.Game1SetPlayer()

        elif self.CurrentGame == 2:
            self.Game2SetPlayer()
        #self.CurrentMove = True

    def Validation_UserWin(self):
        """spieler hat gewonnen"""
        self.master.update()
        self.Validation_ShowEnd("win")

    def Validation_KiWin(self):
        """spieler hat verloren"""
        self.master.update()
        self.Validation_ShowEnd("lose")

    def Validation_ShowEnd(self,EndGameType):
        """zeigt den gewinn/verlier "screen" an"""
        self.btn_backs.destroy()

        TotalStartEnemys = 6
        TotalStartPlayers = 6

        leftEnemys = 0
        leftPlayers = 0
        for i in self.Playfield_Current:
            for cell in i:
                if cell == 1:
                    leftEnemys += 1
                if cell == 2:
                    leftPlayers += 1

        if EndGameType == "win":
            self.StatsPunkte = 10
            self.StatsKiPunkte = -10
        
        elif EndGameType == "lose":
            self.StatsPunkte = -10
            self.StatsKiPunkte = 10

        #enemyDiff = (TotalStartEnemys-leftEnemys)
        self.StatsPunkte = (self.StatsPunkte + (TotalStartEnemys-leftEnemys))*self.algo_StandardSearchDepth - (TotalStartPlayers-leftPlayers)
        self.StatsMoves = self.StatsMoves
        self.StatsKiPunkte = (self.StatsKiPunkte + (TotalStartPlayers-leftPlayers))*self.algo_StandardSearchDepth - (TotalStartEnemys - leftEnemys)

        OutStatsPunkte = StringVar()
        OutStatsPunkte.set(str(self.StatsPunkte))

        OutStatsMoves = StringVar()
        OutStatsMoves.set(str(self.StatsMoves))

        EndScreenPosx = 670
        EndScreenPosY = 300

        EndScreenPosx2 = 1370
        EndScreenPosY2 = 800

        ShadowOverlap = 8

        WinOrLoseText = tk.StringVar()

        self.canv.create_rectangle(PixelSz(EndScreenPosx)+ShadowOverlap*2,PixelSz(EndScreenPosY)+ShadowOverlap*2,PixelSz(EndScreenPosx2)+ShadowOverlap,PixelSz(EndScreenPosY2)+ShadowOverlap,fill="black")#,outline=WindowAccentColor,width=1)
        self.canv.create_rectangle(PixelSz(EndScreenPosx),PixelSz(EndScreenPosY),PixelSz(EndScreenPosx2),PixelSz(EndScreenPosY2),fill=WindowAccentColor)
        
        if EndGameType == "win":
            pass
            Datenbank.winOrDefeat(self.CurrentUsername,True,self.StatsPunkte,self.StatsKiPunkte,self.StatsMoves,self.StatsKiMoves,self.algo_StandardSearchDepth,self.algo_StandardSearchDepth)
        
        elif EndGameType == "lose":
            pass
            Datenbank.winOrDefeat(self.CurrentUsername,False,self.StatsPunkte,self.StatsKiPunkte,self.StatsMoves,self.StatsKiMoves,self.algo_StandardSearchDepth,self.algo_StandardSearchDepth)

        pass

        if EndGameType == "win":
            self.wpic = Image.open(WinPic)
            self.wpic = self.wpic.resize((PixelSz(201),PixelSz(182)))
            self.winPic = ImageTk.PhotoImage(self.wpic)
            self.canv.create_image(PixelSz(1025),PixelSz(400),image=self.winPic,tags="winscrn")
            WinOrLoseText.set("Gewonnen!")

        elif EndGameType == "lose":

            self.lpic = Image.open(LosePic)
            self.lpic = self.lpic.resize((PixelSz(96),PixelSz(145)))
            self.losepic = ImageTk.PhotoImage(self.lpic)
            self.canv.create_image(PixelSz(1025),PixelSz(400),image=self.losepic,tags="losescrn")
            WinOrLoseText.set("Verloren!")
        
        lbl_WinOrLose = tk.Label(self,textvariable=WinOrLoseText,bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(40)) +" bold",anchor="c")
        lbl_WinOrLose.place(x=PixelSz(825),y=PixelSz(500),width=PixelSz(400),height=PixelSz(50))

        btn_EndBack = tk.Button(self,text="Zurück",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(20)) +" bold",command=self.btn_back_pressed)
        btn_EndBack.place(x=PixelSz(700),y=PixelSz(710),width=PixelSz(200),height=PixelSz(50))

        btn_Again = tk.Button(self,text="Nochmal",bg=WindowBGColor,fg=WindowAccentColor,font="Rockwell " + str(PixelSz(20)) +" bold",command=self.btn_Game1_pressed)
        btn_Again.place(x=PixelSz(1150),y=PixelSz(710),width=PixelSz(200),height=PixelSz(50))


        lbl_EndMovesVal = tk.Label(self,textvariable=OutStatsMoves,bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(30)) +" bold",anchor="c")
        lbl_EndMovesVal.place(x=PixelSz(860),y=PixelSz(620),width=PixelSz(100),height=PixelSz(40))

        lbl_EndPunkteVal = tk.Label(self,textvariable=OutStatsPunkte,bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(30)) +" bold",anchor="c")
        lbl_EndPunkteVal.place(x=PixelSz(1070),y=PixelSz(620),width=PixelSz(100),height=PixelSz(40))

        lbl_EndMoves = tk.Label(self,text="Züge",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(20)) +" bold",anchor="nw")
        lbl_EndMoves.place(x=PixelSz(875),y=PixelSz(575),width=PixelSz(100),height=PixelSz(40))

        lbl_EndPunkte = tk.Label(self,text="Punkte",bg=WindowAccentColor,fg=WindowBGColor,font="Rockwell " + str(PixelSz(20)) +" bold",anchor="nw")
        lbl_EndPunkte.place(x=PixelSz(1075),y=PixelSz(575),width=PixelSz(100),height=PixelSz(40))

        self.master.update()
        if EndGameType == "win":
            self.PlaySound("win")
        else:
            self.PlaySound("lose")

    def EmailValidation(self):
        """wird vielleicht in der end version nicht mehr da sein, wird aber hoffentlich zur email verifizierung genutzt"""
        #self.EmailCodeCorrect = False
        #self.emailCode = random.randint(1111,9999)
        #port = 465
        #emailusername = "chessprototypebyanjd@gmail.com"
        #emailpassword = "HHBK1234"
        #message = """
        #Der Code fuer die Email Verifizierung ist : """+str(self.emailCode)

        #sslcontext = ssl.create_default_context()

        #with smtplib.SMTP_SSL("smtp.gmail.com",port,context=sslcontext) as server:
        #    server.login(emailusername,emailpassword)
        #    server.sendmail(emailusername,self.RegisterEmail.get(),message)
        #pass
        #self.EmailSend = True

    def EmailValidation_CheckCode(self):
        """wird auch hoffentlich zum überprüfen des verifizierungs codes genutzt"""
        self.master.update()
        #print(str(self.txt_Code.get()) +" | "+ str(self.emailCode))
        

    def OnPressDrag(self,event):
        """wird ausgeführt wenn man auf einen weißen bauern oder puc klickt"""
        self.canv.delete("waydot")
        self.DragObj = self.canv.find_closest(event.x,event.y)
        self.lastPos = self.canv.coords(self.DragObj)
        self.PlaySound("charup")
        self.Validation_CurrentFieldArr()
        self.AvailablePositions = self.Validation_GetAvailablePos()
        
    def OnMoveDrag(self,event):
        """wird ausgeführt wenn man versucht einen weißen bauern oder puc zu ziehen"""
        self.canv.coords(self.DragObj,event.x,event.y)
        self.canv.addtag_withtag("dragged",self.DragObj)
        self.canv.tag_raise("dragged")

    def OnReleaseDrag(self,event):
        """wird ausgeführt wann man die maustaste wiede loslässt, abhängig von OnPressDrag und OnMoveDrag"""
        self.canv.dtag(self.DragObj,"dragged")
        self.canv.delete("waydot")
        self.master.update()
        self.PlaySound("chardown")
        self.Validation_Move()

    def RegisterPWKey(self,event):
        """vergleicht die beiden passwörter ob sie identisch sind"""
        if self.RegisterPassword.get() == self.RegisterConfirmPassword.get():
            self.PasswordConfirm = True
            #print(self.RegisterPassword.get() + self.RegisterConfirmPassword.get())
        #elif self.RegisterPassword.get() == "" or self.RegisterConfirmPassword.get() == "":
        #    self.PasswordConfirm = True
        else:
            self.PasswordConfirm = False

        if self.PasswordConfirm == True:
            self.txt_RegisterConfirmPassword.config(bg=WindowAccentColor)
            self.txt_RegisterPassword.config(bg=WindowAccentColor)
            #if Datenbank.CheckCredentialsDB(self.Username, self.PasswordHash, False) == True:
            #   pass
            #else:
            #   pass
            pass
        else:
            self.txt_RegisterConfirmPassword.config(bg='#FF0000')
            self.txt_RegisterPassword.config(bg='#FF0000')

    def InitGame1(self):
        """initialisiert das Spiel 1 nachdem das feld erstellt wurde"""
        self.bpicW = Image.open(bauerpicW)
        self.bpicW = self.bpicW.resize((PixelSz(CharSize),PixelSz(CharSize)))
        self.bauerpicW = ImageTk.PhotoImage(self.bpicW)
        
        self.bpicS = Image.open(bauerpicS)
        self.bpicS = self.bpicS.resize((PixelSz(CharSize),PixelSz(CharSize)))
        self.bauerpicS = ImageTk.PhotoImage(self.bpicS)

        self.Game1SetPlayer()

        self.canv.place(x=-5,y=-5,width=PixelSz(4000),height=PixelSz(3000))
        
    def InitGame2(self):
        """initialisiert das Spiel 1 nachdem das feld erstellt wurde"""
        self.pcpicS = Image.open(pucpicS)
        self.pcpicS = self.pcpicS.resize((PixelSz(CharSize),PixelSz(CharSize)))
        self.pucpicS = ImageTk.PhotoImage(self.pcpicS)

        self.pcpicW = Image.open(pucpicW)
        self.pcpicW = self.pcpicW.resize((PixelSz(CharSize),PixelSz(CharSize)))
        self.pucpicW = ImageTk.PhotoImage(self.pcpicW)

        self.Game2SetPlayer()

        self.canv.place(x=-5,y=-5,width=PixelSz(4000),height=PixelSz(3000))
        #self.canv.configure()
        


    def Game1SetPlayer(self):
        """erstellt die bilder bzw spielcharaktäre von spiel 1 nachdem es initialisiert wurde"""
        self.canv.tag_unbind("bauerW","<Button-1>")
        self.canv.tag_unbind("bauerW","<B1-Motion>")
        self.canv.tag_unbind("bauerW","<ButtonRelease-1>")

        for row in range(0,len(self.Playfield_Current)):
            for cell in range(0,len(self.Playfield_Current[row])):
                if self.Playfield_Current[row][cell] == 1:
                    self.canv.create_image(self.playfield_Coords[row][cell][0],self.playfield_Coords[row][cell][1],image=self.bauerpicS,tags=("bauerS","char"))
                elif self.Playfield_Current[row][cell] == 2:
                    self.canv.create_image(self.playfield_Coords[row][cell][0],self.playfield_Coords[row][cell][1],image=self.bauerpicW,tags=("bauerW","char"))
                else:
                    pass
        if self.CurrentMove != False or self.StatsMoves == 0:
            self.canv.tag_bind("bauerW","<Button-1>",self.OnPressDrag)
            self.canv.tag_bind("bauerW","<B1-Motion>",self.OnMoveDrag)
            self.canv.tag_bind("bauerW","<ButtonRelease-1>",self.OnReleaseDrag)

    def Game2SetPlayer(self):
        """erstellt die bilder bzw spielcharaktäre von spiel 1 nachdem es initialisiert wurde"""
        self.canv.tag_unbind("pucW","<Button-1>")
        self.canv.tag_unbind("pucW","<B1-Motion>")
        self.canv.tag_unbind("pucW","<ButtonRelease-1>")
        for row in range(0,len(self.Playfield_Current)):
            for cell in range(0,len(self.Playfield_Current[row])):
                if self.Playfield_Current[row][cell] == 1:
                    self.canv.create_image(self.playfield_Coords[row][cell][0],self.playfield_Coords[row][cell][1],image=self.pucpicS,tags=("pucS","char"))
                elif self.Playfield_Current[row][cell] == 2:
                    self.canv.create_image(self.playfield_Coords[row][cell][0],self.playfield_Coords[row][cell][1],image=self.pucpicW,tags=("pucW","char"))
                else:
                    pass
        if self.CurrentMove != False:
            self.canv.tag_bind("pucW","<Button-1>",self.OnPressDrag)
            self.canv.tag_bind("pucW","<B1-Motion>",self.OnMoveDrag)
            self.canv.tag_bind("pucW","<ButtonRelease-1>",self.OnReleaseDrag)


    def StartGame1(self):
        """startet die initialisierung des spiel 1"""

        self.StatsMoves = 0
        self.StatsPunkte = 0

        self.CurrentGame = 1
        self.Playfield_Current = copy.deepcopy(playfield_startPosGame1)
        self.CreatePlayField()
        self.InitGame1()
        #self.ShowBtn_Back()

    def StartGame2(self):
        """startet die initialisierung des spiel 1"""
        self.StatsMoves = 0
        self.StatsPunkte = 0

        self.CurrentGame = 2
        self.CreatePlayField()
        self.Playfield_Current = copy.deepcopy(playfield_startPosGame2)
        self.InitGame2()
        #self.ShowBtn_Back()


if __name__ == "__main__":
    pass

# Project By Alex Bruksch | Nick Dziewior | Jean Neumann | Daniel Pyka