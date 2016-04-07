import sys
from cx_Freeze import setup, Executable


"""exe = Executable(
    script="eartraining.py",
    base="Win32GUI",
    ) 

setup(
    name = "eartrainingApp",
    version = "0.1",
    description = "An ear training program",
    executables = [exe]
    )

another 
base Win32GUI is for windows
exe = Executable(script="medcker.py",base="Win32GUI")
#version is the program version
setup(version="3.0",options={"build_exe":{"includes":includes}},executables = [exe]) - See more at: http://themkbytes.blogspot.com.es/2012/08/python-cxfreeze-quick-easy-tutorial.html#sthash.SjMkHF9c.dpuf

"""

setup(
    name = "eartrainingApp",
    version = "0.1",
    description = "An ear training program",
    executables = [Executable("eartraining.py")]
    )


