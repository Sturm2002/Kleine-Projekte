from tkinter import font
from PlayerClass import * 
import tkinter as tk
import tkinter.ttk as ttk
# Constants
DARKRED = "#420d0d"
WindowTxtMult = 0.75
Max_Players = 10

Characters = [
    ["Knight - Sir Lancelot","KnightA"],
    ["Knight - Abraham","KnightB"],
    ["Assasin - Jack The Silent","AssassinA"],
    ["Mage - Bender","MageA"],
    ["Mage - Oz (Flint)","MageB"],
    ["Dark Mage - Merlin","DarkMageA"],
    ["Dark Mage - Arthur","DarkMageB"],
    ["Archer - Headshot Hans","ArcherA"],
    ["Archer - Bogen Bertha","ArcherB"]
]

CharsArr0 = []
for i in Characters:
    CharsArr0.append(i[0])

# Variables
AmountPlayers = 1
MapFilePath = ""
AmountPlayersShowText = 0
Difficulty = 0
NewGamePlayers = []
PlayersArray = []
