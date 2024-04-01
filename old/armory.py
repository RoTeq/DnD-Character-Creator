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

import dnd5api

api = dnd5api.DnD5eAPI()

class item():
    def __init__(self,data) -> None:
        self.index = data["index"]
        self.name = data["name"]
        self.url = data["url"]
        self.url = self.url[5:]
    
    def data(self):
        data = api.request(self.url)
        print(data)
        self.desc = data['desc']
        self.special = data['special']
        self.category = data['equipment_category']
        



class armory():
    def __init__(self) -> None:
        self.all_equipment()
        #self.equipment_categories()

    def all_equipment(self):
        self.url1 = "equipment"
        request = api.request(self.url1)
        self.equpment_count = request['count']
        self.data1 = request['results']
        self.equipment_list = {}
        for i in self.data1:
            it = item(i)
            self.equipment_list[it.index] = it

    def equipment_categories(self):
        self.url2 = "equipment-categories"
        request = api.request(self.url2)
        self.category_count = request['count']
        self.data2 = request['results']
        self.category_list = {}
        for i in self.data2:
            self.category_list[i] = i

    def list_all(self):
        for item in self.equipment_list:
            it = self.equipment_list[item]
            print(it.name)
    
    def details(self,item):
        it = self.equipment_list[item]
        it.data()

arms = armory()

arms.details("whip")