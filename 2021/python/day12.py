from utils import get_data
from functools import partial
from collections import deque


def get_next_caves(map, allow_small_caves, cave_name, visited):
    possible_caves = [*[x[1] for x in map if x[0] == cave_name], *[x[0] for x in map if x[1] == cave_name]]
    return (
        [x for x in possible_caves if x not in [y for y in visited if y.islower()]]
        if not allow_small_caves or 2 in [visited.count(x) for x in visited if x.islower()]
        else [x for x in possible_caves if x != "start"]
    )


def build_paths(cave_name, visited, get_next_caves):
    paths = 1
    if cave_name != "end":
        paths = sum(
            [build_paths(cave, deque([*visited, cave]), get_next_caves) for cave in get_next_caves(cave_name, visited)]
        )
    visited.popleft()
    return paths


def day12_1():
    map = [(x.split("-")) for x in get_data(12)]
    print(build_paths("start", deque(["start"]), partial(get_next_caves, map, True)))


def day12_2():
    map = [(x.split("-")) for x in get_data(12)]
    print(build_paths("start", deque(["start"]), partial(get_next_caves, map, True)))
