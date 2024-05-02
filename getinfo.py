import core
from sys import argv

val = argv[1]
g = eval(f'core.{val}')
print(f"{g}")
