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

from libref import api
import json

file = "James Teq.json"

f = open(file,'rt')
dat = f.read()
data = json.loads(dat)
inven = {}

def unpack_inventory(inventory):
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
                        pack = unpack_inventory(dat['contents'])
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


data['Inventory'] = unpack_inventory(data['Inventory'])


print()
print(data['Inventory'])
