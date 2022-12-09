from utils import get_data
from functools import reduce
from itertools import chain
import operator


def scenic_score(i, j, trees):
    def get_score(tree, trees, reverse=False):
        score = 0
        if reverse:
            trees.reverse()
        for t in trees:
            score += 1
            if t >= tree:
                return score
        return score

    sides = [
        ([int(trees[x][j]) for x in range(0, i)], True),
        ([int(trees[x][j]) for x in range(i + 1, len(trees))], False),
        ([int(trees[i][x]) for x in range(0, j)], True),
        ([int(trees[i][x]) for x in range(j + 1, len(trees))], False),
    ]
    is_visible = len([True for x, _ in sides if len(x) == 0 or max(x) < int(trees[i][j])]) > 0
    score = reduce(operator.mul, [get_score(int(trees[i][j]), side, reverse) for side, reverse in sides], 1)
    return (is_visible, score)


input = get_data(8)
values = list(chain(*[[scenic_score(i, j, input) for j in range(len(input))] for i in range(len(input))]))
scores = [score for visible, score in values if visible]

print(f"1:{len(scores)}")
print(f"2:{max(scores)}")
