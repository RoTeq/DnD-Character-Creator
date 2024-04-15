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



class charTabs(CTkTabview):
    def __init__(self, master: Any,**kwargs):
        super().__init__(master,**kwargs)
        
                # create tabs
        self.add("Overview")
        self.add("Inventory")
        self.add("Skills")
        self.add("Features")
        self.add("Spellcasting")
        self.add('Import/Export')
        self.set('Import/Export')

        # Overview
        CTkLabel(master=self.tab("Overview"),text='Overview').grid(row=0, column=0, padx=20, pady=10)

        # Inventory
        CTkLabel(master=self.tab("Inventory"),text='Inventory').grid(row=0, column=0, padx=20, pady=10)

        # Skills
        CTkLabel(master=self.tab("Skills"),text='Skills').grid(row=0, column=0, padx=20, pady=10)

        # Features
        CTkLabel(master=self.tab("Features"),text='Features').grid(row=0, column=0, padx=20, pady=10)

        # Spellcasting
        CTkLabel(master=self.tab("Spellcasting"),text='Spellcasting').grid(row=0, column=0, padx=20, pady=10)


class Menuframe(CTkFrame):
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, **kwargs)

                # Widgets Here
        CTkButton(self,text='Main Menu').grid(row=0,column=0,pady=10)
        CTkButton(self,text='Character',command=self.character).grid(row=1,column=0,pady=10)
        CTkButton(self,text='Help').grid(row=2,column=0)
        CTkButton(self,text='Settings').grid(row=3,column=0,pady=10)


    def character(self):
        charTabs(self).grid(row=0,column=1)

class Mainframe(CTkFrame):
    def __init__(self, master: Any,**kwargs):
        super().__init__(master,**kwargs)

                # Widgets Here
        menuframe = Menuframe(self).grid(row=0,column=0,pady=10,padx=10)
        tabs = charTabs(self).grid(row=0,column=1)


class App(CTk):
    def __init__(self, Name:str, Geometry:tuple[int, int], fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.geometry(f"{Geometry[0]}x{Geometry[1]}")
        self.title(Name)
        self.mainframe = Mainframe(master=self).pack()




app = App(Name='D&D Character Creator',Geometry=(800,500))
app.mainloop()
