# Display info in a window instead of console
import tkinter as tk
from pathlib import Path
from assets.alien_search import general_info, view_all_planets, view_all_races, view_all_attitudes
parent = Path("")
root = Path("data")
file = Path("database.json")
ui_path = root / file

# <--- Info Display Functions --->
def display_planets():
    data, planets = view_all_planets()
    output = ""
    for planet in planets:
        output += f"\n    - {planet}"
    return output

def display_species():
    data, species = view_all_races()
    output = ""
    for race in species:
        output += f"\n    - {race}"
    return output

def display_attitudes():
    data, attitudes = view_all_attitudes()
    output = ""
    for att in attitudes:
        output += f"\n    - {att}"
    return output

# <--- Button Handling --->
def handle_view_info():
    info.delete("1.0", tk.END)
    info_text = general_info(ui_path)
    info.insert(tk.END, info_text)

def handle_view_planets():
    info.delete("1.0", tk.END)
    info_text = display_planets()
    info.insert(tk.END, info_text)

def handle_view_species():
    info.delete("1.0", tk.END)
    info_text = display_species()
    info.insert(tk.END, info_text)

def handle_view_attitudes():
    info.delete("1.0", tk.END)
    info_text = display_attitudes()
    info.insert(tk.END, info_text)

# <--- Main Window --->
main = tk.Tk()
main.title("Information")
main.configure(bg="pale green")
main.geometry("800x900")
main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=1)
main.columnconfigure(2, weight=1)
main.columnconfigure(3, weight=1)

# <--- Title Label --->
title = tk.Label(main, text="Alien Database", font=("Uncial Antiqua", 40, "bold"),
                 fg="dark blue", bg="#c6b7fe")
title.grid(row=0, columnspan=4, pady=20, ipadx=200, ipady=50)

# <--- Buttons --->
# General Info
view_info = tk.Button(main, text="General Info", font=("Cambria", 14),
                      fg="dark blue", bg="#d5cdf3", command=handle_view_info)
view_info.grid(row=1, column=0, pady=(0, 10))
# Planets
view_planets = tk.Button(main, text="View Planets", font=("Cambria", 14),
                      fg="dark blue", bg="#d5cdf3", command=handle_view_planets)
view_planets.grid(row=1, column=1, pady=(0, 10))
# Species
view_species = tk.Button(main, text="View Species", font=("Cambria", 14),
                      fg="dark blue", bg="#d5cdf3", command=handle_view_species)
view_species.grid(row=1, column=2, pady=(0, 10))
# Attitudes
view_attitudes = tk.Button(main, text="View Attitudes", font=("Cambria", 14),
                      fg="dark blue", bg="#d5cdf3", command=handle_view_attitudes)
view_attitudes.grid(row=1, column=3, pady=(0, 10))

# <--- Text Box --->
info = tk.Text(main, height=25, width=75, font=("Arial", 16,), bg="#e6e1f9")
info.grid(row=2, columnspan=4, padx=50, pady=(5, 50), ipadx=10)


# <--- Mainloop --->
main.mainloop()
