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

from typing import Any, Tuple
import Character_Class
from customtkinter import *

char = Character_Class.Character()

Fonts:dict = {
    'Large' : ('Arial',48),
    'Medium' : ('Arial',24),
    'Mall' : ('Arial',18),
    'Small' : ('Arial',12),
    'Tiny' : ('Arial',6),
}

class traits(CTkFrame):
    def __init__(self, master: Any,Trait,data,**kwargs):
        super().__init__(master,**kwargs)
        CTkLabel(self,text=Trait,font=Fonts['Mall'],padx=10,pady=10).grid(column=0,row=0,sticky=W)
        CTkLabel(self,text=data,justify=LEFT,wraplength=500,font=Fonts['Small'],padx=10,pady=10).grid(column=0,row=2)



class skills(CTkFrame):
    def __init__(self, master: Any,skill,**kwargs):
        super().__init__(master,**kwargs)
        CTkCheckBox(self,text='',width=5,state=DISABLED).grid(column=0,row=0,sticky=W)
        CTkLabel(self,text=f'+{0}',font=Fonts['Mall']).grid(column=1,row=0,sticky=W)
        CTkLabel(self,text=skill,justify=LEFT,wraplength=500,font=Fonts['Mall'],padx=10,pady=10).grid(column=2,row=0,sticky=W)

#submenus
class MainTabs(CTkTabview):
    def __init__(self, master: Any,**kwargs):
        super().__init__(master,**kwargs)
        windth = app.geo
        width = windth[0] - 185
        height = windth[1] - 15
        self.configure(width = width, height = height)

                # create tabs
        self.add("Main Page")
        self.add("How to Use")
        self.set('Main Page')
        
        # Main Page
        CTkLabel(master=self.tab("Main Page"),text='Main page of info').grid(row=0, column=0, padx=20, pady=10)

        # How to use
        CTkLabel(master=self.tab("How to Use"),text='Manual').grid(row=0, column=0, padx=20, pady=10)

