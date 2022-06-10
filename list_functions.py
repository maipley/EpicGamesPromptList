# IMPORTS
import os
import sys
import webbrowser
from tkinter import filedialog
from configparser import ConfigParser
from win10toast import ToastNotifier

# VARAIABLES
config = ConfigParser()
def_epic_app = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"


# CONFIG FILE CREATION/OPENING
if os.path.exists(os.getcwd() + "\\config.ini"):
    config.read("config.ini")
    with open("config.ini", "w") as f:
        config.write(f)
else:
    config.read('config.ini')
    config.add_section('main')
    config.set("main", "epic_path", def_epic_app)
    with open("config.ini", "w") as g:
        config.write(g)


# EPIC VARIABLES
epic_app = config.get("main", "epic_path")
epic_web = "https://store.epicgames.com/es-ES/"


# RESET PATH FUNCTION
def reset_path():
    config.set(
        "main",
        "epic_path",
        def_epic_app
    )
    with open("config.ini", "w") as o:
        config.write(o)


# NEW PATH FUNCTION
def newpath():
    global epic_app
    file_path = filedialog.askopenfilename()
    if file_path.endswith("EpicGamesLauncher.exe"):
        epic_app = file_path
        config.set(
            "main",
            "epic_path",
            file_path
        )
        with open("config.ini", "w") as u:
            config.write(u)
    elif len(file_path) <= 0:
        pass
    else:
        notifier()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


ico_path = resource_path("tostada.ico")


# NOTIFIER FUNCTION
def notifier():
    toast = ToastNotifier()
    toast.show_toast(
        "Incorrect Path",
        "You should select Epic Games Launcher executable",
        duration=10,
        icon_path=ico_path,
        threaded=True
    )


# EPIC LAUNCHER
def pc_app():
    os.startfile(epic_app)
    exit()


# EPIC WEB
def web_app():
    webbrowser.open(epic_web)
    exit()


# EPIC BOTH
def both():
    os.startfile(epic_app)
    webbrowser.open(epic_web)
    exit()


