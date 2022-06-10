# IMPORTS
from list_functions import newpath, reset_path, pc_app, web_app, both, resource_path
from tkinter import Tk, Menu, Button

# WINDOW
window = Tk()
window.overrideredirect()
window.geometry("180x120+870+480")
window.title("Epic Games")
window.iconbitmap("C:\\Users\\maipley\\Desktop\\prompt list\\Epic games logo.ico")
window['bg'] = "black"

# MENU BAR
menubar = Menu(window)

window.config(menu=menubar)
path_menu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Path", menu=path_menu)
path_menu.add_command(label="Select path", command=newpath)
path_menu.add_command(label="Reset path", command=reset_path)

# BUTTONS
button1 = Button(window, text="PC app", padx=10, pady=5, bg="grey", command=pc_app)
button2 = Button(window, text="Web app", padx=10, pady=5, bg="grey", command=web_app)
button3 = Button(window, text="Both", padx=10, pady=5, bg="grey", command=both)

button1.pack()
button2.pack()
button3.pack()

# MAINLOOP
window.mainloop()
