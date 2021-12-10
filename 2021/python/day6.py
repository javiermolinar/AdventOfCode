from utils import get_data
from collections import deque


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
    initial_fishes = [int(x) for x in get_data(6, str)[0].split(",")]
    fishes = 0
    for fish in initial_fishes:
        fishes += 1
        parent_fish = abs(0 - fish) + 1
        queue = deque([parent_fish])
        while len(queue) != 0:
            while parent_fish < days and parent_fish + 7 <= days:
                parent_fish += 7
                queue.append(parent_fish)
            parent_fish = queue.popleft()
            parent_fish += 2
            fishes += 1
    return fishes


print(day6_2(18))
