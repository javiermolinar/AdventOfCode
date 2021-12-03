from typing import Callable, List
from utils import get_data


def to_int(bin_num: List[int]) -> int:
    return int("".join(map(str, bin_num)), 2)


def day3_1() -> int:
    "Return the multiplication of depth and horizontal lengh"
    data = get_data(3, str)
    sum_results = [sum(int(num[i]) for num in data) for i, _ in enumerate(data[0])]
    gamma = [(1 if x > len(data) / 2 else 0) for x in sum_results]
    epsilon = [(1 if x == 0 else 0) for x in gamma]
    return to_int(gamma) * to_int(epsilon)


def day3_2() -> int:
    def get_rating(
        data: List[str], index: int, get_common_value: Callable[[int, int], int]
    ) -> int:
        if len(data) == 1:
            return to_int(data[0])
        sum_results = [sum(int(num[i]) for num in data) for i, _ in enumerate(data[0])]
        common = [get_common_value(x, len(data) / 2) for x in sum_results]
        selected_numbers = [x for x in data if int(x[index]) == common[index]]
        return get_rating(selected_numbers, index + 1, get_common_value)

    data = get_data(3, str)
    oxigen_rating = get_rating(data, 0, lambda value, t: 1 if value >= t else 0)
    co2_rating = get_rating(data, 0, lambda value, t: 1 if value < t else 0)
    return oxigen_rating * co2_rating
