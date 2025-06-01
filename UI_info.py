# Display info in a window instead of console
import tkinter as tk
from pathlib import Path
from assets.alien_search import general_info
parent = Path("")
root = Path("assets/data")
file = Path("database.json")
ui_path = parent / root / file
print(ui_path)

general_info(ui_path)
# <--- Window --->
main = tk.Tk()
main.title("Information")

# <--- Buttons --->
view_general_info = tk.Button(main, text="General Info")
view_general_info.pack(padx=50, pady=50)





# <--- Mainloop --->
main.mainloop()
