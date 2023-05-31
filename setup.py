import cx_Freeze
import sys

base = None

if sys.platform == "win32":
	base = "Win32GUI"

executables = [cx_Freeze.Executable("main.py", base=base, icon="iconc.png")]

cx_Freeze.setup(
	name = "Banana Tennis",
	options = {"build_exe": {"packages":["pygame","math"], "include_files":["iconc.png"]}},
	version = "1.0.0",
	description = "Tennis Game Developed By Afari Samuel Adusei (CEO OF BANANA TECHNOLOGIES)",
	executables = executables

	)
