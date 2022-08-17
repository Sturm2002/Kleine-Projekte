import time,win10toast,MainReader,threading,os,json

running = True

jsonpath = os.path.dirname(os.path.abspath(__file__)) + '\conf.json'
jsonfile = open(jsonpath)

jsonvals = json.load(jsonfile)

def StartReader():
    global running
    running = True
    Main()

def StopReader():
    global running

    running = False

def Main():
    global running
    ReaderThread = threading.Thread(target=MainReader.StartReader,daemon=True)
    ReaderThread.start()

    toaster = win10toast.ToastNotifier()
    jsonpath = os.path.dirname(os.path.abspath(__file__)) + '\conf.json'
    jsonfile = open(jsonpath)
    jsonvals = json.load(jsonfile)
    #043674320a5481 | 3edd4403
    while running:
        srnr = MainReader.GetData()
        if srnr == None:
            running = False
            break
        os.system("cls")
        print("Serial: " + srnr + "\n\nPress Enter to Continue")
        if srnr == "043674320a5481":
            if jsonvals["General"]["Settings"]["NotificationEnable"]:
                toaster.show_toast("Door Alert","Alex Openened the Door",duration=jsonvals["General"]["Settings"]["NotificationDuration"],threaded=True)
        elif srnr == "3edd4403":
            if jsonvals["General"]["Settings"]["NotificationEnable"]:
                toaster.show_toast("Door Alert","Vlad Opened the Door",duration=jsonvals["General"]["Settings"]["NotificationDuration"],threaded=True)
        else:
            if jsonvals["General"]["Settings"]["NotificationEnable"]:
                toaster.show_toast("Door Alert","Unauthorized Access Try",duration=jsonvals["General"]["Settings"]["NotificationDuration"],threaded=True)
    MainReader.StopReader()

    

if __name__ == "__main__":
    StartReader()
    MainReader.StartReader()
