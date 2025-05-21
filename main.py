from seen_aliens import seen_all
from alien_search import *

# For 'Search Database' dev purpose
seen_all()

def search_database():
    search_by = input("Search By; ((V)iew all, (P)lanet, (A)ttitude): ").lower()
    if search_by == "v":
        view_all()
    elif search_by == "p":
        planet_search()
    elif search_by == "a":
        attitude_search()
    else:
        print("Invalid Option")

search_database()