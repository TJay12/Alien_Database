class AlienSpecies:
    def __init__(self, speci, planet, attitude, behaviour, texture, color, size):
        self.speci = speci
        self.planet = planet
        self.attitude = attitude
        self.behaviour = behaviour
        self.texture = texture
        self.color = color
        self.size = size

    def describe(self):
        output = ""
        output += f"\n   {self.speci}:\n"
        output += f"   The {self.speci} are a {self.size}, {self.color} species with\n"
        output += f"   a {self.texture} outer.\n"
        output += f"   Naturally {self.attitude} the {self.speci} found on {self.planet}\n"
        output += f"   generally displays {self.behaviour} behaviours.\n"
        return output
