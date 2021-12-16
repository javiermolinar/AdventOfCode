from utils import get_data
import sys

data = [[int(x) for x in y] for y in get_data(15)]


def get_neighbors(i, j, data):
    neighbors = []
    if j + 1 < len(data[0]):
        neighbors.append((i, j + 1))
    if j - 1 >= 0:
        neighbors.append((i, j - 1))
    if i + 1 < len(data):
        neighbors.append((i + 1, j))
    if i - 1 >= 0:
        neighbors.append((i - 1, j))
    return neighbors


def get_min_path(data):
    nodes = set()
    dist = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            nodes.add((i, j))
            dist[i, j] = sys.maxsize

    dist[(0, 0)] = 0
    while len(nodes) > 0:
        current_min_node = None
        for node in nodes:
            if current_min_node is None:
                current_min_node = node
            elif dist[node] < dist[current_min_node]:
                current_min_node = node
        for neighbor in get_neighbors(*current_min_node, data):
            temp = dist[current_min_node] + data[neighbor[0]][neighbor[1]]
            if temp < dist[neighbor]:
                dist[neighbor] = temp
        nodes.remove(current_min_node)
    return dist[(len(data) - 1, len(data[0]) - 1)]


def day15():
    print(get_min_path(data))
