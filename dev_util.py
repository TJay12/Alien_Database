import json
from xml.etree.ElementTree import indent

import JSON_util as j
from pathlib import Path

root = Path("data")
file = Path("database.json")
path = root / file

def add_to_database():
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

    j.save_json(path, data)

def refactor_dict():
    data = j.read_json(path)
    newdata = {}

    planets = []
    for race in data:
        planet = data[race]["planet"]
        if planet not in planets:
            planets.append(planet)

    for planet in planets:
        for race in data:
            if data[race]["planet"] == planet:
                if planet not in newdata:
                    newdata[planet] = {}
                    newdata[planet][race] = {"attitude": data[race]["attitude"]}
                else:
                    newdata[planet][race] = {"attitude": data[race]["attitude"]}

    j.save_json(path, newdata)

entries = int(input("New entries: "))
for i in range(entries):
    add_to_database()
