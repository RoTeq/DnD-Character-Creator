import dnd5eutils
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
        str2 = f"│ level {level} {clas}{' '*(len(str1)-len(str2))} │"
        block = f"├{'─'*(len(name)+2)}┴{'─'*(len(race)+2)}┤"
        top = f"┌{'─'*(len(name)+2)}┬{'─'*(len(race)+2)}┐"
        bottom = f"└{'─'*(len(str1)-2)}┘"
    else:
        str1 = f"│ {name} │ {race}{' '*(len(str2)-len(str1))} │"
        block = f"├{'─'*(len(level)+2)}┴{'─'*(len(clas)+2)}┤"
        top = f"┌{'─'*(len(name)+2)}┬{'─'*(len(race)+2)}┐"
        bottom = f"└{'─'*(len(str2)-2)}┘"
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
        str1 = f"│ {name} │ {race}{' '*(len(str2)-len(str1))} │"
        block = f"├{'─'*(len(str(level))+2)}┴{'─'*(len(clas)+2)}┤"
        top = f"┌{'─'*(len(name)+2)}┬{'─'*(len(race)+2)}┐"
        bottom = f"└{'─'*(len(str2)-2)}┘"
    print(top)
    print(str1)
    print(block)
    print(str2)
    print(bottom)
#
    #Indexes = f"│ HP Cur/Tot │ AC │"
    #Data = f"│ {char.data['Current_Health']}/{char.data['Health']}{' '*(2-len())} │ {char.data['Armor_Class']}{2-len(str(char.data['Armor_Class']))} │ " 
    #top = f"┌{'─'*(len(Data)-3)}┐"
    #middle = f"├{'─'*(len(Data)-3)}┤"
    #bottom = f"└{'─'*(len(Data)-3)}┘"
#
    #print(top)
    #print(Indexes)
    #print(middle)
    #print(Data)
    #print(bottom)

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
    char = Character_Class.Character()
    running = True
    while running == True:
        cmd = input("What would you like to do: ")
        match cmd:
            case 'help':
                print(help)
            case 'character':
                show_char_data(char)
            case 'full':
                show_full_char(char)
            case 'create':
                char.create()
            case 'make':
                char.make()
            case 'build':
                char.build()
            case 'save':
                char.dump()
            case 'load':
                c = input("what character: ")
                char.parse(f'{c}.json')
                show_char_data(char)
            case 'exit':
                running = False

                
                


main()