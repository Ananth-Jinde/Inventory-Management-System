import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\HP\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\HP\AppData\Local\Programs\Python\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("login.py", base=base, icon="IMS_ICON.ico")]


cx_Freeze.setup(
    name = "IMS",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["IMS_ICON.ico",'tcl86t.dll','tk86t.dll','images','ims']}},
    version = "1.0",
    description = "Inventory Management System | Developed By Jinde Anantha Sai",
    executables = executables
    )
