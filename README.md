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

COLOR_MANAGER.ansiprint("Hello, World!", COLOR_MANAGER.RED + COLOR_MANAGER.BOLD, starts_with="\t\t", ends_with="\n\n")
```