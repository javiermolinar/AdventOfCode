from utils import get_data
from collections import Counter
import string


def get_polymerization(steps, template, rules):
    counts = {x: 0 for x in string.ascii_uppercase[:28]} | Counter(list(template))
    pairs = {rule: 0 for rule in rules.keys()} | {template[i : i + 2]: 1 for i in range(len(template) - 1)}
    for _ in range(steps):
        previous_counts = [(key, value) for key, value in pairs.items() if value > 0]
        for pair, count in previous_counts:
            counts[rules[pair]] += count
            pairs[f"{pair[0]}{rules[pair]}"] += count
            pairs[f"{rules[pair]}{pair[1]}"] += count
        for pair, count in previous_counts:
            pairs[pair] -= count
    return max(counts.values()) - min([x for x in counts.values() if x > 0)


template = get_data(14)[0]
rules = {rule: insertion for rule, insertion in [x.split(" -> ") for x in get_data(14)[2:]]}


def day14_1():
    print(get_polymerization(10, template, rules))


def day14_2():
    print(get_polymerization(1000, template, rules))


day14_2()
