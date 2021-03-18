## AnsiColorsLib
### This is a library that is designed to allow developers to easily print colorized text.


## Installation
To install simply use pip:
```sh
pip install AnsiColorsLib
```

## Usage
```python
from ansicolorslib import COLOR_MANAGER

# Print entire text with a modification.
COLOR_MANAGER.ansiprint("Hello, World!", COLOR_MANAGER.RED + COLOR_MANAGER.BOLD, begins_with="\t\t", ends_with="\n\n")


# Modify a specific part of a string.
START_INDEX = 3
STOP_INDEX = 9
MOD = COLOR_MANAGER.GREEN + COLOR_MANAGER.BOLD
param1 = (START_INDEX, STOP_INDEX, MOD)

modded = COLOR_MANAGER.modify_string("Hello, World!", [param1])
print(modded)


# Get ansi string of rgb value.
R = 123
G = 221
B = 111

my_ansi = COLOR_MANAGER.ansirgb(R, G, B)
COLOR_MANAGER.ansiprint("Hello, World!", my_ansi)
```