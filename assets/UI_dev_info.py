# Display info in a window instead of console
import tkinter as tk
from assets.alien_search import (general_info, planet_info, species_info, attitude_info,
                                 view_all_planets, view_all_species, view_all_attitudes)

# <--- Button Handling 'List All' Display Functions --->
def handle_display_all_planets():
    info.delete("1.0", tk.END)
    data, planets = view_all_planets()
    output = ""
    for planet in planets:
        output += f"\n    - {planet}"
    info_text = output
    info.insert(tk.END, info_text)

def handle_display_all_species():
    info.delete("1.0", tk.END)
    data, species = view_all_species()
    output = ""
    for race in species:
        output += f"\n    - {race}"
    info_text = output
    info.insert(tk.END, info_text)

def handle_display_all_attitudes():
    info.delete("1.0", tk.END)
    data, attitudes = view_all_attitudes()
    output = ""
    for att in attitudes:
        output += f"\n    - {att.capitalize()}"
    info_text = output
    info.insert(tk.END, info_text)

# <--- Button Handling 'View Info' Display Functions --->
def handle_view_general_info():
    info.delete("1.0", tk.END)
    info_text = general_info()
    info.insert(tk.END, info_text)

def handle_view_planets_info():
    info.delete("1.0", tk.END)
    info_text = planet_info()
    info.insert(tk.END, info_text)

def handle_view_species_info():
    info.delete("1.0", tk.END)
    info_text = species_info()
    info.insert(tk.END, info_text)

def handle_view_behaviours_info():
    info.delete("1.0", tk.END)
    info_text = attitude_info()
    info.insert(tk.END, info_text)

# <--- Main Window --->
main = tk.Tk()
main.title("Alien Database and Information")
main.configure(bg="pale green")
main.geometry("800x1000")
main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=1)
main.columnconfigure(2, weight=1)

# <--- Title Label --->
title = tk.Label(main, text="Alien Database", font=("Uncial Antiqua", 40, "bold"),
                 fg="dark blue", bg="#c6b7fe")
title.grid(row=0, columnspan=3, pady=20, ipadx=200, ipady=25)

# <--- Buttons --->
# General Info
view_info = tk.Button(main, text="General Info", font=("Cambria", 14),
                      fg="dark blue", bg="#d5cdf3", command=handle_view_general_info)
view_info.grid(row=1, column=1, pady=(0, 10))
# Planets
list_planets = tk.Button(main, text="List All Planets", font=("Cambria", 14),
                              fg="dark blue", bg="#d5cdf3", command=handle_display_all_planets)
list_planets.grid(row=2, column=0, pady=(0, 10))
view_planets_info = tk.Button(main, text="View Planets Info", font=("Cambria", 14),
                              fg="dark blue", bg="#d5cdf3", command=handle_view_planets_info)
view_planets_info.grid(row=3, column=0, pady=(0, 10))
# Species
list_species = tk.Button(main, text="List All Species", font=("Cambria", 14),
                              fg="dark blue", bg="#d5cdf3", command=handle_display_all_species)
list_species.grid(row=2, column=1, pady=(0, 10))
view_species_info = tk.Button(main, text="View Species Info", font=("Cambria", 14),
                              fg="dark blue", bg="#d5cdf3", command=handle_view_species_info)
view_species_info.grid(row=3, column=1, pady=(0, 10))
# Attitudes
list_behaviours = tk.Button(main, text="List All Behaviours", font=("Cambria", 14),
                                 fg="dark blue", bg="#d5cdf3", command=handle_display_all_attitudes)
list_behaviours.grid(row=2, column=2, pady=(0, 10))
view_behaviours_info = tk.Button(main, text="View Behaviours Info", font=("Cambria", 14),
                                 fg="dark blue", bg="#d5cdf3", command=handle_view_behaviours_info)
view_behaviours_info.grid(row=3, column=2, pady=(0, 10))

# <--- Text Box --->
info = tk.Text(main, height=25, width=75, font=("Arial", 16,), bg="#e6e1f9")
info.grid(row=4, columnspan=3, padx=50, pady=(5, 50), ipadx=10)


# <--- Mainloop --->
main.mainloop()
