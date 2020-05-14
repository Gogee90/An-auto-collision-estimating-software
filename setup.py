import sys
from cx_Freeze import setup, Executable


# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"include_files" : ["ocenka.db",
                                        "C:/python34/Lib/site-packages/PyQt5/plugins/sqldrivers",
                                        "C:/python34/Lib/site-packages/lxml",
                                        "default.docx",
                                        "C:/python34/Lib/site-packages/docx"]}


# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "guifoo",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("startwindow.py", base=base, icon='bugh.ico')])
