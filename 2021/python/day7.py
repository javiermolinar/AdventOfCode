from utils import get_data


def day7_1():
    "Calculate the shortest distance between all horizontal points"
    n = get_data(7, str)
    print(min([sum([abs(pos - x) for x in n]) for pos in n]))


def day7_2():
    "Calculate the shortest distance between all horizontal points with offset"

    def get_triangle(n):
        return (n * (n - 1) / 2) + n

    n = get_data(7, str)
    print(min([sum([get_triangle(abs(pos - x)) for x in n]) for pos in range(1, max(n))]))
