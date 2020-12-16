import turtle
import math
import numpy as np
import random
import time
from tkinter import *
from tkinter import messagebox

figurer = []

class Figur:
    def __init__(dræbmig):
        dræbmig.color = (random.random(), random.random(), random.random())


    def draw(dræbmig):
        turtwig = turtle.Turtle()
        #turtwig.goto(-400,+400)
        turtwig.speed(10)
        try:
            for x in range(dræbmig.n):
                turtle.title("Keder mig...")
                #turtwig.pencolor(dræbmig.color)
                turtwig.color((dræbmig.color))

                turtwig.forward(dræbmig.l)
                turtwig.right(dræbmig.vinkel)
        except:
            turtle.title("Hvad skal jeg bruge det her til?")
            turtwig.color((dræbmig.color))
            turtwig.circle(dræbmig.radius)

        turtle.Screen().exitonclick()

class Polygon(Figur):
    def __init__(dræbmig,sider,sidelængde,color):
        super().__init__()
        dræbmig.color = color
        dræbmig.n = sider
        dræbmig.l = sidelængde / sider * 5
        dræbmig.sidelængde = sidelængde / 20

        if dræbmig.n <= 2:
            print("Ikke godkendt antal sider")


        dræbmig.vinkelSum = dræbmig.n * 180 - 360
        dræbmig.vinkel = 180 - dræbmig.vinkelSum / dræbmig.n


        #Omkreds af regulær polygon:
        dræbmig.omkreds = dræbmig.n * dræbmig.sidelængde

        # Areal af regulær polygon:
        dræbmig.areal = (1 / 2 * (dræbmig.n * dræbmig.sidelængde) * ((dræbmig.sidelængde) / (2 * math.tan(math.radians(180 / dræbmig.n)))))

class Cirkel(Figur):
    def __init__(dræbmig,radius,color):
        super().__init__()
        dræbmig.color = color

        dræbmig.radius = radius
        dræbmig.areal = dræbmig.radius**2 * math.pi
        dræbmig.omkreds = dræbmig.radius * 2 * math.pi


        print("Omkreds: " + str(dræbmig.omkreds))
        print("Areal: " + str(dræbmig.areal))


class Femkant(Polygon):
    def __init__(dræbmig):
        super().__init__(dræbmig.areal,dræbmig.color,dræbmig.omkreds)


        print("Omkreds: " + str(dræbmig.omkreds))
        print("Areal: " + str(dræbmig.areal))

        print(super().areal)


class Firkant(Polygon):
    def __init__(dræbmig):
        super().__init__(dræbmig.areal, dræbmig.color, dræbmig.omkreds)

        print("Omkreds: " + str(dræbmig.omkreds))
        print("Areal: " + str(dræbmig.areal))

        print(super().areal)


class Trekant(Polygon):
    def __init__(dræbmig):
        super().__init__(dræbmig.areal, dræbmig.color, dræbmig.omkreds)

        print("Omkreds: " + str(dræbmig.omkreds))
        print("Areal: " + str(dræbmig.areal))

        print(super().areal)


def mainMenu():
    window = Tk()
    window.geometry("400x300")
    window.title("Menu")

    def clicked():
        sider = int(siderEntry.get())
        sidelængde = int(sidelængdeEntry.get())*20
        color = str(colorEntry.get()).lower()

        window.destroy()

        if sider == 0:
            figurer.append(Cirkel(sidelængde,color))
        if sider >= 3:
            figurer.append(Polygon(sider, sidelængde,color))
        for figur in figurer:
            figur.draw()



    betalButton = Button(window, text="Start!", command=clicked, background="white", foreground="black", height=5, width=15)
    betalButton.place(relx=0.5,rely=0.2,anchor=CENTER)


    siderEntry = Entry(window, width=16)
    siderEntry.place(relx=0.5, rely=0.5, anchor=CENTER)

    sidelængdeEntry = Entry(window, width=16)
    sidelængdeEntry.place(relx=0.5, rely=0.7, anchor=CENTER)

    colorEntry = Entry(window, width=12)
    colorEntry.place(relx=0.5, rely=0.9, anchor=CENTER)

    siderLabel = Label(window, text="Indtast antal sider figuren skal have")
    siderLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

    sidelængdeLabel = Label(window, text="Indtast sidelængden af figuren")
    sidelængdeLabel.place(relx=0.5, rely=0.6, anchor=CENTER)

    cirkelLabel = Label(window, text="0 sider = cirkel :D")
    cirkelLabel.place(relx=0.8, rely=0.9, anchor=CENTER)

    colorLabel = Label(window, text="Vælg farve(Engelsk)")
    colorLabel.place(relx=0.5, rely=0.8, anchor=CENTER)

    window.mainloop()
mainMenu()



