from utils import get_data


def is_visible(i, j, trees):
    tree = int(trees[i][j])
    if i == 0 or i == len(trees) - 1 or j == 0 or j == len(trees) - 1:
        return True
    return (
        max([int(trees[x][j]) for x in range(0, i)]) < tree
        or max([int(trees[x][j]) for x in range(i + 1, len(trees))]) < tree
        or max([int(trees[i][x]) for x in range(0, j)]) < tree
        or max([int(trees[i][x]) for x in range(j + 1, len(trees))]) < tree
    )


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

    tree = int(trees[i][j])
    top = get_score(tree, [int(trees[x][j]) for x in range(0, i)], True)
    bottom = get_score(tree, [int(trees[x][j]) for x in range(i + 1, len(trees))])
    left = get_score(tree, [int(trees[i][x]) for x in range(0, j)], True)
    right = get_score(tree, [int(trees[i][x]) for x in range(j + 1, len(trees))])
    return top * bottom * left * right


visibles = 0
best_score = 0
input = get_data(8)
for i in range(len(input)):
    for j in range(len(input)):
        if is_visible(i, j, input):
            visibles += 1
            score = scenic_score(i, j, input)
            if score > best_score:
                best_score = score

print(f"1: {visibles}")
print(f"2: {best_score}")
