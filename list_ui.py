# IMPORTS
from list_functions import newpath, reset_path, pc_app, web_app, both, resource_path
from tkinter import Tk, Menu, Button

# WINDOW
window = Tk()
window.overrideredirect()
window.geometry("180x150+870+480")
window.title("Epic Games")
wiconbitmap = resource_path("Epic games logo.ico")
window.iconbitmap(wiconbitmap)
window['bg'] = "black"

# MENU BAR
menubar = Menu(window)

window.config(menu=menubar)
path_menu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Path", menu=path_menu)
path_menu.add_command(label="Select path", command=newpath)
path_menu.add_command(label="Reset path", command=reset_path)

# BUTTONS
Button(
    window,
    text="PC app",
    padx=10, pady=5,
    bg="grey",
    cursor="hand2",
    command=pc_app
    ).pack(pady=2)

Button(
    window,
    text="Web app",
    padx=10, pady=5,
    bg="grey",
    cursor="hand2",
    command=web_app
    ).pack(pady=2)

Button(
    window,
    text="Both",
    padx=10,
    pady=5,
    bg="grey",
    cursor="hand2",
    command=both
    ).pack(pady=2)

# MAINLOOP
window.mainloop()
