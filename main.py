from Data.aliens import alien_database

# View all seen aliens
print("Seen alien races:")
for alien in alien_database.values():
    if alien.seen:
        print(alien)