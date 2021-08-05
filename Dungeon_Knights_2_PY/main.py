from tkinter import NoDefaultRoot
import PlayerClass,EnemyClass,ObjectsClass,editor,colorama,codecs,MainGUI,Start_Game
from globalVars import *
from os import system
from time import sleep



def StartCode():
    root = MainGUI.InitTK()
    window = MainGUI.MainWindow(root)

    root.mainloop()

    
if __name__ == "__main__":
    StartCode()
