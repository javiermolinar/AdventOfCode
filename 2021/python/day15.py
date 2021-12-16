from utils import get_data
import sys
import heapq

data = [[int(x) for x in y] for y in get_data(15)]


def get_neighbors(i, j, data):
    if j + 1 < len(data[0]):
        yield (i, j + 1)
    if j - 1 >= 0:
        yield (i, j - 1)
    if i + 1 < len(data):
        yield (i + 1, j)
    if i - 1 >= 0:
        yield (i - 1, j)


def get_min_path(data):
    dist = {}
    visited = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            visited[i, j] = False
            dist[i, j] = sys.maxsize

    dist[(0, 0)] = 0
    priority = [(0, (0, 0))]
    while len(priority) > 0:
        _, current_min_node = heapq.heappop(priority)
        if visited[current_min_node]:
            continue
        visited[current_min_node] = True
        for neighbor in get_neighbors(*current_min_node, data):
            temp = dist[current_min_node] + data[neighbor[0]][neighbor[1]]
            if temp < dist[neighbor]:
                dist[neighbor] = temp
                heapq.heappush(priority, (dist[neighbor], neighbor))
    return dist[(len(data) - 1, len(data[0]) - 1)]


def day15_1():
    print(get_min_path(data))


def day15_2():
    big_data = []
    for i in range(len(data) * 5):
        big_data.append([0] * len(data[0]) * 5)
        for j in range(len(data[0]) * 5):
            sum = data[i % len(data)][j % len(data[0])] + int(j / len(data[0])) + int(i / len(data))
            big_data[i][j] = sum if sum <= 9 else sum % 9
    print(get_min_path(big_data))
