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
#     add_to_database()
# planet_dict_refactor()
# edit_planets()
#     add_planet_to_database()