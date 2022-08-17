

from pygame import Color




ColorThemes = {
    "Dark":{
        "BGColor" : "#000000",
        "FGColor" : "#CCCCCC",
        "TachoBGColor" : "#333333",
        "TachoBorderColor" : "#777777",
        "TachoAccentColor" : "#AA4444",
        "TachoNeedleColor" : "#CC3333"

    }
}

PicThemes = {
    "Standard" : {
        "Splash" : "C:/Users/sturm/OneDrive/Python 3/BigProjects/CarTeslaMultiMedia/DCHUD/splash.mp4",
        "ControllLightsPrePath" :  "C:/Users/sturm/OneDrive/Python 3/BigProjects/CarTeslaMultiMedia/DCHUD/res/CL/",
        "ControllLights" : [
            ["abs",[800,300],"abs.png"],
            ["airbag",[100,100],"airbag.png"],
            ["airpressure",[100,100],"airpressure.png"],
            ["battery",[100,100],"battery.png"],
            ["brakes",[100,100],"brakes.png"],
            ["elight",[100,100],"elight.png"],
            ["engine",[100,100],"engine.png"],
            ["lowgas",[100,100],"lowgas.png"],
            ["lowoil",[100,100],"lowoil.png"],
            ["nebelschlussleuchte",[100,100],"nebelschlussleuchte.png"],
            ["overheatingoil",[100,100],"overheatingoil.png"],
            ["slippery",[100,100],"slippery.png"],
            ["tempomat",[100,100],"tempomat.png"],
            ["traktion",[100,100],"traktion.png"],
            ["windshieldheating",[100,100],"windshieldheating.png"],
            ["fernlicht",[200,200],"fernlicht.png"]
        ]
    }
}

ScreenSize = [1920,480]

ct = ColorThemes["Dark"]
pics = PicThemes["Standard"]

def pos(bord:str,pixel:int):
    global ScreenSize
    if bord == "n":
        return 0 + pixel
    elif bord == "e":
        return ScreenSize[0] - pixel
    elif bord == "s":
        return ScreenSize[1] - pixel 
    elif bord == "w":
        return 0 + pixel

def RefVals():
    pass