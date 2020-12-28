from time import sleep
#import loost_main

PerfMode = True

def InitPerfMode(mode):
    global PerfMode
    PerfMode = mode

def printstr(inStr,speed=0.00001):
    global PerfMode
    if speed == 0.001337:
        for i in inStr:
            print(i,end="")
            sleep(speed)


    elif PerfMode == False:
        for i in inStr:
            print(i,end="")
            sleep(speed)
    elif PerfMode == True:
        print(inStr)
