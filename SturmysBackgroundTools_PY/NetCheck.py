# Import Python library
import datetime,networkscan,copy,json,os,threading
from time import sleep
from win10toast import ToastNotifier
from fritzconnection.lib.fritzhosts import FritzHosts




jsonpath = os.path.dirname(os.path.abspath(__file__)) + '\conf.json'
jsonfile = open(jsonpath)
jsonvals = json.load(jsonfile)

Settings = jsonvals["NetCheck"]["Settings"]

KnownDev = jsonvals["NetCheck"]["KnownDevices"]


tick = Settings["RunInterval"]
ToastFormat = Settings["ToastFormat"]
ConFormat = Settings["ConFormat"]


LastCon = {}
CurCon = {}
ShowCon = {}
running = True
ShowRunning = True

toaster = ToastNotifier()

# Main function

def WaitForInput():
    global ShowRunning
    input()
    ShowRunning = False


def ShowConnected():
    global ConFormat,ShowRunning,running
    ShowRunning = True
    if running:
        ShowThread = threading.Thread(target=WaitForInput,daemon=True)
        ShowThread.start()
        oldjsoncurcon = ""
        while ShowRunning:
            jsoncurcon = dict(json.load(open(jsonpath))["NetCheck"]["CurrentDevices"])

            if jsoncurcon != oldjsoncurcon:
                fulloutstr = ""
                for con in sorted(sorted(sorted(jsoncurcon.items(), key=lambda x: x[0]),key=lambda x: x[1]["status"],reverse=True),key=lambda x: x[1]["LastCon"],reverse=True):
                #for con in sorted(jsoncurcon.items(), key=lambda x:x[1]["status"],reverse=True):
                    outstr = ConFormat.replace("ip",jsoncurcon[con[0]]["ip"] + (14-len(jsoncurcon[con[0]]["ip"]))*" ")
                    outstr = outstr.replace("name",jsoncurcon[con[0]]["name"]+ (25-len(jsoncurcon[con[0]]["name"]))*" ")
                    outstr = outstr.replace("status",str(jsoncurcon[con[0]]["status"])+ (7-len(str(jsoncurcon[con[0]]["status"])))*" ")
                    outstr = outstr.replace("CustomName",jsoncurcon[con[0]]["CustomName"]+ (20-len(jsoncurcon[con[0]]["CustomName"]))*" ")
                    outstr = outstr.replace("mac",jsoncurcon[con[0]]["mac"]+ (17-len(jsoncurcon[con[0]]["mac"]))*" ")
                    outstr = outstr.replace("LastCon",jsoncurcon[con[0]]["LastCon"]+ (20-len(jsoncurcon[con[0]]["LastCon"]))*" ")
                    fulloutstr += outstr
                os.system("cls")
                print(fulloutstr + "\n>Press Enter to exit<")
            sleep(0.5)
            oldjsoncurcon = jsoncurcon
    else:
        os.system("cls")
        print(">NetScan< Not running!\n Press Enter to Continue")
        input()
    

def StopNetCheck():
    global running
    running = False

def StartNetCheck():
    global running
    running = True

def Main():
    global running,LastCon,CurCon,ShowCon,KnownDev,tick,ToastFormat,jsonfile,toaster,jsonvals,jsonpath

    fh = FritzHosts(address=jsonvals["NetCheck"]["Settings"]["FritzBoxIP"], password=jsonvals["NetCheck"]["Settings"]["FritzBoxPW"])

    
    while running:
        sleep(tick)
        activeHosts = fh.get_active_hosts()
        NewVals = json.load(open(jsonpath))["NetCheck"]
        OldCurCon = NewVals["CurrentDevices"]
        ChangeCurcon = dict(copy.deepcopy(NewVals["CurrentDevices"]))
        FoundDevices = []

        for con in ChangeCurcon:
            ChangeCurcon[con]["status"] = False

        for cd in activeHosts:
            CurrHost = {
                "ip" : cd["ip"],
                "name" : cd["name"],
                "mac" : cd["mac"],
                "status" : cd["status"]
            }
            for kd in NewVals["KnownDevices"]:
                if cd["ip"] == kd[1]:
                    CurrHost["CustomName"] = kd[0]
                    CurrHost["LastCon"] = datetime.datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
                    
                    ChangeCurcon[kd[0]] = CurrHost
                    break
                else:
                    pass
         
        for kd in NewVals["KnownDevices"]:
            NewDict = {
                "ip" : kd[1],
                "name" : "-",
                "mac" : "-",
                "status" : False,
                "CustomName" : kd[0],
                "LastCon" : "00.00.0000, 00:00:00"
                }
            if not kd[0] in ChangeCurcon:
                ChangeCurcon[kd[0]] = NewDict
        
        newjsonvals = json.load(open(jsonpath))
        newjsonvals["NetCheck"]["CurrentDevices"] = ChangeCurcon

        with open(jsonpath, "w") as outfile:
            outfile.write(json.dumps(newjsonvals,indent=4))
            outfile.close()

        OutStr = ""
        for ccc in ChangeCurcon:
            if ccc in OldCurCon:
                if ChangeCurcon[ccc]["status"] == True and OldCurCon[ccc]["status"] == False:
                    OutStr += NewVals["Settings"]["ToastFormat"].replace("NAME",ccc).replace("STATUS","Connected")
                elif ChangeCurcon[ccc]["status"] == False and OldCurCon[ccc]["status"] == True:
                    OutStr += NewVals["Settings"]["ToastFormat"].replace("NAME",ccc).replace("STATUS","Disconnected")
                else:
                    pass
        if len(OutStr) >= 1:
            jsonpath = os.path.dirname(os.path.abspath(__file__)) + '\conf.json'
            jsonfile = open(jsonpath)
            jsonvals = json.load(jsonfile)
            if jsonvals["General"]["Settings"]["NotificationEnable"]:
                toaster.show_toast("Device Alert",OutStr,threaded=True,duration=jsonvals["General"]["Settings"]["NotificationDuration"])

        
    exit() 

if __name__ == "__main__":
    Main()