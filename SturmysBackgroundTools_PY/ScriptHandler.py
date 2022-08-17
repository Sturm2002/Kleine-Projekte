
import time,ctypes,threading,NetCheck,os,win10toast,KeyGrabber,json,Door,SturmyDiscordBot

jsonpath = os.path.dirname(os.path.abspath(__file__)) + '\conf.json'
jsonfile = open(jsonpath)
jsonvals = json.load(jsonfile)

cmd_shown = False
mythreads = {}
systray = ""
NetCheckRunning = True
LocalPath = os.path.dirname(os.path.abspath(__file__)) + r"\\"


def FormatTextStrike(InText:str):
    return ''.join([u'\u0336{}'.format(c) for c in InText])

def ShowConnectedDevices():
    NetCheck.ShowConnected()

def StopNetCheck():
    try:
        if mythreads["NetCheck"].is_alive():
            
            print("stopping >NetScan<")
            NetCheck.StopNetCheck()
            while mythreads["NetCheck"] != "" and mythreads["NetCheck"].is_alive():
                pass
            print(">NetScan< stopped")
    except AttributeError:
        return

def NetCheckLoop():
    global NetCheckRunning
    NetCheck.Main()

def RestartNetCheck():
    os.system("cls")
    StopNetCheck()
    StartNetCheck()
    input("\nPress Enter to Continue")

def StartNetCheck():
    global mythreads,NetCheckRunning
    try:
        if not mythreads["NetCheck"].is_alive():
            
            print("starting >NetScan<")
            NetCheckRunning = True
            mythreads["NetCheck"] = ""
            NetCheck.StartNetCheck()
            mythreads["NetCheck"] = MTRun(NetCheckLoop)
            while not mythreads["NetCheck"].is_alive():
                pass
            print(">NetScan< started")
    except AttributeError:
        print("starting >NetScan<")
        NetCheckRunning = True
        mythreads["NetCheck"] = ""
        NetCheck.StartNetCheck()
        mythreads["NetCheck"] = MTRun(NetCheckLoop)
        while not mythreads["NetCheck"].is_alive():
            pass
        print(">NetScan< started")

def StopKeyGrabber():
    
    if mythreads["NetCheck"].is_alive():
        
        print("stopping >KeyLogger<")
        KeyGrabber.StopKeyGrabber()
        while mythreads["KeyGrabber"] != "" and mythreads["KeyGrabber"].is_alive():
            pass
        print(">KeyLogger< stopped")
    
def StartKeyGrabber():
    try:
        if not mythreads["KeyGrabber"].is_alive():
            print("starting >KeyLogger<")
            mythreads["KeyGrabber"] = MTRun(KeyGrabber.StartKeyGrabber)
            #KeyGrabber.StartKeyGrabber()
            while not mythreads["KeyGrabber"].is_alive():
                pass
            print(">KeyLogger< started")
    except AttributeError:
        print("starting >KeyLogger<")
        mythreads["KeyGrabber"] = MTRun(KeyGrabber.StartKeyGrabber)
        #KeyGrabber.StartKeyGrabber()
        while not mythreads["KeyGrabber"].is_alive():
            pass
        print(">KeyLogger< started")

def RestartKeyGrabber():
    StopKeyGrabber()
    StartKeyGrabber()

def StartNFCReader():
    try:
        if not mythreads["NFCReader"].is_alive():
            print("starting >NFCReader<")
            mythreads["NFCReader"] = MTRun(Door.StartReader)
            #KeyGrabber.StartKeyGrabber()
            while not mythreads["NFCReader"].is_alive():
                pass
            print(">NFCReader< started")
    except AttributeError:
        print("starting >NFCReader<")
        mythreads["NFCReader"] = MTRun(Door.StartReader)
        #KeyGrabber.StartKeyGrabber()
        while not mythreads["NFCReader"].is_alive():
            pass
        print(">NFCReader< started")

def StopNFCReader():
    if mythreads["NFCReader"].is_alive():
        
        print("stopping >NFCReader<")
        Door.StopReader()
        while mythreads["NFCReader"] != "" and mythreads["NFCReader"].is_alive():
            pass
        print(">NFCReader< stopped")

def RestartNFCReader():
    StopNFCReader()
    StartNFCReader()

def StartDisBot():
        try:
            if not mythreads["DiscordBot"].is_alive():
                print("starting >DiscordBot<")
                mythreads["DiscordBot"] = MTRun(SturmyDiscordBot.StartDisBot)
                #KeyGrabber.StartKeyGrabber()
                while not mythreads["DiscordBot"].is_alive():
                    pass
                print(">DiscordBot< started")
        except AttributeError:
            print("starting >DiscordBot<")
            mythreads["DiscordBot"] = MTRun(SturmyDiscordBot.StartDisBot)
            #KeyGrabber.StartKeyGrabber()
            while not mythreads["DiscordBot"].is_alive():
                pass
            print(">DiscordBot< started")