class charTabs(CTkTabview):
    def __init__(self, master: Any,**kwargs):
        super().__init__(master,**kwargs)
        windth = app.geo
        width = windth[0] - 185
        height = windth[1] - 15
        self.configure(width = width, height = height)

                # create tabs
        self.add("Overview")
        self.add("Inventory")
        self.add("Skills")
        self.add("Features")
        self.add("Spellcasting")
        self.add('Import/Export')
        if char.data['Name'] != 'N/A':
            self.set("Overview")
        else:
            self.set('Import/Export')
        

        # Overview
        CTkLabel(master=self.tab("Overview"),text=char.data['Name'],font=Fonts['Large']).grid(row=0, column=0, padx=20, pady=20)
        CTkLabel(master=self.tab("Overview"),text=char.data['Race'],font=Fonts['Large']).grid(row=0, column=1, padx=20, pady=20)
        CTkLabel(master=self.tab("Overview"),text=f"{char.data['Starting_Class']} {char.data['Total_Level']}",font=Fonts['Large']).grid(row=0, column=2, padx=20, pady=20)
        #Overview.Scores
        scoreframe = CTkFrame(master=self.tab("Overview"))
        #STRength
        strframe = CTkFrame(master=scoreframe,border_width=2)
        CTkLabel(strframe,text="Strength",font=Fonts['Medium']).pack(pady = 10)
        CTkLabel(strframe,text=char.data['Scores']['str'],font=Fonts['Medium']).pack()
        strframe.grid(row = 1, column = 0,ipadx = 10,ipady=10,pady = 10)
        #DEXterity
        dexframe = CTkFrame(master=scoreframe,border_width=2)
        CTkLabel(dexframe,text="Dexterity",font=Fonts['Medium']).pack(pady = 10)
        CTkLabel(dexframe,text=char.data['Scores']['dex'],font=Fonts['Medium']).pack()
        dexframe.grid(row = 1, column = 1,ipadx = 10,ipady=10,pady = 10)
        #CONstitution
        conframe = CTkFrame(master=scoreframe,border_width=2)
        CTkLabel(conframe,text="Constitution",font=Fonts['Medium']).pack(pady = 10)
        CTkLabel(conframe,text=char.data['Scores']['con'],font=Fonts['Medium']).pack()
        conframe.grid(row = 1, column = 2,ipadx = 10,ipady=10,pady = 10)
        #INTeligence
        intframe = CTkFrame(master=scoreframe,border_width=2)
        CTkLabel(intframe,text="Inteligence",font=Fonts['Medium']).pack(pady = 10)
        CTkLabel(intframe,text=char.data['Scores']['int'],font=Fonts['Medium']).pack()
        intframe.grid(row = 1, column = 3,ipadx = 10,ipady=10,pady = 10)
        #WISdom
        wisframe = CTkFrame(master=scoreframe,border_width=2)
        CTkLabel(wisframe,text="Wisdom",font=Fonts['Medium']).pack(pady = 10)
        CTkLabel(wisframe,text=char.data['Scores']['wis'],font=Fonts['Medium']).pack()
        wisframe.grid(row = 1, column = 4,ipadx = 10,ipady=10,pady = 10)
        #CHArisma
        chaframe = CTkFrame(master=scoreframe,border_width=2)
        CTkLabel(chaframe,text="Charisma",font=Fonts['Medium']).pack(pady = 10)
        CTkLabel(chaframe,text=char.data['Scores']['cha'],font=Fonts['Medium']).pack()
        chaframe.grid(row = 1, column = 5,ipadx = 10,ipady=10,pady = 10)
        scoreframe.grid(row=1,column = 0,columnspan = 3)


        #stats
        statsframe = CTkFrame(master=self.tab("Overview"))
        #Health
        hpframe = CTkFrame(master=statsframe,border_width=2)
        CTkLabel(hpframe,text="Health",font=Fonts['Medium']).pack(pady = 10)
        CTkLabel(hpframe,text=f"{char.data['Current_Health']}/{char.data['Health']}",font=Fonts['Medium']).pack()
        hpframe.grid(row = 0, column = 0,ipadx = 10,ipady=10,pady = 10,padx = 10)
        #Armor Class
        acframe = CTkFrame(master=statsframe,border_width=2)
        CTkLabel(acframe,text="Armor Class",font=Fonts['Medium']).pack(pady = 10)
        CTkLabel(acframe,text=char.data['Armor_Class'],font=Fonts['Medium']).pack()
        acframe.grid(row = 0, column = 1,ipadx = 10,ipady=10,pady = 10,padx = 10)
        #Walking Speed
        walkframe = CTkFrame(master=statsframe,border_width=2)
        CTkLabel(walkframe,text="Speed",font=Fonts['Medium']).pack(pady = 10)
        CTkLabel(walkframe,text=char.data['Walking_Speed'],font=Fonts['Medium']).pack()
        walkframe.grid(row = 0, column = 2,ipadx = 10,ipady=10,pady = 10,padx = 10)
        #Death Saves
        saveframe = CTkFrame(master=statsframe,border_width=2)
        CTkLabel(saveframe,text="Saves",font=Fonts['Medium']).grid(column=0,row=0,pady=10)
        dataframe = CTkFrame(saveframe)
        #Successes
        CTkLabel(dataframe,text='Successes',font=Fonts["Mall"]).grid(column=0,row=0,padx=5)
        CTkCheckBox(dataframe,text=' ',width=5).grid(column=1,row=0,)
        CTkCheckBox(dataframe,text=' ',width=5).grid(column=2,row=0,)
        CTkCheckBox(dataframe,text=' ',width=5).grid(column=3,row=0,)
        #Fails
        CTkLabel(dataframe,text='Failures',font=Fonts["Mall"]).grid(column=0,row=1,padx=5)
        CTkCheckBox(dataframe,text=' ',width=5).grid(column=1,row=1,)
        CTkCheckBox(dataframe,text=' ',width=5).grid(column=2,row=1,)
        CTkCheckBox(dataframe,text=' ',width=5).grid(column=3,row=1,)
        dataframe.grid(column=0,row=1,padx=10)
        saveframe.grid(row = 0, column = 3,ipadx = 10,ipady=10,pady = 10,padx = 10)
        statsframe.grid(row=3,column = 0,columnspan = 3)


        # Inventory
        CTkLabel(master=self.tab("Inventory"),text='Inventory').grid(row=0, column=0, padx=20, pady=10)


        # Skills
        # Strength
        strskilfrm = CTkFrame(self.tab("Skills"))
        CTkLabel(strskilfrm,text='Strength',font=Fonts['Medium']).grid(row=0,column=0)
        skills(strskilfrm,"Athletics").grid(row=1,column=0,sticky=W)
        strskilfrm.grid(row=3, column=0,columnspan=1, padx=20, pady=10,sticky=EW)
        # Dexterity
        dexskilfrm = CTkFrame(self.tab("Skills"))
        CTkLabel(dexskilfrm,text='Dexterity',font=Fonts['Medium']).grid(row=0,column=0)
        skills(dexskilfrm,"Acrobatics").grid(row=1,column=0,sticky=W)
        skills(dexskilfrm,"Sleight of Hand").grid(row=2,column=0,sticky=W)
        skills(dexskilfrm,"Stealth").grid(row=3,column=0,sticky=W)
        dexskilfrm.grid(row=1, column=0, padx=20, pady=10,sticky=W)
        # Constitution
            # Ha i thought this was gonna be a thing T-T (Honestly shows how much I know about D&D lmao)
        # Inteligence
        intskilfrm = CTkFrame(self.tab("Skills"))
        CTkLabel(intskilfrm,text='Inteligence',font=Fonts['Medium']).grid(row=0,column=0)
        skills(intskilfrm,"Arcana").grid(row=1,column=0,sticky=W)
        skills(intskilfrm,"History").grid(row=2,column=0,sticky=W)
        skills(intskilfrm,"Investigation").grid(row=3,column=0,sticky=W)
        skills(intskilfrm,"Nature").grid(row=4,column=0,sticky=W)
        skills(intskilfrm,"Religion").grid(row=5,column=0,sticky=W)
        intskilfrm.grid(row=0, column=2, padx=20, pady=10,sticky=W)
        # Wisdom
        wisskilfrm = CTkFrame(self.tab("Skills"))
        CTkLabel(wisskilfrm,text='Wisdom',font=Fonts['Medium']).grid(row=0,column=0)
        skills(wisskilfrm,"Animal Handling").grid(row=1,column=0,sticky=W)
        skills(wisskilfrm,"Insight").grid(row=2,column=0,sticky=W)
        skills(wisskilfrm,"Medicine").grid(row=3,column=0,sticky=W)
        skills(wisskilfrm,"Perception").grid(row=4,column=0,sticky=W)
        skills(wisskilfrm,"Survival").grid(row=5,column=0,sticky=W)
        wisskilfrm.grid(row=1, column=2, padx=20, pady=10,sticky=W)
        #Charisma
        chaskilfrm = CTkFrame(self.tab("Skills"))
        CTkLabel(chaskilfrm,text='Charisma',font=Fonts['Medium']).grid(row=0,column=0)
        skills(chaskilfrm,"Deception").grid(row=1,column=0,sticky=W)
        skills(chaskilfrm,"Intimidation").grid(row=2,column=0,sticky=W)
        skills(chaskilfrm,"Performance").grid(row=3,column=0,sticky=W)
        skills(chaskilfrm,"Persuasion").grid(row=4,column=0,sticky=W)
        chaskilfrm.grid(row=0, column=0, padx=20, pady=10)


        # Features
        traitframe = CTkFrame(self.tab("Features"),width=app.geo[0]-170,height=app.geo[1]-50)
        i=0
        for Trait,data in char.data['Traits'].items():
            traits(traitframe,Trait,data).grid(column=0,row=i,sticky=W,pady=10,padx=10)
            i += 1
        traitframe.grid(column=0,row=0,sticky=E)


        # Spellcasting
        CTkLabel(master=self.tab("Spellcasting"),text='Spellcasting').grid(row=0, column=0, padx=20, pady=10)
        

        #Import/Export
        self.grid_columnconfigure(0,weight=1)
        self.import_path = CTkEntry(master=self.tab("Import/Export"),placeholder_text='Import Path')
        self.import_path.grid(row=0, column=0, padx=20, pady=10)
        CTkButton(master=self.tab("Import/Export"),text='Import',command=lambda: self.parse()).grid(row=1, column=0, padx=20, pady=10)

    def parse(self):
        path = self.import_path.get()
        char.parse(f"Characters\\{path}.json")
        Menuframe.tabs = charTabs(app.mainframe).grid(row=0,column=1,padx = 10,sticky = NW)



