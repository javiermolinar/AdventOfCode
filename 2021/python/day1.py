from utils import get_data


def day1_1():
    "Count the number of times a number increases respect to the previous one"
    data = get_data(1, int)
    return len([depth for i, depth in enumerate(data) if i > 0 and depth > data[i - 1]])


def day1_2():
    "Count the number of time it increases as sliding window"
    data = get_data(1, int)
    count = 0
    for i, _ in enumerate(data):
        if i == len(data) - 3:
            break
        if sum(data[i : i + 3]) < sum(data[i + 1 : i + 4]):
            count += 1
    return count
