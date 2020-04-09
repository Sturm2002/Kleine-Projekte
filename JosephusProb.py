from time import sleep
import turtle
import os

AnzahlPersonen = 23

Personen = []
texte = []

readyloaded = False

wn = turtle.Screen()
wn.screensize(600,800)
wn.title("Josephus Problem in Python!")
wn.bgcolor("Black")

title = turtle.Turtle()
title.pu()
title.color("white")
title.ht()
title.speed(0)

description = turtle.Turtle()
description.pu()
description.color("grey")
description.ht()
description.speed(0)
description.goto(0,-400)
description.write("Space drücken um Nächste runde zu Starten",align="center")

byalex = turtle.Turtle()
byalex.pu()
byalex.color("white")
byalex.ht()
byalex.speed(0)
byalex.goto(400,-400)
byalex.write("By Alex Bruksch / 7.4.2020",align="center")



def MakePerson():
    global AnzahlPersonen

    for i in range(AnzahlPersonen):

        Person = turtle.Turtle()
        Person.penup()
        Person.shape("circle")
        Person.fillcolor("White")
        Person.speed(0)
        Person.shapesize(2,2)

        text = turtle.Turtle()
        text.penup()
        text.shape("circle")
        text.color("White")
        text.speed(0)
        text.shapesize(2,2)
        #text.write(i)
        text.ht()
        

        Personen.append(Person)
        texte.append(text)

def ArangePersons():
    global Personen
    global texte
    global readyloaded

    for i in range(len(Personen)):
        Personen[i].setheading(90)
        texte[i].setheading(90)
        

    deg = 360 / len(Personen)
    Personen[0].setheading(90)
    texte[0].setheading(90)

    for i in range(len(Personen)):

        texte[i].setheading(i*deg)
        texte[i].forward(10*len(Personen))

        Personen[i].setheading(i *deg)
        Personen[i].forward(8*len(Personen))
    readyloaded = True
    
    
        


def KillPersons():
    global Personen
    global readyloaded
    if readyloaded == True:

        for i in range(0,len(Personen)):
            if i +1 == len(Personen):
                
                Personen[0].fillcolor("Red")
                Personen.pop(0)

            else:
                Personen[i+1].fillcolor("Red")
                Personen.pop(i+1)
            
            
            print(i)
            print(len(Personen))
            sleep(0.5)
    else:
        pass


MakePerson()
ArangePersons()

wn.listen()
wn.onkeypress(KillPersons,"space")



    


running = True

while running:

    if len(Personen) == 1:
        title.write("Found")
        

    for zahl in range(len(texte)):
        texte[zahl].write(zahl)

    wn.update()
    sleep(0.1)

# Made By Alex Bruksch / Sturm2002 
# 6.4.2020 

    
