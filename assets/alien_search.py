from assets import JSON_util as j
from pathlib import Path
from assets.Classes.Planet import Planet
from assets.Classes.Alien import AlienSpecies
from assets.Classes.Attitude import Attitude

root = Path("data")
database_file = Path("database.json")
database_path = root / database_file
attribute_file = Path("speci_attributes.json")
attribute_path = root / attribute_file

# <--- Galaxy Info ---> (to be changed and class-ified later)
def general_info():
    data, species = view_all_species()
    data, planets = view_all_planets()
    galaxy = "Galitor"
    species_num = len(species)
    planets_num = len(planets)
    output = (f"    Welcome to {galaxy}! \n    This galaxy is home to {species_num} different "
              f"species across {planets_num} unique planets.")
    return output

# <--- View Info on Specific Categories --->
# Planet Info
def planet_info():
    data, planets = view_all_planets()
    output = ""
    for planet in planets:
        if planet in data:
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

# Species Info
def species_info():
    data, species_list = view_all_species()
    output = ""
    for speci in species_list:
        for planet in data:
            current_planet = planet
            if speci in data[planet]["species"]:
                speci = AlienSpecies(
                    speci= speci,
                    planet=current_planet,
                    attitude=data[planet]["species"][speci]["attitude"],
                    behaviour=data[planet]["species"][speci]["behaviour"],
                    texture=data[planet]["species"][speci]["texture"],
                    color=data[planet]["species"][speci]["color"],
                    size=data[planet]["species"][speci]["size"]
                )
                output += speci.describe()
    return output

# Attitude Info
def attitude_info():
    data, attitude_list = view_all_attitudes()
    attribute_data = j.read_json(attribute_path)
    output = ""
    for num in range(len(attitude_list)):
        attitude = attitude_list[num]
        behaviour = attribute_data['attitude_behaviors'][attitude]
        behav1 = behaviour[0]
        behav2 = behaviour[1]
        if len(behaviour) == 3:
            behav3 = behaviour[2]
        else:
            behav3 = ""
        attitude = Attitude(
            attitude=attitude,
            behavior1=behav1,
            behavior2=behav2,
            behavior3=behav3
        )
        output += attitude.describe()
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

# Search by Species
def speci_search():
    data, species = view_all_species()
    input_race = input("Enter Race: ")
    if input_race not in species:
        print(f"{input_race} not found")
    else:
        for planet, race in data.items():
            for race, info in data[planet].items():
                if input_race == race:
                    attitude = data[planet][race]["attitude"]
        print(f"{input_race} is from {planet} ({attitude})")

# <--- View all Items of a Specific Category --->
def view_all_planets():
    data = j.read_json(database_path)
    planets = []
    for planet in data:
        planets.append(planet)
    planets.sort()
    return data, planets

def view_all_species():
    data = j.read_json(database_path)
    species_list = []
    for planet, info in data.items():
        for speci, attitude in info["species"].items():
            if speci not in species_list:
                species_list.append(speci)
    species_list.sort()
    return data, species_list

def view_all_attitudes():
    data = j.read_json(database_path)
    attitudes_list = []
    for planet, info in data.items():
        for species, attributes in info["species"].items():
            attitude = attributes["attitude"]
            if attitude not in attitudes_list:
                attitudes_list.append(attitude)
    attitudes_list.sort()
    return data, attitudes_list

general_info()
# planet_info()
# species_info()
# attitude_info()
# view_all_planets()
# view_all_species()
# view_all_attitudes()
# planet_search()
# speci_search()
# attitude_search()