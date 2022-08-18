import tkinter as tk
from assets import PixelSz


WindowTitle = "Sudoku-Prototype"

WindowBGColor = "#000000"
WindowAccentColor = "#FFFFFF"

ProtypeDBPath = "res/prototype.db"

ScreenSizeMultiplicator = 0.95
ScreenSizeX = 1920
ScreenSizeY = 1080
HalfScreenX = ScreenSizeX / 2
HalfScreenY = ScreenSizeY / 2
PasswordHash = ""

runWithAlgo = True

algo_StandardSearchDepth = 4

snd_MainVolume = 0.5

#https://mixkit.co/free-sound-effects/
bauerpicS = r"res/Schach_Figur_S.png" # png
bauerpicW = r"res/Schach_Figur_W.png" # png
loading = r"res/loading.png"
snd_CharUp = r"res/charup.wav"
snd_CharDown = r"res/chardown.wav"
snd_CharKill = r"res/charkill.wav"
snd_VolTick = r"res/voltick.wav"
snd_pop = r"res/pop.wav"
snd_win = r"res/win.wav"
snd_lose = r"res/lose.wav"

CreditsPic = r"res/credits.png"

pucpicS = r"res/pucS.png"
pucpicW = r"res/pucW.png"
waydot = r"res/waydot.png"

LosePic = r"res/lose.png"
WinPic = r"res/win.png"
#WinPic = r"res/Ra874d191615e130d3253441f4c13eb64.png"

CharSize = 130

playfield_startx = 575
playfield_distx = 150
playfield_starty = 100
playfield_disty = 150
playfield_size = 6
playfield_FindFieldTolerance = 60 # In Pixel
playfield_Coords = []
playfield_startPosGame1 = [
    [1,1,1,1,1,1],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [2,2,2,2,2,2]
]

playfield_startPosGame2 = [
    [0,1,0,1,0,1],
    [1,0,1,0,1,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,2,0,2,0,2],
    [2,0,2,0,2,0]
]

#Playfield_Current = []

def ScreenSizeMultSet(val):
    global ScreenSizeMult
    ScreenSizeMult = val

StatsScreenTextGame1 = """

Ein Schachspiel nur mit Bauern, der Spieler
startet mit Weiß, während die KI auf den 
Spieler reagiert. Die Bauern können immer 
ein Feld nach vorne ziehen, außer ein 
gegnerischer oder verbündeter Bauer steht 
ihnen entgegen. Wenn ein Bauer ein Feld nah
diagonal zu einem feindlichen Bauer steht 
kann er diesen mit einem diagonalen Zug 
schlagen und auf dessen Position gehen. 

Gewonnen bzw. Verloren hat man wenn man 
die gegenüberliegenden Grundlinie mit 
einem seiner Figuren erreicht keine Figuren
mehr hat oder kein Zug mehr ausführbar ist."""

StatsScreenTextGame2 = """

Die Figuren starten auf den schwarzen 
Feldern der ersten beiden Reihen. Figuren
bewegen sich diagonal, und springen über 
gegnerische Figuren. In Dame gilt 
schlagpflicht sprich man muss wenn es 
möglich ist eine gegnerische Figur schlagen. 
Schlagen kann man wenn eine gegnerische 
Figur hinter sich ein freies Feld hat und 
somit die Figur übersprungen werden kann.
Dann steht die eigene Figur hinter der 
gegnerischen und die gegnerische Figur 
wird aus dem Spielbrett genommen. Springt
man über eine Figur und steht dann auf 
einem Feld von wo aus man eine andere Figur
schlagen kann, muss dies ebenfalls getan 
werden(also eine Schlag- bzw. Sprungkette). 

Gewonnen bzw. Verloren hat man wenn man 
die gegenüberliegenden Grundlinie mit 
einem seiner Figuren erreicht, keine 
Figuren mehr hat oder kein Zug mehr 
ausführbar ist."""

StatsScreenTextGame3 = """

Auf dem Spielfeld werden abwechselnd auf
freien Spielfeldern Figuren gesetzt.

Gewonnen ist wenn man als Erster viel 
Spielsteine in einer Zeile, Spalte oder 
Diagonale gesetzt hat. Unentschieden ist 
wenn alle Felder belegt sind und keine Reihe, 
Spalte oder Diagonale erreicht worden ist."""

SuperDuperSecretButtonLink = "https://www.thisworldthesedays.com/lul18.html"

# Project By Alex Bruksch | Nick Dziewior | Jean Neumann | Daniel Pyka