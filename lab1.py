import json

with open('pokemon_full.json') as file:
    text_data = str(file.read())
    file.seek(0)
    pokemon_data = json.load(file)

# 1
print(len(text_data))

# 2
amount = 0
for symbols in text_data:
    if symbols.isalnum():
        amount += 1
print(amount)

# 3
max_symbols_description = 0
pokemon_name = 0
for object_name in pokemon_data:
    if len(object_name['description']) > max_symbols_description:
        pokemon_name = object_name['name']
        max_symbols_description = len(object_name['description'])
print(pokemon_name)

# 4
max_symbols_ability = 0
for object_ability_name in pokemon_data:
    for ability_name in object_ability_name['abilities']:
        if len(ability_name.split()) > max_symbols_ability:
            max_symbols_ability = len(ability_name.split())
            ability = []
        if len(ability_name.split()) == max_symbols_ability:
            ability.append(ability_name)
print(ability)


