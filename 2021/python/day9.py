from utils import get_data
import math


def is_low_point(x, y, data):
    value = data[x][y]
    if y - 1 >= 0 and data[x][y - 1] <= value:
        return False
    if y + 1 < len(data[0]) and data[x][y + 1] <= value:
        return False
    if x - 1 >= 0 and data[x - 1][y] <= value:
        return False
    if x + 1 < len(data) and data[x + 1][y] <= value:
        return False
    return True


def get_basin_size(x, y, data, numbers):
    if data[x][y] == 9:
        return numbers
    if (x, y) in numbers:
        return numbers
    numbers.add((x, y))
    if y - 1 >= 0:
        numbers.union(get_basin_size(x, y - 1, data, numbers))
    if y + 1 < len(data[0]):
        numbers.union(get_basin_size(x, y + 1, data, numbers))
    if x - 1 >= 0:
        numbers.union(get_basin_size(x - 1, y, data, numbers))
    if x + 1 < len(data):
        numbers.union(get_basin_size(x + 1, y, data, numbers))
    return numbers


def day9_1():
    map = [[int(y) for y in x] for x in get_data(9, str)]
    lowest_points = [[map[i][j] for j in range(len(map[0])) if is_low_point(i, j, map)] for i in range(len(map))]
    return print(sum([item + 1 for sublist in lowest_points for item in sublist]))


def day9_2():
    map = [[int(y) for y in x] for x in get_data(9, str)]
    basin_sizes = [
        [get_basin_size(i, j, map, set()) for j in range(len(map[0])) if is_low_point(i, j, map)]
        for i in range(len(map))
    ]
    basin_sum = [len(basins) for sublist in basin_sizes for basins in sublist]
    basin_sum.sort(reverse=True)

    return math.prod(basin_sum[:3])
