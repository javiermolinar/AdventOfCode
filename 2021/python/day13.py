from utils import get_data

points = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in get_data(13) if "fold along" not in x and x != ""]
folds = [(x.split("=")[0].split("fold along ")[1], int(x.split("=")[1])) for x in get_data(13) if "fold along" in x]


def fold(matrix, folding_type, fold_no):
    x_size = len(matrix[0]) if folding_type == "y" else fold_no
    y_size = fold_no if folding_type == "y" else len(matrix)
    range_i = range(fold_no, len(matrix)) if folding_type == "y" else range(len(matrix))
    range_j = range(len(matrix[0])) if folding_type == "y" else range(fold_no, len(matrix[0]))

    folded_matrix = [[x for j, x in enumerate(lines) if j < x_size] for i, lines in enumerate(matrix) if i < y_size]

    for i in range_i:
        for j in range_j:
            if matrix[i][j] == "#":
                if folding_type == "y":
                    folded_matrix[(fold_no - i) % fold_no][j] = "#"
                else:
                    folded_matrix[i][(fold_no - j) % fold_no] = "#"
    return folded_matrix


def get_initial_matrix(points):
    res = [["." for _ in range(max([x for (x, _) in points]) + 1)] for _ in range(max([y for (_, y) in points]) + 1)]
    for x, y in points:
        res[y][x] = "#"
    return res


def day13_1():
    print(sum([sum([1 for x in y if x == "#"]) for y in fold(get_initial_matrix(points), *folds[0])]))


def day13_2():
    matrix = get_initial_matrix(points)
    for fold_operation in folds:
        matrix = fold(matrix, *fold_operation)
    print(matrix)
