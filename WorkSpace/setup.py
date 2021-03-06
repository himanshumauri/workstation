import cx_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Himanshu Kumar\AppData\Local\Programs\Python\Python37-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Himanshu Kumar\AppData\Local\Programs\Python\Python37-32\tcl\tk8.6"

executables = [cx_Freeze.Executable("workspace.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "WorkSpace",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll', 'image']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )
