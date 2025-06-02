from assets import JSON_util as j
from pathlib import Path
from assets.Classes.Planet import Planet

root = Path("data")
file = Path("database.json")
path = root / file


def general_info(path):
    data = j.read_json(path)

    output = ""

    for planet in data:
        planet_data = data[planet]
        planet = Planet(
            name=planet,
            size=planet_data["size"],
            color= planet_data["color"],
            temperature=planet_data["temperature"],
            species=planet_data["species"],
            weather=planet_data["weather"]
        )
        output += planet.describe()
    return output

# <--- Search all Items in a Specific Category --->
# Search by Planet
def planet_search():
    data, planets = view_all_planets()
    planet = input("Enter Planet: ")
    if planet not in planets:
        print(f"{planet} not found")
        return
    else:
        planet_data = data[planet]
        planet = Planet(
            name=planet,
            size=planet_data["size"],
            color=planet_data["color"],
            temperature=planet_data["temperature"],
            species=planet_data["species"]
        )
        planet.describe()

# Search by Races
def race_search():
    data, races = view_all_races()

    input_race = input("Enter Race: ")
    if input_race not in races:
        print(f"{input_race} not found")
    else:
        for planet, race in data.items():
            for race, info in data[planet].items():
                if input_race == race:
                    attitude = data[planet][race]["attitude"]
        print(f"{input_race} is from {planet} ({attitude})")

# Search by Attitude
def attitude_search():
    data, attitudes = view_all_attitudes()

    atude_imput = input("\nEnter Attitude: ")
    print(f"{atude_imput} Alien Races:")
    for planet, race in data.items():
        for race, attitude in data[planet].items():
            attitude = data[planet][race]["attitude"]
            if attitude == atude_imput:
                print(f" - {race} ({planet})")

# <--- View all Items of a Specific Category --->
def view_all_planets():
    data = j.read_json(path)
    planets = []
    for planet in data:
        planets.append(planet)
    for planet in planets:
        print(f" - {planet}")
    return data, planets

def view_all_races():
    data = j.read_json(path)
    races = []
    for planet, info in data.items():
        for species, attitude in info["species"].items():
            if species not in races:
                races.append(species)
    for race in races:
        print(f" - {race}")
    return data, races

def view_all_attitudes():
    data = j.read_json(path)
    attitudes = []
    for planet, info in data.items():
        for species, attributes in info["species"].items():
            attitude = attributes["attitude"]
            if attitude not in attitudes:
                attitudes.append(attitude)
    for attitude in attitudes:
        print(f" - {attitude}")
    return data, attitudes

# general_info(path)
# view_all_planets()
# view_all_races()
# view_all_attitudes()
# planet_search()
# race_search()
# attitude_search()