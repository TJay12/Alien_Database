from Data.aliens import alien_database
from seen_aliens import seen_all

seen_all()

# View all seen aliens
print("Seen alien races:")
for alien in alien_database.values():
    if alien.seen:
        print(alien)