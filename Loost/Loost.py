import loost_main
from sturmysprint import printstr
from time import sleep

loost_main.ClearCons()

def StartGame(state="load"):
    loost_main.ClearCons()
    print(loost_main.GameStart(state))
    sleep(3)

printstr(loost_main.StartString,0.001337)
sleep(3)
loost_main.ClearCons()

def MainMenu():
    running = True
    while running:
        loost_main.ClearCons()
        print(loost_main.StartString+"\n\n1 - Continue\n2 - New Game\n3 - Exit\n\n")
        inp = input()
        if inp.isnumeric():
            inp = int(inp)
            if inp == 1:
                StartGame("load")
                #running = False
            elif inp == 2:
                StartGame("new")
                #running = False
            elif inp == 3:
                running = False
MainMenu()
exit
            

    

    