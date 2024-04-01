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


from Libs.dice import dice
from Libs.dnd5api import DnD5eAPI
import json

api = DnD5eAPI()

class Character():
    def __init__(self) -> None:
        self.Labels = ['Strength', 'Dexterity','Constitution','Inteligence','Wisdom','Charisma']
        self.score_num = {
            0 : 'str',
            1 : 'dex',
            2 : 'con',
            3 : 'int',
            4 : 'wis',
            5 : 'cha'
        }
        self.data = {
            'initialized' : False,
            'made' : False,
            'built' : False,
    
            #Basic Character Info
            'Name' : "N/A",
            'Race' : '',

            #Inventory
            'Inventory' : {},
            'future_aditions' : [],

            #Number Things
            'Scores' : {
                'str' : 0,
                'dex' : 0,
                'con' : 0,
                'int' : 0,
                'wis' : 0,
                'cha' : 0
            },
            'Saving_Throws' : {
                'str' : 0,
                'dex' : 0,
                'con' : 0,
                'int' : 0,
                'wis' : 0,
                'cha' : 0
            },
            'Proficencies': {},
            'Proficeny_Bonus' : 0,
    
            #Character Traits
            'Languages' : [],
            'Traits' : {},
            'Walking_Speed' : 0,
            'Size' : '',
    
            #Character Health
            'Hit_Dice' : 0,
            'Health' : 0,
            'Current_Health' : 0,
            'Armor_Class' : 0,
    
            #Levels and Class
            'Total_Level' : 0,
            'Multiclassing' : False,
            'Starting_Class' : '',
            'Classes' : {
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
        }
        self.data['initialized'] = True

    def dump(self,folder:str = 'Characters'):
        dat = self.data
        js = json.dumps(dat)
        filename = f"{folder}\\{self.data['Name']}.json"
        f = open(f"{filename}",'wt')
        f.write(js)
    
    def parse(self, Json_File):
        f = open(Json_File,'rt')
        data = f.read()
        self.data = json.loads(data)

    def create(self):
        self.data['Name'] = input("What is your name: ")
        self.data['Race'] = input("What race are you?: ")
        self.data['Starting_Class'] = input("Which class are you? ")
        self.data['Classes'][self.data['Starting_Class']] = 1
        print(f"You Are {self.data['Name']} a {self.data['Race']} {self.data['Starting_Class']} at level 1")
        self.data['Total_Level'] += 1
        score_list = self.randomize_scores()
        print()
        print("Choose Scores by index starting from 0")
        for score in range(6):
            valid = False
            while valid == False:
                print(f"[0,  1,  2,  3,  4,  5,]")
                choice = input(f"{score_list} choose {self.Labels[score]}: ")
                choice = int(choice)
                if choice < (6-score):
                    self.data['Scores'][self.score_num[score]] = score_list[choice]
                    score_list.pop(choice)
                    valid = True
                else:
                    print("Please try again")

    def grab_race_data(self):
        data = api.request_locale(self.data['Race'].lower())
        self.data['Walking_Speed'] = data['speed']
        self.data['Size'] = data['size']
        for bonus in data['ability_bonuses']:
            bonus_cat =bonus['ability_score']['index']
            self.data['Scores'][bonus_cat]+= bonus['bonus']
        self.Size = (data['size'])
        for proficency in data['starting_proficiencies']:
            self.data['Proficencies'][proficency['index'][6:]] = 'type-skill'
        for language in data['languages']:
            self.data['Languages'].append(language['name'])
        for trait in data['traits']:
            self.data['Traits'][trait['name']] = trait['url']

    def grab_class_data(self):
        data = api.request_locale(self.data['Starting_Class'].lower())
        self.data['Hit_Dice'] = data['hit_die']
        proficiency_choices = data['proficiency_choices'][0]
        print(proficiency_choices['desc'])
        choices = proficiency_choices['from']['options']
        itemlist = {}
        for item in choices:
            itemlist[item['item']['index'][6:]] = item['item']['index'][6:]
        for prof in range(proficiency_choices['choose']):
            while True:
                choice = input(f"Choice {prof}: ")
                choice = choice.lower()
                if choice in itemlist:
                    self.data['Proficencies'][choice] = "type-skill"
                    itemlist.pop(choice)
                    break
        for proficiency in data['proficiencies']:
            if 'saving-throw-' in proficiency['index']:
                pass
            else:
                self.data['Proficencies'][proficiency['name']] = "type-equipment"
        for throw in data['saving_throws']:
            self.data['Saving_Throws'][throw['index']] += 1

        for item in data['starting_equipment']:
            it = {
                'Name': item['equipment']['name'],
                'count' : item['quantity'],
                'url' : item['equipment']['url']
            }
            self.data['Inventory'][it['Name']] = it
        for option in data['starting_equipment_options']:
            print(option['desc'])
            print()
            option_list = []
            for opt in option['from']['options']:
                option_list.append(opt)
            choice = input("Which item (by index): ")
            if choice == 'a':
                choice = 0
            if choice == 'b':
                choice = 1
            if choice == 'c':
                choice = 2
            o = option_list[choice]
            if o['option_type'] == 'counted_reference':
                it = {
                    'Name': o['of']['name'],
                    'count' : o['count'],
                    'url' : o['of']['url']
                }
                self.data['Inventory'][it['Name']] = it
            if o['option_type'] == 'multiple':
                for ite in o['items']:
                    it = {
                    'Name': ite['of']['name'],
                    'count' : ite['count'],
                    'url' : ite['of']['url']
                    }
                    self.data['Inventory'][it['Name']] = it

    def make(self):
        self.grab_race_data()
        self.grab_class_data()
        self.data['made'] = True

    def unpack_inventory(self,inventory):
        inven = {}
        for item in inventory:
            try:
                dat = api.url_call(inventory[item]['url'])
            except:
                dat = api.url_call(item['item']['url'])
            match dat['equipment_category']['index']:
                case 'armor':
                    armor = {
                        'name' : dat['name'],
                        'type' : ('armor'),
                        'armor_class' : dat['armor_class']['base'],
                        'dex_bonus' : dat['armor_class']['dex_bonus'],
                        'str_minimum' : dat['str_minimum'],
                        'stealth_disadvantage' : dat['stealth_disadvantage'],
                        'weight' : dat['weight'],
                        'cost' : (dat['cost']['quantity'],dat['cost']['unit']),
                        #'count' : item['count']
                    }
                    inven[armor['name']] = armor
                case 'weapon':
                    weapon = {
                        'name' : dat['name'],
                        'type' : ('weapon',dat['weapon_category'],dat['weapon_range']),
                        'cost' : (dat['cost']['quantity'],dat['cost']['unit']),
                        #'count' : item['count'],
                        'damage' : {
                            'dice' : (dat['damage']['damage_dice'].split('d')[0],dat['damage']['damage_dice'].split('d')[1]),
                            'type' : dat['damage']['damage_type']['name']
                        },
                        'range' : {
                            'normal' : dat['range']['normal']
                        },
                        'weight' : dat['weight']
                    }
                    try:
                        weapon['range']['long'] = dat['range']['long']
                    except:
                        pass
                    try:
                        weapon['throw_range']['normal'] = dat['throw_range']['normal']
                        weapon['throw_range']['long'] = dat['throw_range']['long']
                    except:
                        pass
                    inven[weapon['name']] = weapon
                case 'tools':
                    tool = {
                        'name' : dat['name'],
                        'type' : ('tool'),
                        'cost' : (dat['cost']['quantity'],dat['cost']['unit']),
                        'desc' : dat['desc'],
                        #'count' : item['count']
                    }
                    inven[tool['name']] = tool
                case 'adventuring-gear':
                    match dat['gear_category']['index']:
                        case 'equipment-packs':
                            pack = self.unpack_inventory(dat['contents'])
                            for i in pack:
                                inven[pack[i]['name']] = pack[i]
                        case _:
                            gear = {
                                'name' : dat['name'],
                                'type' : (dat['gear_category']['index']),
                                'cost' : (dat['cost']['quantity'],dat['cost']['unit']),
                                #'count' : dat['count']
                            }
                            inven[gear['name']] = gear
        return inven

    def build(self):
        for trait in self.data['Traits']:
            dat = api.url_call(self.data['Traits'][trait])
            self.data['Traits'][trait] = dat['desc'][0]
        self.data['Inventory'] = self.unpack_inventory(self.data['Inventory'])     

    def randomize_scores(self) -> list[int]:
        scores = []
        for x in range(6):
            y = dice(number=4,sides=6,drop=('min',1))
            scores.append(y)
        return scores

    def modifier_calculator(ability_score:int) -> int:
        if ability_score <= 9:
            modifier = int((ability_score-11)/2)
        else:
            modifier = int((ability_score-10)/2)
        return modifier


