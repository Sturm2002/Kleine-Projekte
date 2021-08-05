import random
import time,os,pygame
from tkinter.constants import DISABLED
from PIL import Image,ImageTk
import tkinter as tk
Cards = ["Ohrenklatscher","Ohrenklatscher","Eisklatscher","Eisklatscher","Daumenklatscher","Daumenklatscher","Linksklatscher","Linksklatscher","Rechtsklatscher","Rechtsklatscher","Klatschmeister","Klatschmeister","Klatschmeister","Klatschmeister","Klatschglas","Klatschglas","Klatschglas","Klatschglas","Klatschglas","Klatschregel","Klatschregel","Klatschregel","Klatschregel","Klatschpartner","Klatschpartner","Klatschpartner","Klatschleuchte","Klatschleuchte","Klatschreim","Klatschreim","Klatschreim","Klatschreim","Klatschgeschichte","Klatschgeschichte","Klatschthema","Klatschthema","Klatschthema","Klatschthema","Klatschkoffer","Klatschkoffer","Klatschkoffer","Klatschduell","Klatschduell","Klatschduell","Klatschduell","Frauenklatscher","Frauenklatscher","Männerklatscher","Männerklatscher","Klatschkarte","Klatschkarte","Klatschkarte","Klatschkarte","Klatschverkehr","Klatschverkehr","Klatschverkehr","Klatschkampf","Klatschkampf","Klatschkampf","Klatschrichtung","Klatschrichtung","Klatschgeschenk","Klatschgeschenk","Klatschgeschenke","Klatschgeschenke","Klatschrunde","Klatschrunde","Lavaklatscher","Lavaklatscher","Kratzklatscher","Kratzklatscher","Wahrheitsklatscher1","Wahrheitsklatscher2","Wahrheitsklatscher3","Wahrheitsklatscher4","Wahrheitsklatscher5","Wahrheitsklatscher6","Wahrheitsklatscher7","Klatschabstimmung","Klatschabstimmung","Pantomimenklatscher","Pantomimenklatscher","Erklärklatscher","Erklärklatscher","Küsschenklatscher","Küsschenklatscher","Kussklatscher","Kussklatscher","Klatscher","Klatscher","Medusaklatscher","Medusaklatscher","Medusaklatscher","NICHTVORLESENklatscher","Klatschname","Klatschname","Klatschname","Klatschname","Nasenklatscher","Nasenklatscher","Tanzklatscher","Tanzklatscher","Tanzklatscher","Brillenklatscher","Brillenklatscher","Langhaarklatscher","Kurzhaarklatscher","I-Phoneklatscher","I-Phoneklatscher","Kleinkindklatscher","Volljährigenklatscher","Klatschcutie"]
HoldCards = ["Klatschmeister","Klatschregel","Klatschpartner","Medusaklatscher","Klatschname"]
Player = [
    ["Wlada",[]],
    ["Alessio",[]],
    ["Klaus",[]],
    ["Jana",[]]
]



def InitTK():
    root = tk.Tk()
    #root.geometry("800x600+300+300")
    root.title("DoppelKlatschen")
    root.configure(background="black")
    return root

