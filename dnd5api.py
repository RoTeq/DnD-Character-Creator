import requests

class DnD5eAPI():
    def __init__(self) -> None:
        self.site = "https://www.dnd5eapi.co/api/"
        self.headers = {'Accept': 'application/json'}
        self.urlcall = "https://www.dnd5eapi.co"

        self.locales = {
            'ability scores' : 'ability-scores',
            'alignments' : 'alignments',
            'backgrounds' : 'backgrounds',
            'classes' : 'classes',
            'conditions' : 'conditions',
            'damage types' : 'damage-types',
            'equipment' : 'equipment',
            'equipment categories' : 'equipment-categories',
            'feats' : 'feats',
            'features' : 'features',
            'languages' : 'languages',
            'magic items' : 'magic-items',
            'magic schools' : 'magic-schools',
            'monsters' : 'monsters',
            'proficiencies' : 'proficiencies',
            'races' : 'races',
            'rule sections' : 'rule-sections',
            'rules' : 'rules',
            'skills' : 'skills',
            'spells' : 'spells',
            'subclasses' : 'subclasses',
            'subraces' : 'subraces',
            'traits' : 'traits',
            'weapon properties' : 'weapon-properties'
        }
        self.classes = {
            'barbarian' : 'barbarian',
            'bard' : 'bard',
            'cleric' : ' cleric',
            'druid' : 'druid',
            'fighter' : 'fighter',
            'monk' : 'monk',
            'paladin' : 'paladin',
            'ranger' : 'ranger',
            'rogue' : 'rogue',
            'sorcerer' : 'sorcerer',
            'warlock' : 'warlock',
            'wizard' : 'wizard'
        }
        self.races = {
            'dragonborn' : 'dragonborn',
            'dwarf' : 'dwarf',
            'elf' : 'elf',
            'gnome' : 'gnome',
            'half elf' : 'half-elf',
            'half orc' : 'half-orc',
            'halfling' : 'halfling',
            'human' : 'human',
            'tiefling' : 'tiefling'
        }
    
    def url_call(self,url:str):
        link = self.urlcall+url
        response = requests.get(link,headers=self.headers)
        return response.json()

    def request(self,location:str = ''):
        url = self.site+location
        response = requests.get(url,headers=self.headers)
        return response.json()

    def request_locale(self, Defined_locale:str = 0):
        Defined_locale = Defined_locale.lower()
        if Defined_locale == 0:
            return self.request()
        if Defined_locale in self.classes:
            return self.request(f"classes/{self.classes[Defined_locale]}")
        if Defined_locale in self.races:
            return self.request(f"races/{self.races[Defined_locale]}")
        else:
            return self.request(self.locales[Defined_locale])