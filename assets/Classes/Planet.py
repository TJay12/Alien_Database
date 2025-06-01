class Planet:
    def __init__(self, name, size, color, temperature, weather, species):
        self.name = name
        self.size = size
        self.color = color
        self.temperature = temperature
        self.weather = weather
        self.species = species

    def describe(self):
        print(f"{self.name}:")
        print(f"Seen from space {self.name} is a {self.size}, {self.color} planet, "
              f"up close it can bee seen as a {self.temperature} planet that's "
              f"generally {self.weather}.\n"
              f"Home to the:")
        for race, info in self.species.items():
            print(f" - {race} ({info['attitude']})")