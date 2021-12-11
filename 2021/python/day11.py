from utils import get_data

energy = [[int(y) for y in x] for x in get_data(11, str)]

flashes = 0


def increment(i, j, data):
    if i >= 0 and i < len(data) and j >= 0 and j < len(data[0]) and data[i][j] != 0:
        data[i][j] += 1


for step in range(500):

    for i in range(0, len(energy[0])):
        for j in range(0, len(energy)):
            energy[i][j] += 1

    more_flashes = True
    while more_flashes:
        more_flashes = False
        for i in range(0, len(energy)):
            for j in range(0, len(energy[0])):
                if energy[i][j] == 0:
                    continue
                if energy[i][j] > 9:
                    energy[i][j] = 0
                    more_flashes = True
                    flashes += 1
                    if i - 1 >= 0:
                        if energy[i - 1][j] != 0:
                            energy[i - 1][j] += 1
                        if j - 1 >= 0 and energy[i - 1][j - 1] != 0:
                            energy[i - 1][j - 1] += 1
                        if j + 1 < len(energy) >= 0 and energy[i - 1][j + 1] != 0:
                            energy[i - 1][j + 1] += 1
                    if i + 1 < len(energy[0]):
                        if energy[i + 1][j] != 0:
                            energy[i + 1][j] += 1
                        if j - 1 >= 0 and energy[i + 1][j - 1] != 0:
                            energy[i + 1][j - 1] += 1
                        if j + 1 < len(energy) >= 0 and energy[i + 1][j + 1] != 0:
                            energy[i + 1][j + 1] += 1
                    if j - 1 >= 0 and energy[i][j - 1] != 0:
                        energy[i][j - 1] += 1
                    if j + 1 < len(energy) and energy[i][j + 1] != 0:
                        energy[i][j + 1] += 1
    if sum([flashes for sublist in energy for flashes in sublist]) == 0:
        print(step)
        break

print(flashes)