class MainWindow(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.configure(width=800,height=800,bg="black")

        self.CurrentPlayer = 0
        self.cardy = 150
        self.cardw = 214
        self.cardh = 300


        self.LeftCards = tk.StringVar(self)
        self.LeftCards.set(str(len(Cards)) + " Karten Übrig")
        self.CurrentPlayerStrVar = tk.StringVar(self)
        self.WladaStrVar = tk.StringVar(self)
        self.AlessioStrVar = tk.StringVar(self)
        self.KlausStrVar  = tk.StringVar(self)
        self.JanaStrVar = tk.StringVar(self)

        self.CurrentPlayerStrVar.set(Player[self.CurrentPlayer][0] + " muss ziehen!")
        
        #Doppelklatschenkarten/Klatscher.png
        #Doppelklatschenkarten/Klatscher.png

        self.pack()
        self.OpenMainScreen()

    def OpenMainScreen(self):
        self.title = tk.Label(self,text="DoppelKlatschen",bg="black",fg="white",font="Rockwell " + str(20) +" bold",anchor="c")
        self.title.place(x=150,y=25,height=100,width=300)

        self.anreihe = tk.Label(self,textvariable=self.CurrentPlayerStrVar,bg="black",fg="white",font="Rockwell " + str(15) +" bold",anchor="n")
        self.anreihe.place(x=100,y=550,height=100,width=400)


        self.titlewlada = tk.Label(self,text="Wlada",bg="black",fg="white",font="Rockwell " + str(15) +" bold",anchor="n")
        self.titlewlada.place(x=500,y=50,height=100,width=200)

        self.lblwlada = tk.Label(self,textvariable=self.WladaStrVar,bg="black",fg="white",font="Rockwell " + str(15) +" bold",anchor="ne")
        self.lblwlada.place(x=500,y=75,height=400,width=200)


        self.titlealessio = tk.Label(self,text="Alessio",bg="black",fg="white",font="Rockwell " + str(15) +" bold",anchor="n")
        self.titlealessio.place(x=500,y=200,height=100,width=200)

        self.lblalessio = tk.Label(self,textvariable=self.AlessioStrVar,bg="black",fg="white",font="Rockwell " + str(15) +" bold",anchor="ne")
        self.lblalessio.place(x=500,y=225,height=400,width=200)


        self.titleklaus = tk.Label(self,text="Klaus",bg="black",fg="white",font="Rockwell " + str(15) +" bold",anchor="n")
        self.titleklaus.place(x=500,y=350,height=100,width=200)

        self.lblklaus = tk.Label(self,textvariable=self.KlausStrVar,bg="black",fg="white",font="Rockwell " + str(15) +" bold",anchor="ne")
        self.lblklaus.place(x=500,y=375,height=400,width=200)


        self.titlejana = tk.Label(self,text="Jana",bg="black",fg="white",font="Rockwell " + str(15) +" bold",anchor="n")
        self.titlejana.place(x=500,y=500,height=100,width=200)

        self.lbljana = tk.Label(self,textvariable=self.JanaStrVar,bg="black",fg="white",font="Rockwell " + str(15) +" bold",anchor="ne")
        self.lbljana.place(x=500,y=525,height=400,width=200)


        self.Ziehen = tk.Button(self,text="Ziehen", bg="white",fg="black",font="Rockwell " + str(15) +" bold",anchor="c",command=self.ZiehenButtonPressed)
        self.Ziehen.place(x=100,y=600,height=100,width=400)

        self.lblLeftCards = tk.Label(self,textvariable=self.LeftCards,bg="black",fg="white",font="Rockwell " + str(15) +" bold",anchor="n")
        self.lblLeftCards.place(x=100,y=700,height=100,width=400)

    def ZiehenButtonPressed(self):
        if len(Cards) <= 0:
            self.Ziehen.configure(text="keine Karten!",state="disabled")
        else:
            rndCard = random.randint(0,len(Cards)-1)
            self.currentCard = Cards[rndCard]
            for i in HoldCards:
                if i == self.currentCard:
                    for j in Player:
                        for k in j[1]:
                                if k == i:
                                    j[1].pop(j[1].index(k))
                                    
                    Player[self.CurrentPlayer][1].append(self.currentCard)
            
            Cards.pop(rndCard)
            self.LeftCards.set(str(len(Cards)) + " Karten Übrig")
            
            print(self.currentCard + " | " + str(len(Cards)) + " | " + str(Player))
            if self.CurrentPlayer >= len(Player) -1:
                self.CurrentPlayer = 0
            else:
                self.CurrentPlayer += 1
            self.RefPlayerStat()
            self.CurrentPlayerStrVar.set(Player[self.CurrentPlayer][0] + " muss ziehen!")
            self.reloadPic(self.currentCard)
            self.cardpic = tk.Label(self,image=self.cardimg,bg="black",anchor="c")
            
            self.cardpic.place(x=200,y=self.cardy,width=self.cardw,height=self.cardh)

    def RefPlayerStat(self):
        wladastr = ""
        alessiostr = ""
        klausstr = ""
        janastr = ""
        for i in Player:
            if i[0] == "Wlada":
                for j in i[1]:
                    wladastr += j + "\n"
            if i[0] == "Alessio":
                for j in i[1]:
                    alessiostr += j + "\n"
            if i[0] == "Klaus":
                for j in i[1]:
                    klausstr += j + "\n"
            if i[0] == "Jana":
                for j in i[1]:
                    janastr += j + "\n"
        self.WladaStrVar.set(wladastr)
        self.AlessioStrVar.set(alessiostr)
        self.KlausStrVar.set(klausstr)
        self.JanaStrVar.set(janastr)

    def reloadPic(self,cardname):
        #dirname = os.path.dirname(__file__)
        #pfad = os.path.join(dirname, "res/" + cardname + ".png")

        self.card = Image.open(os.getcwd() + "/res/" + cardname + ".png")
        self.card = self.card.resize((self.cardw,self.cardh))
        self.cardimg = ImageTk.PhotoImage(self.card)

if __name__ == "__main__":
    mainroot = InitTK()
    window = MainWindow(mainroot)
    mainroot.mainloop()