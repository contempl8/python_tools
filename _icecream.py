# https://github.com/gruns/icecream
from icecream import ic
ic.configureOutput(includeContext=True)

for i in range(10):
    ic(i)

ic(f'This will print out from line 8')