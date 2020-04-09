from time import sleep
import os

weiter = True
personen = []

data = open("datas.txt",'a+')
data.seek(0)

num_lines = sum(1 for line in open('datas.txt'))

last = False

print(num_lines)
for i in range(int(num_lines / 4)):
    datavname = data.readline().replace("\n","")
    datanname = data.readline().replace("\n","")
    dataalter = data.readline().replace("\n","")
    datagesch = data.readline().replace("\n","")

    personen.append([datavname,datanname,dataalter,datagesch])

def ausgabe():
    if len(personen) == 0:
        os.system('cls')
        print("\nEs wurden noch keine Personen Eingegeben!\n")
        sleep(3)
        os.system('cls')
        eingabe()

    else:
        enter = None
        os.system('cls')
        print("|--Vorname--|--Nachname--|--Alter--|--Gesch--|\n")
        
        for i in range(len(personen)):
            curvname = personen[i][0]
            curnname = personen[i][1]
            curalter = personen[i][2]
            curgesch = personen[i][3]
            
            print("|--",curvname,"--|","|--",curnname,"--|","|--",curalter,"--|","|--",curgesch,"--|")
        print("Enter drücken! oder Delete Eintippen um Datenbank zu leeren")
        enter = input()
        if enter == "Delete":
            data.close()
            os.remove("datas.txt")
            personen.clear()
            
def eingabe():

    def EinStatus():
        print("|--",vname,"--|","|--",nname,"--|","|--",alter,"--|","|--",gesch,"--|")

    os.system('cls')
    vname = None
    nname = None
    alter = None
    gesch = None
    
    os.system('cls')
    print("\n\nPersonen Eintragen!\n")
    sleep(2)
    os.system('cls')


    print("Bitte Vorname Eintippen\n")
    vname = str(input())
    
    
    os.system('cls')
    EinStatus()
    print("Bitte Nachname Eintippen!\n")
    nname = str(input())

    os.system('cls')
    EinStatus()
    print("Bitte Alter Eintippen!\n")
    alter = int(input())

    os.system('cls')
    EinStatus()
    print("Bitte M oder W Eintippen!\n")
    gesch = str(input())

    os.system('cls')
    EinStatus()
    trash = input()
    os.system('cls')

    personen.append([vname,nname,alter,gesch])

    data.write(vname + "\n")
    data.write(nname +"\n")
    data.write(str(alter) +"\n")
    data.write(gesch +"\n")
    data.close()

##############################################################
while True:
    try:
        data = open("datas.txt",'a+')
        os.system('cls')
        if len(personen) == 0:
            print("Es Wurden Bisher noch keine personen Eingetragen!")
            sleep(3)
            os.system('cls')

        einoderaus = None
        print("Moechtest du Personen *Ausgeben* oder *Eingeben* ?\nUm zu Verlassen, gebe E(x)it ein!\nUm das Programm zu Löschen tippe Deinstallieren ein!\nBitte (E)ingabe oder (A)usgabe eintippen")
        einoderaus = input()
        if einoderaus == "A" or einoderaus == "Ausgabe" or einoderaus == "a":
            ausgabe()
        if einoderaus == "E" or einoderaus == "Eingabe" or einoderaus == "e":
            eingabe()
        if einoderaus == "X" or einoderaus == "Exit" or einoderaus == "x":
            exit()
        if einoderaus == "Deinstallieren":
            print("\n\nDanke Fuer Das Benutzen meiner Datenbank!\n\n")
            os.remove("DatenbankByAlex.exe")

    except KeyboardInterrupt:
        sleep(5)
        exit()