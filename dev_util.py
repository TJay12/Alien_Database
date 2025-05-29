import JSON_util as j
from pathlib import Path

root = Path("data")
file = Path("database.json")
path = root / file

def add_to_database():
    race = input("Race: ")
    friendliness = input("Attitude: ")
    planet = input("Planet: ")

    data = j.read_json(path)

    data[race] = {"race": race, "attitude": friendliness, "planet": planet}

    j.save_json(path, data)
    print(f"{race} from {planet} added to database")

entries = int(input("New entries: "))
for i in range(entries):
    add_to_database()

