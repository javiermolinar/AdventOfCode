from utils import get_data
from collections import namedtuple
from collections import deque

Node = namedtuple("Node", ["cave", "childs"])
data = [(x.split("-")) for x in get_data(12)]


def get_next_caves(cave_name, visited, map, allow_small_caves):
    possible_caves = [x[1] for x in map if x[0] == cave_name]
    possible_caves = [*possible_caves, *[x[0] for x in map if x[1] == cave_name]]
    counts = [visited.count(x) for x in visited if x.islower()]
    return (
        [x for x in possible_caves if x not in [y for y in visited if y.islower()]]
        if not allow_small_caves or 2 in counts
        else [x for x in possible_caves if x != "start"]
    )


def build_paths(node, map, visited, allow_small_caves=False):
    if node.cave == "end":
        visited.popleft()
        return 1
    paths = 0
    for cave_name in get_next_caves(node.cave, visited, map, allow_small_caves):
        cave = Node(cave_name, [])
        node.childs.append(cave)
        visited.appendleft(cave_name)
        paths += build_paths(cave, map, visited, allow_small_caves)
    visited.popleft()
    return paths


def day12_1():
    print(build_paths(Node("start", []), data, deque(["start"])))


def day12_2():
    print(build_paths(Node("start", []), data, deque(["start"]), True))
