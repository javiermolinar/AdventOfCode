from typing import List
from utils import get_data


def to_int(bin_num: List[int]) -> int:
    return int("".join(map(str, bin_num)), 2)


def day3_1():
    "Return the multiplication of depth and horizontal lengh"
    data = get_data(3, str)
    sum_results = [sum(int(num[i]) for num in data) for i, _ in enumerate(data[0])]
    gamma = [(1 if x > len(data) / 2 else 0) for x in sum_results]
    epsilon = [(1 if x == 0 else 0) for x in gamma]
    return to_int(gamma) * to_int(epsilon)


def day3_2():
    def get_rating(data: List[str], most_common: bool = True) -> int:
        index = 0
        rating = data[:]
        while len(rating) > 1:
            sum_results = [
                sum(int(num[i]) for num in rating) for i, _ in enumerate(rating[0])
            ]
            if most_common:
                gamma = [(1 if x >= len(rating) / 2 else 0) for x in sum_results]
            else:
                gamma = [(1 if x < len(rating) / 2 else 0) for x in sum_results]
            rating = [x for x in rating if int(x[index]) == gamma[index]]
            index += 1
        return to_int(rating[0])

    data = get_data(3, str)

    return get_rating(data) * get_rating(data, False)


print(day3_2())
