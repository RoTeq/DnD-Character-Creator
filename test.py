import dnd5eutils

api = dnd5eutils.dnd5api.DnD5eAPI()

data = api.request_locale('elf')

print(data['name'])
print(data['speed'])
for bonus in data['ability_bonuses']:
    score = bonus['ability_score']
    print(score['index'])
print(data['size'])
for proficency in data['starting_proficencies']:
    p = proficency['name']
print(data['starting_proficiencies'])
print(data['languages'])
print(data['traits'])
print(data['subraces'])