class helpTabs(CTkTabview):
    def __init__(self, master: Any,**kwargs):
        super().__init__(master,**kwargs)
        windth = app.geo
        width = windth[0] - 185
        height = windth[1] - 15
        self.configure(width = width, height = height)

                # create tabs
        self.add("Github")
        self.add("Contact Me")
        self.add("Legal")
        self.set('Github')
        
        # Github
        CTkLabel(master=self.tab("Github"),text='Github').grid(row=0, column=0, padx=20, pady=10)

        # Contact me
        CTkLabel(master=self.tab("Contact Me"),text='How to Contact me').grid(row=0, column=0, padx=20, pady=10)

        # Legal
        CTkLabel(master=self.tab("Legal"),text='GPL-v3').grid(row=0, column=0, padx=20, pady=10)

class settingsTabs(CTkTabview):
    def __init__(self, master: Any,**kwargs):
        super().__init__(master,**kwargs)
        windth = app.geo
        width = windth[0] - 185
        height = windth[1] - 15
        self.configure(width = width, height = height)

                # create tabs
        self.add("General")
        self.add("Future")
        self.set('General')
        
        # General
        CTkLabel(master=self.tab("General"),text='General Settings').grid(row=0, column=0, padx=20, pady=10)

        # Future
        CTkLabel(master=self.tab("Future"),text='Future').grid(row=0, column=0, padx=20, pady=10)


