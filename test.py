import dnd5eutils

api = dnd5eutils.dnd5api.DnD5eAPI()

data = api.request_locale('Rogue')

print(data['hit_die'])
print()
#print(data['proficiency_choices'])
proficiency_choices = data['proficiency_choices'][0]
print(proficiency_choices['desc'])
print()
for choice in proficiency_choices['from']['options']:
    print(choice['item']['name'])

print()
for proficiency in data['proficiencies']:
    print(proficiency)
print()
print(data['saving_throws'])
print()
print(data['starting_equipment'])
print()
print(data['starting_equipment_options'])
print()
print(data['class_levels'])