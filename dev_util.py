import JSON_util as j
from pathlib import Path

root = Path("data")
file = Path("database.json")
path = root / file

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
    friendliness = input("Attitude: ")

    data = j.read_json(path)
    if planet not in data:
        data[planet] = {}
        data[planet][race] = {"attitude": friendliness}
    elif race in data[planet]:
        print("Race already recorded on this planet")
    else:
        data[planet][race] = {"attitude": friendliness}
        print(f"{race} from {planet} added to database")


entries = int(input("New entries: "))
for i in range(entries):
#     add_planet_to_database()
#     rename_planet()
    edit_planet_info()
#     del_planet_info()
#     del_planet_from_database()
#     add_species_to_database()
