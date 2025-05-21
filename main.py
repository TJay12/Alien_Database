from Data.seen_aliens import alien_database

# Mark them as seen during an encounter
alien_database["Zenthari"].mark_seen()
alien_database["Gralnox"].mark_seen()
alien_database["Skarn"].mark_seen()

# View all seen aliens
print("Seen alien races:")
for alien in alien_database.values():
    if alien.seen:
        print(alien)