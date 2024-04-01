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

from dnd5api import DnD5eAPI


class spell():
    def __init__(self,data) -> None:
        self.index = data["index"]
        self.name = data["name"]
        self.url = data["url"]
        self.url = self.url[5:]

    def details(self) -> None:
        """
        Call the details for the spell object
        """
        data = api.request(self.url)
        description = data['desc']
        self.description = description[0]
        self.higher_level = data['higher_level']
        self.range = data['range']
        self.components = data['components']
        try:
            self.material = data['material']
        except:
            self.material = "None"
        self.ritual = data['ritual']
        self.duration = data['duration']
        self.concentration = data['concentration']
        self.casting_time = data['casting_time']
        self.level = data['level']
        self.school = data['school']
        self.classes = data['classes']
        self.subclasses = data['subclasses']

    def __str__(self) -> str:
        self.details()
        if len(self.classes) > 1:
            self.class_list = []
            for x in self.classes:
                self.class_list.append(x['name'])
        else:
            self.class_list = self.classes['name']
        #if len(self.subclasses) > 1:
        #    self.subclass_list = []
        #    for x in self.subclasses:
        #        self.subclass_list.append(x['name'])
        #else:
        #    self.subclass_list = self.subclasses[0]['name']
        return f"""
{self.name} | School of {self.school['name']} | Spell Slot Size: {self.level}

Requirments:
{self.components} | Material: {self.material} | Ritual: {self.ritual} | Concentration: {self.concentration} | Range: {self.range}

Use:
Casting Time: {self.casting_time} | Duration: {self.duration} 

{self.description}

{self.higher_level}

Can be used by:
classes: {self.class_list}
"""


class spellbook():
    def __init__(self) -> None:
        self.spell_list = {}
        location = "spells"
        spell_data = api.request(location)
        self.count = spell_data["count"]
        spell_data = spell_data["results"]
        for spells in spell_data:
            s = spell(spells)
            name = s.name.lower()
            self.spell_list[name] = s
    
    def list_all(self):
        for spell in self.spell_list:
            s = self.spell_list[spell]
            print(s.name)
            

    def Details(self,spell):
        spell = spell.lower()
        s = self.spell_list[spell]
        print(s)

api = DnD5eAPI()



