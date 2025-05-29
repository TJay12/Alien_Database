from alien_search import *

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