class Alien:
    def __init__(self, race, friendliness, planet, seen=False):
        self.race = race
        self.friendliness = friendliness
        self.planet = planet
        self.seen = seen

    def mark_seen(self):
        self.seen = True

    def __str__(self):
        status = "seen" if self.seen else "unseen"
        return f"{self.race} ({self.friendliness}) from {self.planet} - {status}"