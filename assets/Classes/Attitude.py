class Attitude:
    def __init__(self, attitude, behavior):
        self.attitude = attitude
        self.behaviour = behavior

    def describe(self):
        output = ""
        output += f"\n   {self.attitude.capitalize()}:\n"
        output += f"   Creatures that have a {self.attitude} attitude generally\n"
        output += f"   display {self.behaviour} behaviours. \n"
        return output