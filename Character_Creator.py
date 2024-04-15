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


help = f"""
help: This command
character: prints current character loaded
full: shows all the data for the loaded character
create: Make a new character
make: Add the basic details of the character
build: fill out the character data
save: save the characters data to a json
load: load a character from a json
"""

warranty = f"""
  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.
"""

def show_char_data(char:Character_Class.Character):
    name = char.data['Name']
    race = char.data['Race']
    clas = char.data['Starting_Class']
    level = char.data['Total_Level']
    print()
    str1 = f"│ {name} │ {race} │"
    str2 = f"│ level {level} {clas} │"
    longer = len(str1) - len(str2)
    if longer >= 0:
        ref = f"│ {name} │ {race} │"
        str2 = f"│ level {level} {clas}{' '*(len(str1)-len(str2))} │"
        str1 = f"│ {name} │ {race} |"
        block = f"├{'─'*(len(name)+2)}┴{'─'*(len(race)+2)}┤"
        top = f"┌{'─'*(len(name)+2)}┬{'─'*(len(race)+2)}┐"
        bottom = f"└{'─'*(len(ref)-2)}┘"
    else:
        ref = f"│ level {level} {clas} │"
        str1 = f"│ {name}{' '*(len(str2)-len(str1))} │ {race} │"
        str2 = f"│ level {level} {clas} │"
        block = f"├{'─'*4}{'─'*(len(str(level))+2)}┴{'─'*(len(clas)+2)}┤"
        top = f"┌{'─'*4}{'─'*(len(str(level))+2)}┬{'─'*(len(clas)+2)}┐"
        bottom = f"└{'─'*(len(ref)-2)}┘"
    print(top)
    print(str1)
    print(block)
    print(str2)
    print(bottom)
    print()


def show_full_char(char:Character_Class.Character):
    name = char.data['Name']
    race = char.data['Race']
    clas = char.data['Starting_Class']
    level = char.data['Total_Level']
    scores = char.data['Scores']
    print()

    str1 = f"│ {name} │ {race} │"
    str2 = f"│ level {level} {clas} │"

    longer = len(str1) - len(str2)
    if longer >= 0:
        ref = f"│ {name} │ {race} │"
        str2 = f"│ level {level} {clas}{' '*(len(str1)-len(str2))} │ {scores['str']}{' '*(3-len(str(scores['str'])))} │ {scores['dex']}{' '*(3-len(str(scores['dex'])))} │ {scores['con']}{' '*(3-len(str(scores['con'])))} │ {scores['int']}{' '*(3-len(str(scores['int'])))} │ {scores['wis']}{' '*(3-len(str(scores['wis'])))} │ {scores['cha']}{' '*(3-len(str(scores['cha'])))} │"
        str1 = f"│ {name} │ {race} │ STR │ DEX │ CON │ INT │ WIS │ CHA │"
        block = f"├{'─'*(len(name)+2)}┴{'─'*(len(race)+2)}┼{'─────┼'*5}─────┤"
        top = f"┌{'─'*(len(name)+2)}┬{'─'*(len(race)+2)}┬{'─────┬'*5}─────┐"
        bottom = f"└{'─'*(len(ref)-2)}┴{'─────┴'*5}─────┘"
    else:
        ref = f"│ level {level} {clas} │"
        str1 = f"│ {name}{' '*(len(str2)-len(str1))} │ {race} │ STR │ DEX │ CON │ INT │ WIS │ CHA │"
        str2 = f"│ level {level} {clas} │ {scores['str']}{' '*(3-len(str(scores['str'])))} │ {scores['dex']}{' '*(3-len(str(scores['dex'])))} │ {scores['con']}{' '*(3-len(str(scores['con'])))} │ {scores['int']}{' '*(3-len(str(scores['int'])))} │ {scores['wis']}{' '*(3-len(str(scores['wis'])))} │ {scores['cha']}{' '*(3-len(str(scores['cha'])))} │"
        block = f"├{'─'*4}{'─'*(len(str(level))+2)}┴{'─'*(len(clas)+2)}┼{'─────┼'*5}─────┤"
        top = f"┌{'─'*4}{'─'*(len(str(level))+2)}┬{'─'*(len(clas)+2)}┬{'─────┬'*5}─────┐"
        bottom = f"└{'─'*(len(ref)-2)}┴{'─────┴'*5}─────┘"
    print(top)
    print(str1)
    print(block)
    print(str2)
    print(bottom)

    Indexes = f"│ HP Cur/Tot │ AC │"
    hp = f"{char.data['Current_Health']}/{char.data['Health']}"
    Data = f"│ {hp}{' '*((len(' HP Cur/Tot ')-len(hp))-2)} │ {char.data['Armor_Class']}{' '*(2-len(str(char.data['Armor_Class'])))} │ " 
    top = f"┌{'─'*(len(Data)-3)}┐"
    middle = f"├{'─'*(len(Data)-3)}┤"
    bottom = f"└{'─'*(len(Data)-3)}┘"

    print(top)
    print(Indexes)
    print(middle)
    print(Data)
    print(bottom)

    inv_width = 40
    inv_str = "│ Inventory │"
    top = f"┌{'─'*(len(inv_str)-2)}┐"
    bottom = f"├{'─'*(len(inv_str)-2)}┴{'─'*((inv_width - len(inv_str))-1)}┐"
    print(top)
    print(inv_str)
    print(bottom)
    for item in char.data['Inventory']:
        string = f"│{char.data['Inventory'][item]['name']}│"
        string = f"│{char.data['Inventory'][item]['name']}{' '*(inv_width - len(string))}│"
        print(string)
    bottom = f"└{'─'*(inv_width - 2)}┘"
    print(bottom)

    
    

def main():
    print("""    
DnD Character Creator Copyright (C) 2024  Jacob Feldman
This program comes with ABSOLUTELY NO WARRANTY; for details type `warranty'.
This is free software, and you are welcome to redistribute it
under certain conditions; type `conditions' for details.
    """)
    char = Character_Class.Character()
    running = True
    while running == True:
        cmd = input("What would you like to do: ")
        match cmd:
            case 'conditions':
                print("\nSee LICENSE doccument in repository for full list of conditions at \'https://github.com/RoTeq/DnD-software/blob/main/LICENSE\'\n")
            case 'warranty':
                print(warranty)
            case 'help':
                print(help)
            case 'character':
                show_char_data(char)
            case 'full':
                show_full_char(char)
            case 'create':
                if char.data['Total_Level'] >= 1:
                    pass
                else:
                    char.create()
            case 'make':
                char.make()
            case 'build':
                char.build()
            case 'save':
                char.dump()
            case 'load':
                folder = 'Characters'
                c = input("what character: ")
                char.parse(f'{folder}\\{c}.json')
                #show_char_data(char)
            case 'exit':
                running = False

                
                


main()