import JSON_util as j
from pathlib import Path
import random

root = Path("data")
file = Path("database.json")
path = root / file

attitudes = ["positive", "negative", "neutral", "proactive", "reactive",
             "assertive", "aggressive", "empathic", "egocentric", "distrustful"]

attutude_behaviors = {
    "positive": {
        "optimistic",
        "constructive"
    },
    "negative": {
        "pessimistic",
        "complainer",
        "criticizing",
    },
    "neutral": {
        "indifferent",
        "unemotional"
    },
    "proactive": {
        "motivated",
        "responsible",
        "initiative"
    },
    "reactive": {
        "overwhelmed",
        "passive"
    },
    "assertive": {
        "communicative",
        "expressive"
        "respectful"
    },
    "aggressive": {
        "hostile",
        "imposing",
        "confrontational"
    },
    "empathic": {
        "sensitive",
        "understanding",
        "compassionate"
    },
    "egocentric": {
        "selfish",
        "self-centered"
    },
    "distrustful": {
        "skeptical",
        "suspicious",
        "distant"
    },
}

textures = ["smooth", "ridged", "soft", "rough", "hard"]
colors = ["black", "grey", "white", "brown", "red", "orange", "yellow", "green", "blue",
         "purple", "pink"]
sizes = ["massive", "tall", "average", "short", "tiny"]

def rand_behaviour():
    attitude = random.choice(attitudes)
    behaviour = random.choice(list(attutude_behaviors[attitude]))
    return attitude, behaviour

def rand_appearance():
    tex = random.choice(textures)
    color = random.choice(colors)
    size = random.choice(sizes)
    return tex, color, size

def add_planet_to_database():
    planet = input("Planet Name: ")
    size = input("Planet Size: ")
    temperature = input("Planet Temperature: ")

    data = j.read_json(path)
    if planet not in data:
        data[planet] = {}
    data[planet]["size"] = size
    data[planet]["temperature"] = temperature

    j.save_json(path, data)

def rename_planet():
    data = j.read_json(path)
    old_name = input("Current Planet Name: ")

    if old_name not in data:
        print(f"No planet named {old_name} found")
        return

    new_name = input("New Planet Name: ")
    if new_name in data:
        update = input(f"A planet named {new_name} already exists do you wish to update {new_name}").lower()
        if update == "y":
            edit_planet_info()
        else:
            return

    data[new_name] = data.pop(old_name)
    print(f"{old_name} has been renamed to {new_name}")
    j.save_json(path, data)

def edit_planet_info():
    data = j.read_json(path)
    planet_name = input("Planet Name: ")
    if planet_name not in data:
        print(f"No planet named {planet_name} found")
        return
    else:
        key = input("Key to Update: ")
        new_value = input("New Value: ")
        if key not in data[planet_name]:
            add_key = input(f"{key} property not found do you wish to add {key} (y/n): ")
            if add_key == "y":
                data[planet_name][key] = new_value
                print(f"{key} added to planet {planet_name}")
                print(f"{planet_name}s {key} is {new_value}")
            else:
                return
        j.save_json(path, data)

def del_planet_info():
    data = j.read_json(path)
    planet = input("Planet Name: ")

    if planet not in data:
        print(f"{planet} doesn't exist")
        return

    key = input("Which key to delete: ")
    if key not in data[planet]:
        print(f"{key} not found in {planet}")
    else:
        delete = input(f"Are you sure you want to delete '{key}' from {planet}? (y/n): ").lower()
        if delete == "y":
            del data[planet][key]
            print(f"{key} deleted from {planet}")
            j.save_json(path, data)

def del_planet_from_database():
    data = j.read_json(path)
    planet_name = input("Planet to Remove: ")

    if planet_name not in data:
        print(f"{planet_name} doesn't exist")
    else:
        delete = input(f"Are you sure you want to permanently delete {planet_name} (y/n): ").lower()
        if delete == "y":
            del data[planet_name]
            print(f"{planet_name} removed from database")
            j.save_json(path, data)

def add_species_to_database():
    planet = input("Planet: ")
    race = input("Race: ")
    attitude, behaviour = rand_behaviour()
    texture, color, size = rand_appearance()

    data = j.read_json(path)
    if planet not in data:
        data[planet] = {}
        data[planet][race] = {"attitude": attitude,
                              "behaviour": behaviour,
                              "texture": texture,
                              "color": color,
                              "size": size}
    elif race in data[planet]:
        print("Race already recorded on this planet")
    else:
        data[planet][race] = {"attitude": attitude,
                              "behaviour": behaviour,
                              "texture": texture,
                              "color": color,
                              "size": size
                              }
        print(f"{race} from {planet} added to database")

def add_attributes_species_info():
    data = j.read_json(path)
    for planet, info in data.items():
        species = data[planet]["species"]
        for speci, attrib in species.items():
            attitude = species[speci]["attitude"]
            species[speci]["behaviour"] = random.choice(list(attutude_behaviors[attitude]))
            texture, color, size = rand_appearance()
            species[speci]["texture"] = texture
            species[speci]["color"] = color
            species[speci]["size"] = size
    j.save_json(path, data)


# entries = int(input("New entries: "))
# for i in range(entries):
#     add_planet_to_database()
#     rename_planet()
#     edit_planet_info()
#     del_planet_info()
#     del_planet_from_database()
#     add_species_to_database()
# rand_behaviour()
# rand_appearance()
# add_attributes_species_info()
