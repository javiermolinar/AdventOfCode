from utils import get_data
from collections import deque


def get_next_caves(cave_name, visited, map, allow_small_caves):
    possible_caves = [x[1] for x in map if x[0] == cave_name]
    possible_caves = [*possible_caves, *[x[0] for x in map if x[1] == cave_name]]
    counts = [visited.count(x) for x in visited if x.islower()]
    return (
        [x for x in possible_caves if x not in [y for y in visited if y.islower()]]
        if not allow_small_caves or 2 in counts
        else [x for x in possible_caves if x != "start"]
    )


def build_paths(cave_name, map, visited, allow_small_caves=False):
    paths = 1
    if cave_name != "end":
        paths = sum(
            [
                build_paths(cave, map, deque([*visited, cave]), allow_small_caves)
                for cave in get_next_caves(cave_name, visited, map, allow_small_caves)
            ]
        )
    visited.popleft()
    return paths


def day12_1():
    print(build_paths("start", [(x.split("-")) for x in get_data(12)], deque(["start"])))


def day12_2():
    print(build_paths("start", [(x.split("-")) for x in get_data(12)], deque(["start"]), True))
