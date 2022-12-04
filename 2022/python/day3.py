import string
from utils import get_data

char_dict = {k: v + 1 for (v, k) in enumerate(string.ascii_lowercase)}
char_dict |= {k: v + 27 for (v, k) in enumerate(string.ascii_uppercase)}
input = get_data(3)


def get_dup_priority(rucksack):
    halve = len(rucksack) // 2
    set1, set2 = (set(rucksack[:halve]), set(rucksack[halve:]))
    return sum([char_dict[v] for v in set1.intersection(set2)])


def get_common_badge_priority(rs1, rs2, rs3):
    return sum([char_dict[v] for v in set(rs1).intersection(set(rs2).intersection(set(rs3)))])


def day3_1():
    return sum([get_dup_priority(rucksack) for rucksack in input])


def day3_2():
    groups = [input[i : i + 3] for i in range(0, len(input), 3)]
    return sum([get_common_badge_priority(*group) for group in groups])
