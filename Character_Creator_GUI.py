#DnD Character Creator
#    Copyright (C) 2024  Jacob Feldman
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

import Character_Class
from tkinter import *
from tkinter import ttk as ttk
from customtkinter import *

overview = True

Pallete:dict = {
    'red1' : '#670A18',
    'red2' : '#890E20',
    'red3' : '#AB1128',
    'red4' : '#F7193A',
    'red5' : '#EF1838',
    'red6' : '#F7193A',
    'black' : '#000000',
    'white' : '#FFFFFF',
    'gray' : '#332C2D'
}

Fonts:dict = {
    'Large' : ('Arial',24),
    'Medium' : ('Arial',18),
    'Small' : ('Arial',12),
    'Tiny' : ('Arial',6),
}

def donothing():
    filewin = Toplevel(Root)
    button = Button(filewin, text='Not Implemented yet')
    button.pack()

#Character Data
char = Character_Class.Character()

#Character Menu Functions
def new():
    donothing()

def open():
    char.parse('Characters\\James Teq.json')
    overview(True)

def save():
    donothing()

def save_as():
    donothing()

def export():
    donothing()



#Main Windows

def overview(on:bool):
    if on == True:
        frm = CTkFrame(Root)
        frm.grid(column=1,row=0,sticky=NSEW)
        CTkLabel(frm,text='Overview',font=Fonts['Large']).grid(column=0,row=0,sticky=NW)
        CTk
        datafrm = CTkFrame(frm)
        
        #Row 1 Basic Character Info

        CTkLabel(datafrm,text=char.data['Name'],font=Fonts['Medium']).grid(column=0,row=0,sticky=W)
        CTkLabel(datafrm,text=char.data['Race'],font=Fonts['Medium']).grid(column=1,row=0,padx=10,sticky=W)
        CTkLabel(datafrm,text=f"{char.data['Starting_Class']} {char.data['Total_Level']}",font=Fonts['Medium']).grid(column=2,row=0,sticky=W)

        #Row 2 Scores
        scoresfrm = CTkFrame(datafrm)
        scoresfrm.columnconfigure(0,pad=10)
        scoresfrm.columnconfigure(1,pad=10)
        scoresfrm.columnconfigure(2,pad=10)
        scoresfrm.columnconfigure(3,pad=10)
        scoresfrm.columnconfigure(4,pad=10)
        scoresfrm.columnconfigure(5,pad=10)
        #Strengh
        strframe = CTkFrame(scoresfrm)
        CTkLabel(strframe,text='Strength',font=Fonts['Small']).grid(row=0)
        CTkLabel(strframe,text=char.data['Scores']['str'],font=Fonts['Small']).grid(row=1)
        strframe.grid(column=0,row=0)
        #Dexterity
        dexframe = CTkFrame(scoresfrm)
        CTkLabel(dexframe,text='Dexterity',font=Fonts['Small']).grid(row=0)
        CTkLabel(dexframe,text=char.data['Scores']['dex'],font=Fonts['Small']).grid(row=1)
        dexframe.grid(column=1,row=0)
        #Constitution
        conframe = CTkFrame(scoresfrm)
        CTkLabel(conframe,text='Constitution',font=Fonts['Small']).grid(row=0)
        CTkLabel(conframe,text=char.data['Scores']['con'],font=Fonts['Small']).grid(row=1)
        conframe.grid(column=2,row=0)
        #Inteligence
        intframe = CTkFrame(scoresfrm)
        CTkLabel(intframe,text='Inteligence',font=Fonts['Small']).grid(row=0)
        CTkLabel(intframe,text=char.data['Scores']['int'],font=Fonts['Small']).grid(row=1)
        intframe.grid(column=3,row=0)
        #Wisodm
        wisframe = CTkFrame(scoresfrm)
        CTkLabel(wisframe,text='Wisdom',font=Fonts['Small']).grid(row=0)
        CTkLabel(wisframe,text=char.data['Scores']['wis'],font=Fonts['Small']).grid(row=1)
        wisframe.grid(column=4,row=0)
        #Charisma
        chaframe = CTkFrame(scoresfrm)
        CTkLabel(chaframe,text='Constitution',font=Fonts['Small']).grid(row=0)
        CTkLabel(chaframe,text=char.data['Scores']['cha'],font=Fonts['Small']).grid(row=1)
        chaframe.grid(column=5,row=0)


        scoresfrm.grid(column=0,row=1,columnspan=3,pady=20)
        datafrm.grid(column=0,row=1,pady=10)

    Root.mainloop()

def inventory(on:bool):
    if on == True:
        frm = CTkFrame(Root)
        frm.grid(column=1,row=0,sticky=NSEW,padx=10)
        CTkLabel(frm,text='Inventory',font=Fonts['Large']).grid(column=0,row=0,sticky=NW)
        datafrm = CTkFrame(frm,padding=10,relief=SUNKEN)

        #TODO inventory
        
        datafrm.grid(column=0,row=1,pady=10)
    Root.mainloop()

def skills(on:bool):
    if on == True:
        frm = CTkFrame(Root)
        frm.grid(column=1,row=0,sticky=NSEW,padx=10)
        CTkLabel(frm,text='Skills',font=Fonts['Large']).grid(column=0,row=0,sticky=NW)
        datafrm = CTkFrame(frm,padding=10,relief=SUNKEN)

        #TODO Skills
        
        datafrm.grid(column=0,row=1,pady=10)
    Root.mainloop()

def features(on:bool):
    if on == True:
        frm = CTkFrame(Root)
        frm.grid(column=1,row=0,sticky=NSEW,padx=10)
        CTkLabel(frm,text='Features',font=Fonts['Large']).grid(column=0,row=0,sticky=NW)
        datafrm = CTkFrame(frm,padding=10,relief=SUNKEN)

        #TODO Features
        
        datafrm.grid(column=0,row=1,pady=10)
    Root.mainloop()

def spellcasting(on:bool):
    if on == True:
        frm = CTkFrame(Root)
        frm.grid(column=1,row=0,sticky=NSEW,padx=10)
        CTkLabel(frm,text='Spellcasting',font=Fonts['Large']).grid(column=0,row=0,sticky=NW)
        datafrm = CTkFrame(frm,padding=10,relief=SUNKEN)

        #TODO Spellcasting
        
        datafrm.grid(column=0,row=1,pady=10)
    Root.mainloop()




#Geometry

#main window
Root = CTk()
Root.title(' D&D Character Creator')
Root.geometry('800x300')

Root.grid_columnconfigure(0,weight=0)
Root.grid_columnconfigure(1,weight=1)

#sidebar
sidebar = CTkFrame(Root)
sidebar.grid(column=0,row=0,sticky=NS)
CTkButton(sidebar,text='Overview',command=lambda :overview(True)).pack(pady=5)
CTkButton(sidebar,text='Inventory',command=lambda :inventory(True)).pack(pady=5)
CTkButton(sidebar,text='Skills',command=lambda :skills(True)).pack(pady=5)
CTkButton(sidebar,text='Features',command=lambda :features(True)).pack(pady=5)
CTkButton(sidebar,text='Spellcasting',command=lambda: spellcasting(True)).pack(pady=5)


overview(True) #starts on the overview screen
Root.mainloop()
