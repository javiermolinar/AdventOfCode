from utils import get_data


def day6(days):
    "Given a list of fishes calculate the number of fishes after N days"
    fishes = [int(x) for x in get_data(6, str)[0].split(",")]
    for _ in range(days):
        new_fishes = [8 for _ in range(len([0 for x in fishes if x == 0]))]
        fishes = [x - 1 if x > 6 else (x - 1) % 7 for x in fishes]
        fishes.extend(new_fishes)
    return len(fishes)


print(day6(256))
