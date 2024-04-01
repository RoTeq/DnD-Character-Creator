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

import json
from dnd5eutils import *

api = dnd5api.DnD5eAPI()


class Character:
    def __init__(self) -> None:

        #Class Info
        self.initialized = True
        self.data_entered = False
        self.built = False

        #Basic Character Info
        self.Name = "N/A"
        self.Scores = [0,0,0,0,0,0]
        self.Saving_Throws = [0,0,0,0,0,0]
        self.Proficencies = {}
        self.Proficeny_Bonus = 0

        #Character Traits
        self.Race = ''
        self.Languages = []
        self.Traits = {}
        self.Walking_Speed = 0
        self.Size = ''

        #Character Health
        self.Hit_Dice = 0
        self.Health = 0
        self.Current_Health = 0
        self.Armor_Class = 0

        #Levels and Class
        self.Total_Level = 0
        self.Classes = {
            'Barbarian' : 0,
            'Bard' : 0,
            'Cleric' : 0,
            'Druid' : 0,
            'Fighter' : 0,
            'Monk' : 0,
            'Paladin' : 0,
            'Ranger' : 0,
            'Rogue' : 0,
            'Sorcerer' : 0,
            'Warlock' : 0,
            'Wizard' : 0
        }

    def parse(self,json): #TODO Fix for dict values
        """
        Parses a JSON for the character data
        """
        f = open(json,"rt")
        data = f.read()
        data = json.loads(data)

        self.Name = data['Name']
        self.Scores = data['Scores']
        self.Saving_Throws = data['Saving_Throws']
        self.Proficeny_Bonus = data['Proficeny_bonus']
        self.Proficencies = data['Proficencies']
        self.Languages = data['Languages']
        self.Walking_Speed = data['Walking Speed']
        self.Health = data['Health']
        self.Current_Health = data['Current_Health']
        self.Armor_Class = data['Armor_Class']
        self.Total_Level = data['Total_Level']
        self.Size = data['Size']
        self.Barbarian_Level = data['Barbarian_Level']
        self.Bard_Level = data['Bard_Level']
        self.Cleric_Level = data['Cleric_Level']
        self.Druid_Level = data['Druid_Level']
        self.Fighter_Level = data['Fighter_Level']
        self.Monk_level = data['Monk_Level']
        self.Paladin_Level = data['Paladin_Level']
        self.Ranger_Level = data['Ranger_Level']
        self.Rouge_Level = data['Rouge_Level']
        self.Sorcerer_Level = data['Sorcerer_Level']
        self.Warlock_Level = data['Warlock_Level']
        self.Wizard_Level = data['Wizard_Level']
        self.Race = data['Race']
        self.data_entered = True
    
    def Dump(self): #TODO Fix for dict values
        if self.data_entered == False:
            print("[ERROR] Invalid")
        data = {}
        f = open(f"{self.Name}.json",'at')

        data['Name'] = self.Name
        data['Scores'] = self.Scores
        try:
            data['Saving_Throws'] = self.Saving_Throws
            data['Proficeny_bonus'] = self.Proficeny_Bonus
            data['Proficencies'] = self.Proficencies
            data['Languages'] = self.Languages
            data['Walking Speed'] = self.Walking_Speed
            data['Health'] = self.Health
            data['Current_Health'] = self.Current_Health
            data['Armor_Class'] = self.Armor_Class
            data['Size'] = self.Size
        except:
            pass
        data['Total_Level'] = self.Total_Level
        data['Barbarian_Level'] = self.Barbarian_Level
        data['Bard_Level'] = self.Bard_Level
        data['Cleric_Level'] = self.Cleric_Level
        data['Druid_Level'] = self.Druid_Level
        data['Fighter_Level'] = self.Fighter_Level
        data['Monk_Level'] = self.Monk_level
        data['Paladin_Level'] = self.Paladin_Level
        data['Ranger_Level'] = self.Ranger_Level
        data['Rouge_Level'] = self.Rouge_Level
        data['Sorcerer_Level'] = self.Sorcerer_Level
        data['Warlock_Level'] = self.Warlock_Level
        data['Wizard_Level'] = self.Wizard_Level
        data['Race'] = self.Race
        newdata = json.dumps(data)
        f.write(newdata)
        f.close

    def Make(self):
        self.Name = input("What is your name: ")
        self.Race = input("What race are you?: ")
        Class = input("Which class are you? ")
        self.Classes[Class] = 1
        print(f"You Are {self.Name} a {self.Race} {Class} at level 1")
        self.Scores = []
        score_list = self.randomize_scores()
        Labels = ['Strength', 'Dexterity','Constitution','Inteligence','Wisdom','Charisma']
        for y in range(6):
            valid = False
            while valid == False:
                try:
                    x = input(f"Which number is your {Labels[y]} score {score_list}: ")
                    x = int(x)
                    valid = True
                except:
                    print("Invalid number try again")
            for z in range(6):
                if x == score_list[z]:
                    self.Scores.append(x)
                    score_list.pop(z)
                    x = 0
                    break

    def Build(self): #TODO finish
        self.Race_data()        

    def randomize_scores(self) -> list[int]:
        scores = []
        for x in range(6):
            y = dice.dice(number=4,sides=6,drop=('min',1))
            scores.append(y)
        return scores
    
    def modifier_calculator(ability_score:int) -> int:
        if ability_score <= 9:
            modifier = int((ability_score-11)/2)
        else:
            modifier = int((ability_score-10)/2)
        return modifier

    def Race_data(self):
        data = api.request_locale(self.Race.lower())
        self.Walking_Speed = data['speed']
        for bonus in data['ability_bonuses']:
            bonus_cat =bonus['ability_score']['index']
            match bonus_cat:
                case 'str':
                    self.Scores[0]+= bonus['bonus']
            match bonus_cat:
                case 'dex':
                    self.Scores[1]+= bonus['bonus']
            match bonus_cat:
                case 'con':
                    self.Scores[2]+= bonus['bonus']
            match bonus_cat:
                case 'int':
                    self.Scores[3]+= bonus['bonus']
            match bonus_cat:
                case 'wis':
                    self.Scores[4]+= bonus['bonus']
            match bonus_cat:
                case 'cha':
                    self.Scores[5]+= bonus['bonus']
        self.Size = (data['size'])
        for proficency in data['starting_proficiencies']:
            self.Proficencies[proficency['index']] = proficency['url']
        for language in data['languages']:
            self.Languages.append(language['name'])
        for trait in data['traits']:
            self.Traits[trait['name']] = trait['url']
    
    def Class_data(self):  
        data = api.request_locale(self.Class.lower())

        self.Hit_Dice = data['hit_die']

        proficiency_choices = data['proficiency_choices'][0]
        print(proficiency_choices['desc'])
        choices = proficiency_choices['from']['options']
        itemlist = {}
        for item in choices:
            itemlist[item['item']['index'][6:]] = item['item']['index'][6:]
        for prof in range(proficiency_choices['choose']):
            while True:
                choice = input(f"Choice {prof}: ")
                if choice in itemlist:
                    self.Proficencies[choice] = "type-skill"
                    itemlist.pop(choice)
                    break

        for proficiency in data['proficiencies']:
            if 'saving-throw-' in proficiency['index']:
                pass
            else:
                self.Proficencies[proficiency] = "type-equipment"


        for throw in data['saving_throws']:
            print(throw['index'])
        for item in data['starting_equipment']:
            print(f"{item['equipment']['name']} | count: {item['quantity']}")
        for option in data['starting_equipment_options']:
            print(option['desc'])
            for opt in option['from']['options']:
                print(opt)
        
        print(data['class_levels'])