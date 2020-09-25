import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\acer\AppData\Local\Programs\Python\Python38\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\acer\AppData\Local\Programs\Python\Python38\tcl\tk8.6"

executables = [cx_Freeze.Executable("snake game.py", base=base)]


cx_Freeze.setup(
    name = "Funny Snake game",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["snake-image.ico",'tcl86t.dll','tk86t.dll', 'src']}},
    # Copy the 'tcl86t.dll' and 'tk86t.dll' from python folder
    # Include the name of your own files in "include_files":[]
    version = "1.0",
    description = "Pygame Play and enjoy",
    executables = executables
    )