def StopDisBot():
    if mythreads["DiscordBot"].is_alive():
        
        print("stopping >DiscordBot<")
        Door.StopReader()
        while mythreads["DiscordBot"] != "" and mythreads["DiscordBot"].is_alive():
            pass
        print(">DiscordBot< stopped")

def RestartDisBot():
    StopDisBot()
    StartDisBot()

def MTRun(func):
    NewThread = threading.Thread(target=func,daemon=True)
    NewThread.start()
    return NewThread

def RunSherlock():
    global jsonvals
    #os.system("cls")
    cmd_str = "python " + '"' + os.path.dirname(os.path.abspath(__file__)) + '\sherlock\sherlock.py' + '"'
    userinp = input("Username to Search: ")
    cmd_str += " " + userinp
    cmd_str += ' --timeout '+ str(jsonvals["General"]["Settings"]["SherlockTimeout"]) + ' --print-all -o ' + '"' + os.path.dirname(os.path.abspath(__file__)) + jsonvals["General"]["Settings"]["SherlockOutputFile"].replace("*","_" + userinp) + '"'
    os.system(cmd_str)
    input("Press Enter to Continue")

def MainLoop():
    global mythreads,jsonvals

    KeyGrabb = ""
    NetScan = ""
    NFCReader = ""
    DisBot = ""

    if jsonvals["General"]["Settings"]["KeyGrabberNormalOn"]:
        KeyGrabb = MTRun(KeyGrabber.StartKeyGrabber)
    if jsonvals["General"]["Settings"]["NetCheckNormalOn"]:
        NetScan = MTRun(NetCheckLoop)
    if jsonvals["General"]["Settings"]["NFCReaderNormalOn"]:
        NFCReader = MTRun(Door.StartReader)
    if jsonvals["General"]["Settings"]["DiscordBotNormalOn"]:
        DisBot = MTRun(SturmyDiscordBot.StartDisBot)
    
    mythreads = {
        "NetCheck" : NetScan,
        "KeyGrabber" : KeyGrabb,
        "NFCReader" : NFCReader,
        "DiscordBot": DisBot
    }
    while True:
        os.system("cls")
        print("""
1- Show Connected Devices

2- Stop NetScan
3- Start NetScan
4- Restart NetScan


5- Run Sherlock

6- Stop KeyGrabber
7- Start KeyGrabber
8- Restart KeyGrabber

9- Stop NFC-Reader
10- Start NFC-Reader
11- Restart NFC-Reader

12- Stop Sturmy's Discord Bot
13- Start Sturmy's Discord Bot
14- Restart Sturmy's Discord Bot

0- Minimize
        """)
        inp = input("Selection: ")

        if inp == "0":
            Hide_cmd()

        elif inp == "1":
            ShowConnectedDevices()

        elif inp == "2":
            os.system("cls")
            StopNetCheck()
            input("\nPress Enter to Continue")

        elif inp == "3":
            os.system("cls")
            StartNetCheck()
            input("\nPress Enter to Continue")

        elif inp == "4":
            RestartNetCheck()

        elif inp == "5":
            RunSherlock()

        elif inp == "6":
            os.system("cls")
            StopKeyGrabber()
            input("\nPress Enter to Continue")

        elif inp == "7":
            os.system("cls")
            StartKeyGrabber()
            input("\nPress Enter to Continue")

        elif inp == "8":
            os.system("cls")
            RestartKeyGrabber()
            input("\nPress Enter to Continue")

        elif inp == "9":
            os.system("cls")
            StopNFCReader()
            input("\nPress Enter to Continue")

        elif inp == "10":
            os.system("cls")
            StartNFCReader()
            input("\nPress Enter to Continue")

        elif inp == "11":
            os.system("cls")
            RestartNFCReader()
            input("\nPress Enter to Continue")

        elif inp == "12":
            os.system("cls")
            StopDisBot()
            input("\nPress Enter to Continue")

        elif inp == "13":
            os.system("cls")
            StartDisBot()
            input("\nPress Enter to Continue")

        elif inp == "14":
            os.system("cls")
            RestartDisBot()
            input("\nPress Enter to Continue")

def Switch_Show_cmd():
    global cmd_shown
    if cmd_shown == True:
        Hide_cmd()
    else:
        Show_cmd()

def OpenConf():
    #print(str(os.path.dirname(os.path.abspath(__file__))) + "\conf.json")
    os.system('"' + str(os.path.dirname(os.path.abspath(__file__))) + '\conf.json"')

def Show_cmd():
    global cmd_shown
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 1 )
    cmd_shown = True
    #MainLoop()

def Hide_cmd():
    global cmd_shown
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
    cmd_shown = False

def StartMain():
    MainLoopThread = threading.Thread(target=MainLoop,daemon=True)
    MainLoopThread.start()

if __name__ == "__main__":
    print("running")
    Hide_cmd()
    time.sleep(3)
    Show_cmd()
    time.sleep(6)