import JSON_util as j
from pathlib import Path
from Classes.Planet import Planet

root = Path("data")
file = Path("database.json")
path = root / file

def keys_dict_refactor():
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


def planet_dict_refactor():
    data = j.read_json(path)
    newdata = {}

    for planet, race in data.items():
        for race, info in race.items():
            if planet not in newdata:
                newdata[planet] = {}
            if "species" not in newdata[planet]:
                newdata[planet] = {"species": {race: info}}
            else:
                newdata[planet]["species"][race] = info

    j.save_json(path, newdata)


def manual_read_planet():
    data = j.read_json(path)

    Xenith_Prime_data = data["Xenith Prime"]
    planet = Planet(
        name="Xenith Prime",
        size=Xenith_Prime_data["size"],
        temperature=Xenith_Prime_data["temperature"],
        species=Xenith_Prime_data["species"]
    )

    print(f"{planet.name}:")
    print(f"{planet.name} is a {planet.size}, {planet.temperature} planet.\n"
          f"Home to the:")
    for race, info in planet.species.items():
        print(f" - {race} ({info["attitude"]})")

def auto_read_planet(planet_name):
    data = j.read_json(path)

    if planet_name not in data:
        print("Planet not found")
        return

    planet_data = data[planet_name]
    planet = Planet(
        name=planet_name,
        size=planet_data["size"],
        temperature=planet_data["temperature"],
        species=planet_data["species"]
    )

    print(f"{planet.name}:")
    print(f"{planet.name} is a {planet.size}, {planet.temperature} planet.\n"
          f"Home to the:")
    for race, info in planet.species.items():
        print(f" - {race} ({info['attitude']})")

# manual_read_planet()
auto_read_planet("Xenth")
