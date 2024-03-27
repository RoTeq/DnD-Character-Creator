import json
from dnd5eutils import *

api = dnd5api.DnD5eAPI()


class Character:
    def __init__(self) -> None:
        self.initialized = True
        self.data_entered = False
        self.Name = "N/A"
        self.Scores = [0,0,0,0,0,0]
        self.Saving_Throws = [0,0,0,0,0,0]
        self.Proficencies = []
        self.Proficeny_Bonus = 0
        self.Walking_Speed = 0
        self.Health = 0
        self.Current_Health = 0
        self.Armor_Class = 0
        self.Total_Level = 0
        self.Size = ''

        self.Barbarian_Level = 0
        self.Bard_Level = 0
        self.Cleric_Level = 0
        self.Druid_Level = 0
        self.Fighter_Level = 0
        self.Monk_level = 0
        self.Paladin_Level = 0
        self.Ranger_Level = 0
        self.Rouge_Level = 0
        self.Sorcerer_Level = 0
        self.Warlock_Level = 0
        self.Wizard_Level = 0

    def parse(self,json):
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
    
    def Dump(self):
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
        self.Class = input("Which class are you? ")
        match self.Class:
            case 'Barbarian':
                self.Barbarian_Level = 1
            case 'Bard':
                self.Bard_Level = 1
            case 'Cleric':
                self.Cleric_Level = 1
            case 'Druid':
                self.Druid_Level = 1
            case 'Fighter':
                self.Fighter_Level = 1
            case 'Monk':
                self.Monk_level = 1
            case 'Paladin':
                self.Paladin_Level = 1
            case 'Ranger':
                self.Ranger_Level = 1
            case 'Rouge':
                self.Rouge_Level = 1
            case 'Sorcerer':
                self.Sorcerer_Level = 1
            case 'Warlock':
                self.Warlock_Level = 1
            case 'Wizard':
                self.Wizard_Level = 1
        print(f"You Are {self.Name} a {self.Race} {self.Class} at level 1")
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

    def Build(self):
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
            p = proficency['name']
            print(p)
        for language in data['languages']:
            print(language['name'])
        for trait in data['traits']:
            print(trait['name'])
        for subrace in data['subraces']:
            print(subrace['name'])


    def randomize_scores(self) -> list[int]:
        scores = []
        for x in range(6):
            y = dice.dice(number=4,sides=6,drop=('min',1))
            scores.append(y)
        return scores

    def grab_race_data(self):
        pass

