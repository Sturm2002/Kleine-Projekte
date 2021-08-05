import datetime,colorama,time
from os import system

def clear():
    system("cls")

charlen = [2,9,0,5,9,0,5,9]
cols = []
clockarr = []
clockarrsizex = 8
clockarrsizey = 20

for i in range(clockarrsizey):
    shorty = []
    for j in range(clockarrsizex):
        shorty.append(" ")
    clockarr.append(shorty)

for i in range(0,len(charlen)-1):
    
    shorty = []
    for j in range(0,charlen[i]+1):
        shorty.append(j)
    cols.append(shorty)

running = True
endtime = ""

while running:
    starttime = str(datetime.datetime.now())
    starttime = starttime.split(" ")[1]
    starttime = starttime.split(".")[0]

    if endtime != starttime:
        curtime = str(datetime.datetime.now())
        curtime = curtime.split(" ")[1]
        curtime = curtime.split(".")[0]
        curtime = curtime.split(":")
        curtime = str(curtime[0])+str(curtime[1])+str(curtime[2])
        h1,h2,m1,m2,s1,s2 = curtime[0],curtime[1],curtime[2],curtime[3],curtime[4],curtime[5]
        clockarr[9][0],clockarr[9][1],clockarr[9][2],clockarr[9][3],clockarr[9][4],clockarr[9][5],clockarr[9][6],clockarr[9][7] = h1,h2,":",m1,m2,":",s1,s2

        for row in range(len(clockarr)):
            if row == 9:
                pass
            else:
                for cell in range(len(clockarr[row])):
                    if cell != 2 and cell != 5:
                        clockarr[row][cell] = str(int(clockarr[9][cell]) - (9-row))
                        if int(clockarr[row][cell]) < 0:
                            clockarr[row][cell] = " "
                        elif int(clockarr[row][cell]) > charlen[cell]:
                            clockarr[row][cell] = " "
        clear()
        for i in clockarr:
            for j in i:
                if clockarr.index(i)==9:
                    if j == ":":
                        print(colorama.Fore.LIGHTBLACK_EX+":",end=colorama.Fore.WHITE)
                    else:
                        print(colorama.Fore.LIGHTGREEN_EX+j,end=colorama.Fore.WHITE)
                else:
                    print(colorama.Fore.LIGHTBLACK_EX+j,end=colorama.Fore.WHITE)
            print("\n",end="")
        endtime = str(datetime.datetime.now())
        endtime = endtime.split(" ")[1]
        endtime = endtime.split(".")[0]