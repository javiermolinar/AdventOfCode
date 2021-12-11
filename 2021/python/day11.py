from utils import get_data


def increment(i, j, data):
    if i >= 0 and i < len(data) and j >= 0 and j < len(data[0]) and data[i][j] != 0:
        data[i][j] += 1


def get_flashes(steps, data):
    flashes = 0
    for step in range(steps):
        for i in range(0, len(data[0])):
            for j in range(0, len(data)):
                data[i][j] += 1

        more_flashes = True
        while more_flashes:
            more_flashes = False
            for i in range(0, len(data)):
                for j in range(0, len(data[0])):
                    if data[i][j] == 0:
                        continue
                    if data[i][j] > 9:
                        data[i][j] = 0
                        more_flashes = True
                        flashes += 1
                        increment(i - 1, j, data)
                        increment(i - 1, j - 1, data)
                        increment(i - 1, j + 1, data)
                        increment(i + 1, j, data)
                        increment(i + 1, j - 1, data)
                        increment(i + 1, j + 1, data)
                        increment(i, j - 1, data)
                        increment(i, j + 1, data)
        if sum([flashes for sublist in data for flashes in sublist]) == 0:
            return (flashes, step + 1)
    return (flashes, step + 1)


energy_data = [[int(y) for y in x] for x in get_data(11, str)]


def day11_1():
    print(get_flashes(100, energy_data)[0])


def day11_2():
    print(get_flashes(300, energy_data)[1])
