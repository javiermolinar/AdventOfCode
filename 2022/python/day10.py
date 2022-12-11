from utils import get_data
from collections import deque

input = get_data(10)
instructions = deque()
for instruction in input:
    if "noop" in instruction:
        instructions.appendleft(0)
    else:
        instructions.appendleft(0)
        instructions.appendleft(int(instruction.split(" ")[1]))


def print_pixel(cicle, register):
    print("#" if (cicle % 40) - 1 in [register - 1, register, register + 1] else ".", end="")
    if cicle % 40 == 0:
        print("")


x = 1
cicle = 1
signal_strenght = 0
while instructions:
    print_pixel(cicle, x)
    x += instructions.pop()
    cicle += 1
    if cicle in [20, 60, 100, 140, 180, 220]:
        signal_strenght += cicle * x

print(signal_strenght)
