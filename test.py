import dnd5eutils

api = dnd5eutils.dnd5api.DnD5eAPI()

data = api.request_locale('human')

print(data['name'])
print(data['speed'])
for bonus in data['ability_bonuses']:
    print(f"{bonus['ability_score']['index']}: +{bonus['bonus']}")
print(data['size'])
for proficency in data['starting_proficiencies']:
    p = proficency['name']
    print(p)
for language in data['languages']:
    print(language['name'])
for trait in data['traits']:
    print(trait['name'])
for subrace in data['subraces']:
    print(subrace['name'])
