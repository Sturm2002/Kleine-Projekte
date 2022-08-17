from time import sleep
import tkinter as tk
from tkinter import StringVar
from turtle import Screen, screensize
import pygame,random,copy
from globs import *
from PIL import Image,ImageTk
from tkvideo import tkvideo


def InitTK():
    
    root = tk.Tk()
    #root.geometry("800x600+300+300")
    root.configure(background=ct["BGColor"])
    return root

class MainDC(tk.Frame):
    
    def __init__(self,master):
        """Wird Ausgeführt wenn man eine instanz von MainWindow Erstellt"""
        super().__init__(master)
        self.master = master
        self.configure(width=ScreenSize[0],height=ScreenSize[1],bg=ct["BGColor"])
        #master.attributes("-fullscreen",True)

        self.OilTempPerc = 50
        self.GasVal = 50
        self.controllights = []
        self.ShowSplash()

        self.pack()


    def ShowSplash(self):
        self.splash = tk.Label(self,bg=ct["BGColor"])
        self.splash.place(x=460,y=0)
        player = tkvideo(pics["Splash"],self.splash,loop=0,size = (1080,480))
        player.play()
        self.after(2500,self.ShowMainDC)
        
    def DrawSpeedo(self):
        self.canv.create_oval(pos("w",100),pos("n",0),pos("w",580),pos("s",0),outline=ct["TachoBorderColor"],fill=ct["TachoBGColor"],width=4,tags=["speedo"])

    def DrawTacho(self):
        self.canv.create_oval(pos("e",100),pos("n",0),pos("e",580),pos("s",0),outline=ct["TachoBorderColor"],fill=ct["TachoBGColor"],width=4,tags=["tacho"])

    def DrawOilTemp(self):
        self.canv.delete("temp")
        
        for temp in range(int(self.OilTempPerc/5)):
            self.canv.create_rectangle(0,480-(temp-1)*24,340,480-temp*24,width=4,fill=self.rgb((int(255/20)*temp,255-int(255/20)*temp,0)),tags=["temp"])

        self.canv.tag_raise("speedo")

    def DrawGasVal(self):
        self.canv.delete("gas")
        
        for temp in range(int(self.GasVal/5)):
            self.canv.create_rectangle(pos("e",0),480-(temp-1)*24,pos("e",340),480-temp*24,width=4,fill=self.rgb((int(255/20)*temp,255-int(255/20)*temp,0)),tags=["gas"])

        self.canv.tag_raise("tacho")

    def DrawAllControlLights(self):
        self.canv.delete("controlllights")
        for light in pics["ControllLights"]:
            load = Image.open(pics["ControllLightsPrePath"] + light[2])
            load = load.resize((80,80))
            lightpic = copy.deepcopy(ImageTk.PhotoImage(load))

            self.controllights.append([light[0],lightpic])

            piclbl = tk.Label(self,image=self.controllights[-1],bg=ct["BGColor"],anchor="c")
            piclbl.place(width=80,height=80,x=light[1][0],y=light[1][1])
            self.controllights[-1].append(piclbl)
            self.master.update()
        
        self.master.update()



    def ShowMainDC(self):
        self.ClearFrame()
        self.canv = tk.Canvas(self,background=ct["BGColor"],highlightthickness=0,width=ScreenSize[0],height=ScreenSize[1])
        self.canv.pack()
        self.DrawSpeedo()
        self.DrawTacho()
        self.DrawOilTemp()
        self.DrawGasVal()
        self.DrawAllControlLights()
        

    def rgb(self,rgb):
        """  take rgb To hexadecimal  Args: rgb: rgb Color  Returns:  Hexadecimal  """
        rgb = str(rgb)
        RGB = rgb.replace('(', '').replace(")", '').split(',')  #  take RGB The format is divided into 
        color = '#'
        for i in RGB:
            num = int(i)
            #  take R、G、B Convert to 16 Base concatenation conversion and capitalization  hex()  The function is used to 10 Base integers are converted to 16 Base number , In string form 
            color += str(hex(num))[-2:].replace('x', '0')
        return color

    def ClearFrame(self):
        """leert alle Tkinter Elemente (Canvas mit eingeschlossen)"""
        for child in self.winfo_children():
            child.destroy()

    def Testplus(self):
        self.OilTempPerc += 5
        self.DrawOilTemp()
        self.canv.tag_raise("speedo")
        self.update()

    def Testminus(self):
        self.OilTempPerc -= 5
        self.DrawOilTemp()
        self.canv.tag_raise("speedo")
        self.update()
    

        
        
    




