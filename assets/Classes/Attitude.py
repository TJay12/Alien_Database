class Attitude:
    def __init__(self, attitude, behavior1, behavior2, behavior3):
        self.attitude = attitude
        self.behaviour1 = behavior1
        self.behaviour2 = behavior2
        self.behaviour3 = behavior3

    def describe(self):
        output = ""
        output += f"\n   {self.attitude.capitalize()}:\n"
        output += f"   Creatures that have a {self.attitude} attitude generally\n"
        if self.behaviour3 == "":
            output += f"   display {self.behaviour1} or {self.behaviour2} behaviours. \n"
        else:
            output += (f"   display {self.behaviour1}, {self.behaviour2} or {self.behaviour3} "
                       f"behaviours. \n")
        return output