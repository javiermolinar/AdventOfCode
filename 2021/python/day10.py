from utils import get_data
from collections import deque

delimiters = {")": "(", "]": "[", "}": "{", "}": "{", ">": "<"}
navigation = get_data(10, str)

def get_value(delimiter):
    match delimiter:
        case ")":
            return (3, 1)
        case "]":
            return (57, 2)
        case "}":
            return (1197, 3)
        case ">":
            return (25137, 4)
        case _:
            return (0, 0)

def get_delimiters(input):
    queue = deque()
    for d in input:
        if d in (delimiters.keys()):
            delimiter = queue.popleft()
            if delimiters[d] != delimiter:
                return d
        else:
            queue.appendleft(d)

    return ("", [list(delimiters.keys())[list(delimiters.values()).index(x)] for x in list(queue)])

def get_missing_delimiters_value(input):
    value = 0
    for delimiter in input:
        value *= 5
        value += get_value(delimiter)[1]
    return value

def day10_1():
    print(sum([get_value(x)[0] for x in [get_delimiters(line)[0] for line in navigation]]))

def day10_2():
    missing_delimiters = [get_delimiters(line)[1] for line in navigation if get_delimiters(line)[0] == ""]
    missing_values = [get_missing_delimiters_value(x) for x in missing_delimiters]
    missing_values.sort()
    print(missing_values[int(len(missing_values)/2)])
