from utils import get_data
from collections import deque


def get_initial_stacks(crates_stacks):
    stacks = [deque() for _ in range(int(crates_stacks[-1][-2]))]
    for i in range(len(crates_stacks) - 1):
        line = crates_stacks[len(crates_stacks) - 2 - i]
        crates = [line[i : i + 4] for i in range(0, len(line), 4)]
        for pos, crate in enumerate(crates):
            if crate[1] != " ":
                stacks[pos].appendleft(crate[1])
    return stacks


def get_movements(mov):
    return [[int(i) for i in m.split() if i.isdigit()] for m in mov]


data = get_data(5)
crates_stacks, movements = (get_initial_stacks(data[: data.index("")]), get_movements(data[data.index("") + 1 :]))


def day5_1():
    for move in movements:
        crates = [crates_stacks[move[1] - 1].popleft() for _ in range(move[0])]
        crates_stacks[move[2] - 1].extendleft(crates)
    return "".join([stack.popleft() for stack in [s for s in crates_stacks]])


def day5_2():
    for move in movements:
        crates = [crates_stacks[move[1] - 1].popleft() for _ in range(move[0])]
        crates.reverse()
        crates_stacks[move[2] - 1].extendleft(crates)
    return "".join([stack.popleft() for stack in [s for s in crates_stacks]])


print(day5_1())
