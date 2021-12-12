from utils import get_data
from collections import namedtuple
from collections import deque

Node = namedtuple("Node", ["cave", "childs"])


def get_next_caves(cave_name, visited, map):
    possible_caves = [x[1] for x in map if x[0] == cave_name]
    possible_caves = [*possible_caves, *[x[0] for x in map if x[1] == cave_name]]
    valid_caves = [x for x in possible_caves if x not in [y for y in visited if y.islower()]]

    return valid_caves


def build_paths(node, map, visited):
    if node.cave == "end":
        visited.popleft()
        return 1
    paths = 0
    for cave_name in get_next_caves(node.cave, visited, map):
        cave = Node(cave_name, [])
        node.childs.append(cave)
        visited.appendleft(cave_name)
        paths += build_paths(cave, map, visited)
    visited.popleft()
    return paths


def day12_1():
    data = [(x.split("-")) for x in get_data(12)]
    print(data)
    root = Node("start", [])
    visited = deque(["start"])
    paths = build_paths(root, data, visited)
    print(paths)


def day12_2():
    data = [(x.split("-")) for x in get_data(12)]
    print(data)
    root = Node("start", [])
    visited = deque(["start"])
    paths = build_paths(root, data, visited)
    print(paths)


day12_1()
