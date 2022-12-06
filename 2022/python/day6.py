from utils import get_data


def get_first_marker(marker_len):
    input = get_data(6)[0]
    for i in range(len(input)):
        if len(set(input[i : i + marker_len])) == marker_len:
            return i + marker_len


def day6_1():
    return get_first_marker(4)


def day6_2():
    return get_first_marker(14)
