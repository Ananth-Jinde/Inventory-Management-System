import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

# Resolve Tcl/Tk from the active Python installation instead of a hardcoded path.
python_dir = os.path.dirname(sys.executable)
tcl_library = os.path.join(python_dir, "tcl", "tcl8.6")
tk_library = os.path.join(python_dir, "tcl", "tk8.6")
if os.path.isdir(tcl_library):
    os.environ['TCL_LIBRARY'] = tcl_library
if os.path.isdir(tk_library):
    os.environ['TK_LIBRARY'] = tk_library

executables = [cx_Freeze.Executable("login.py", base=base, icon="assets/icons/IMS_ICON.ico")]


cx_Freeze.setup(
    name = "IMS",
    options = {
        "build_exe": {
            "packages": ["tkinter", "os"],
            "include_files": [
                "assets/icons/IMS_ICON.ico",
                "assets/images",
                "data/ims.db",
                "data/bills",
                "tools/build/tcl86t.dll",
                "tools/build/tk86t.dll",
            ],
        }
    },
    version = "1.0",
    description = "Inventory Management System | Developed By Jinde Anantha Sai",
    executables = executables
    )
