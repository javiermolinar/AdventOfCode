from utils import get_data


def day6(days):
    "Given a list of fishes calculate the number of fishes after N days"
    fishes = [int(x) for x in get_data(6, str)[0].split(",")]
    for _ in range(days):
        new_fishes = [8 for _ in range(len([0 for x in fishes if x == 0]))]
        fishes = [x - 1 if x > 6 else (x - 1) % 7 for x in fishes]
        fishes.extend(new_fishes)
        print(fishes)
    return len(fishes)


def day6_2(days):
    "Given a list of fishes calculate the number of fishes after N days"
    days += 1
    initial_fishes = [int(x) for x in get_data(6, str)[0].split(",")]
    fishes_per_day = [0] * days
    fishes_per_day[0] = len(initial_fishes)
    for fish in initial_fishes:
        fishes_per_day[abs(0 - fish) + 1] += 1
        next_day = abs(0 - fish) + 8
        while next_day < days:
            fishes_per_day[next_day] += 1
            next_day += 7

    for day in range(1, days):
        next_day = day + 9
        while next_day < days:
            fishes_per_day[next_day] += fishes_per_day[day]
            next_day += 7
    return sum(fishes_per_day)
