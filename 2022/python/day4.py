from utils import get_data


def get_range(r) -> set:
    a, b = r.split("-")
    return set(range(int(a), int(b) + 1))


def get_results(f):
    return sum([f(get_range(d.split(",")[0]), get_range(d.split(",")[1])) for d in get_data(4)])


def day4_1():
    return get_results(lambda r1, r2: int(r1.issubset(r2) or r2.issubset(r1)))


def day4_2():
    return get_results(lambda r1, r2: 1 if r1.intersection(r2) else 0)
