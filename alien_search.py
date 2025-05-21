from Data.aliens import alien_database

# View all seen aliens
def view_all():
    print("Seen alien races:")
    for alien in alien_database.values():
        if alien.seen:
            print(alien)

# Search by Planet
def planet_search():
    planets = []
    for race in alien_database.values():
        add_planet = race.planet
        if add_planet not in planets:
            planets.append(add_planet)
    for planet in planets:
        print(f" - {planet}")

    planet = input("Enter Planet: ")
    if planet not in planets:
        print("Planet not found")
    else:
        print(f"Alien Races on Planet {planet}:")
        for race in alien_database:
            if alien_database[race].planet == planet:
                attitude = alien_database[race].friendliness
                print(f" - {race} ({attitude})")

def attitude_search():
    attitudes = []
    for race in alien_database.values():
        add_attitude = race.friendliness
        if add_attitude not in attitudes:
            attitudes.append(add_attitude)
    for attitude in attitudes:
        print(f"{attitude}, ",end="")

    attitude = input("\nEnter Attitude: ")
    print(f"{attitude} Alien Races:")
    for race in alien_database:
        if alien_database[race].friendliness == attitude:
            planet = alien_database[race].planet
            print(f" - {race} ({planet})")
