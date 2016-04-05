#!/usr/bin/python

import sys
import pygame
from Tkinter import *

pygame.init()

def value_quit():
    octava=str(0+boct)
    nota="C"+octava
    num1.set(nota)
#    sound = pygame.mixer.Sound("./sounds/piano/Piano.pp."+nota+".aiff")
#    sound.play()
    return

#octava del que partimos
boct=2

def value_C0():
    octava=str(0+boct)
    nota="C"+octava
    num1.set(nota)
    sound = pygame.mixer.Sound("./sounds/piano/Piano.pp."+nota+".aiff")
    sound.play()
    return

def value_Db0():
    octava=str(0+boct)
    nota="Db"+octava
    num1.set(nota)
    sound = pygame.mixer.Sound("./sounds/piano/Piano.pp."+nota+".aiff")
    sound.play()
    return

def value_D0():
    octava=str(0+boct)
    nota="D"+octava
    num1.set(nota)
    sound = pygame.mixer.Sound("./sounds/piano/Piano.pp."+nota+".aiff")
    sound.play()
    return

def value_Eb0():
    octava=str(0+boct)
    nota="Eb"+octava
    num1.set(nota)
    sound = pygame.mixer.Sound("./sounds/piano/Piano.pp."+nota+".aiff")
    sound.play()
    return

def value_E0():
    octava=str(0+boct)
    nota="E"+octava
    num1.set(nota)
    sound = pygame.mixer.Sound("./sounds/piano/Piano.pp."+nota+".aiff")
    sound.play()
    return

def value_F0():
    octava=str(0+boct)
    nota="F"+octava
    num1.set(nota)
    sound = pygame.mixer.Sound("./sounds/piano/Piano.pp."+nota+".aiff")
    sound.play()
    return

def value_Gb0():
    octava=str(0+boct)
    nota="E"+octava
    num1.set(nota)
    sound = pygame.mixer.Sound("./sounds/piano/Piano.pp."+nota+".aiff")
    sound.play()
    return

def value_G0():
    octava=str(0+boct)
    nota="E"+octava
    num1.set(nota)
    sound = pygame.mixer.Sound("./sounds/piano/Piano.pp."+nota+".aiff")
    sound.play()
    return

def value_Ab0():
    octava=str(0+boct)
    nota="Ab"+octava
    num1.set(nota)
    sound = pygame.mixer.Sound("./sounds/piano/Piano.pp."+nota+".aiff")
    sound.play()
    return

def value_A0():
    octava=str(0+boct)
    nota="A"+octava
    num1.set(nota)
    sound = pygame.mixer.Sound("./sounds/piano/Piano.pp."+nota+".aiff")
    sound.play()
    return

def value_Bb0():
    octava=str(0+boct)
    nota="Bb"+octava
    num1.set(nota)
    sound = pygame.mixer.Sound("./sounds/piano/Piano.pp."+nota+".aiff")
    sound.play()
    return

def value_B0():
    octava=str(0+boct)
    nota="B"+octava
    num1.set(nota)
    sound = pygame.mixer.Sound("./sounds/piano/Piano.pp."+nota+".aiff")
    sound.play()
    return

def value_C1():
    octava=str(1+boct)
    nota="C"+octava
    num1.set(nota)
    sound = pygame.mixer.Sound("./sounds/piano/Piano.pp."+nota+".aiff")
    sound.play()
    return


root = Tk()
frame = Frame(root)
frame.pack()

root.title('PIANO FROM C '+str(boct))

num1=StringVar()

topframe = Frame(root)
topframe.pack(side = TOP)
txtDisplay=Entry(frame, textvariable = num1, bd=20, insertwidth=1, font=30, justify='center',width=4)
txtDisplay.pack(side=TOP)

button1_0 = Button(topframe, width=4, height=14, text="C", fg="black",command=value_C0)
button1_0.pack(side=LEFT)
button2_0 = Button(topframe, width=2, height=12, pady=8, bd=8, text="Db", bg="black", fg="white",command=value_Db0)
button2_0.pack(side=LEFT)
button3_0 = Button(topframe, width=4, height=14, text="D", fg="black",command=value_D0)
button3_0.pack(side=LEFT)
button4_0 = Button(topframe, width=2, height=12, pady=8, bd=8,text="Eb", bg="black", fg="white",command=value_Eb0)
button4_0.pack(side=LEFT)
button5_0 = Button(topframe, width=4, height=14, text="E", fg="black",command=value_E0)
button5_0.pack(side=LEFT)
button6_0 = Button(topframe, width=4, height=14, text="F", fg="black",command=value_F0)
button6_0.pack(side=LEFT)
button7_0 = Button(topframe, width=2, height=12, pady=8, bd=8, text="Gb", bg="black", fg="white",command=value_Gb0)
button7_0.pack(side=LEFT)
button8_0 = Button(topframe, width=4, height=14, text="G", fg="black",command=value_G0)
button8_0.pack(side=LEFT)
button9_0 = Button(topframe, width=2, height=12, pady=8, bd=8, text="Ab", bg="black", fg="white",command=value_Ab0)
button9_0.pack(side=LEFT)
button10_0 = Button(topframe, width=4, height=14, text="A", fg="black",command=value_A0)
button10_0.pack(side=LEFT)
button11_0 = Button(topframe, width=2, height=12, pady=8, bd=8, text="Bb", bg="black", fg="white",command=value_Bb0)
button11_0.pack(side=LEFT)
button12_0 = Button(topframe, width=4, height=14, text="B", fg="black",command=value_B0)
button12_0.pack(side=LEFT)

button13_0 = Button(topframe, width=4, height=14, text="C", fg="black",command=value_C1)
button13_0.pack(side=LEFT)

frame1 = Frame(root)
frame1.pack(side=TOP)

label1 = Label(frame1, text="Primera nota C "+str(boct))

root.mainloop()







