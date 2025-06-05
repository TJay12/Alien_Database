from alien_search import *

def search_database():
    search_by = input("Search By; ((V)iew all, (P)lanet, (A)ttitude), (S)pecies: ").lower()
    if search_by == "p":
        planet_search()
    elif search_by == "a":
        attitude_search()
    elif search_by == "s":
        speci_search()
    else:
        print("Invalid Option")

search_database()