#layout
class Menuframe(CTkFrame):
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, **kwargs)

                # Widgets Here
        CTkButton(self,text='Main Menu',command=main_menu).grid(row=0,column=0,pady=10)
        CTkButton(self,text='Character',command=character_menu).grid(row=1,column=0,pady=10)
        CTkButton(self,text='Help',command=help_menu).grid(row=2,column=0)
        CTkButton(self,text='Settings',command=settings_menu).grid(row=3,column=0,pady=10)

class Mainframe(CTkFrame):
    def __init__(self, master: Any,**kwargs):
        super().__init__(master,**kwargs)
        self.grid_columnconfigure(0,weight=0)
        self.grid_columnconfigure(1,weight=3)

                # Widgets Here
        self.menuframe = Menuframe(self).grid(row=0,column=0,pady=10,padx=10,sticky = N)

class App(CTk):
    def __init__(self, Name:str, Geometry:tuple[int, int], fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.geo = Geometry
        self.geometry(f"{Geometry[0]}x{Geometry[1]}")
        self.title(Name)
        self.minsize(Geometry[0],Geometry[1])
        self.maxsize(Geometry[0],Geometry[1])
        self.mainframe = Mainframe(master=self).grid()


#Menu Switching
def character_menu():
    Menuframe.tabs = charTabs(app.mainframe).grid(row=0,column=1,padx = 10,sticky = NW)
def main_menu():
    Menuframe.tabs = MainTabs(app.mainframe).grid(row=0,column=1,padx = 10,sticky = NW)
def help_menu():
    Menuframe.tabs = helpTabs(app.mainframe).grid(row=0,column=1,padx = 10,sticky = NW)
def settings_menu():
    Menuframe.tabs = settingsTabs(app.mainframe).grid(row=0,column=1,padx = 10,sticky = NW)



geo1 = 1920,1020
geo2 = 1000,700

app = App(Name='D&D Character Creator',Geometry=geo2)
app.mainloop()
