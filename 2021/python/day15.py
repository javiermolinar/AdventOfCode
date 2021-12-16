from collections import deque
from utils import get_data

data = [[int(x) for x in y] for y in get_data(15)]


def get_minimun_risk(x, y, data, path, min_risk, counter, counter_risk, slice):
    current_risk = min_risk
    if sum(path) + data[x][y] > min_risk:
        path.pop()
        return min_risk

    if (x, y) in counter:
        if counter[(x, y)] > sum(path) - path[0]:
            if (x, y) in counter_risk:
                if counter_risk[(x, y)] - (counter[(x, y)] - (sum(path) - path[0])) > min_risk:
                    return min_risk
            counter[(x, y)] = sum(path) - path[0]
        else:
            path.pop()
            return min_risk
    elif len(path) > 0:
        counter[(x, y)] = sum(path) - path[0]

    # if x <= slice[0] and len(path) > 1 and ((sum(path) - path[0]) + slice[1]) >= min_risk:
    #     path.pop()
    #     return min_risk

    if x + 1 >= len(data):
        # print(sum(path) + sum(data[x][y : len(data[0])]) - path[0])
        summatory = sum(path) + sum(data[x][y : len(data[0])]) - path[0]
        path.pop()
        return summatory

    for j in range(len(data[0])):

        r = sum(data[x][j : y + 1]) if j < y else sum(data[x][y : j + 1])
        risk = get_minimun_risk(x + 1, j, data, deque([*path, r]), current_risk, counter, counter_risk, slice)
        if risk < current_risk:
            current_risk = risk

    if (x, y) in counter_risk:
        if counter_risk[(x, y)] > risk:
            counter_risk[(x, y)] = risk
    else:
        counter_risk[(x, y)] = risk

    return current_risk


def can_continue(path, current_no, x, min_risk, min_risk_slices):
    sum_risk = sum(path) + current_no
    sum_min_risk_slices = 0
    if min_risk_slices:
        sum_min_risk_slices = sum([min_risk_slices[value] for value in min_risk_slices.keys() if int(value) > x])
    return (sum_risk < min_risk) and (sum_risk + sum_min_risk_slices) < min_risk


def get_min_risk_greadily(data):
    return sum([x[0] for x in data]) + sum([x for x in data[len(data) - 1]])


def get_min_risk_for_slices(data):
    counter = {}
    for i in range(0, len(data), 2):
        counter[i] = get_minimun_risk(0, 0, data[i : i + 2], deque([]), get_min_risk_greadily(data[i : i + 2]), None)
    return counter


# slices = get_min_risk_for_slices(data)
print(get_minimun_risk(0, 0, data[2:4], deque([]), get_min_risk_greadily(data[2:4]), {}, {}, (8, 22)))
