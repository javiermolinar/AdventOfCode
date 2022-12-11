from utils import get_data

input = get_data(9)


def move_tail(head_pos, knot_pos, direction):
    if head_pos[0] == knot_pos[0]:  # Same row
        if direction == "L":
            knot_pos[1] -= 1
        else:
            knot_pos[1] += 1
    elif head_pos[1] == knot_pos[1]:  # Same column
        if direction == "U":
            knot_pos[0] -= 1
        else:
            knot_pos[0] += 1
    else:  # Diagonal
        if head_pos[0] > knot_pos[0]:
            knot_pos[0] += 1
            if head_pos[1] < knot_pos[1]:
                knot_pos[1] -= 1
            else:
                knot_pos[1] += 1
        else:
            knot_pos[0] -= 1
            if head_pos[1] < knot_pos[1]:
                knot_pos[1] -= 1
            else:
                knot_pos[1] += 1


def move(head_pos, knots, direction, movements, visited):
    for i in range(movements):
        match direction:
            case "L":
                head_pos[1] -= 1
            case "R":
                head_pos[1] += 1
            case "U":
                head_pos[0] -= 1
            case "D":
                head_pos[0] += 1

        head = (head_pos[0], head_pos[1])
        i = 0
        while abs(head[0] - knots[i][0]) >= 2 or abs(head[1] - knots[i][1]) >= 2:
            move_tail(head, knots[i], direction)
            head = (knots[i][0], knots[i][1])
            i += 1
            if i == len(knots):
                break

        if (knots[-1][0], knots[-1][1]) not in visited:
            visited.add((knots[-1][0], knots[-1][1]))


def day9_1():
    visited = {(0, 0)}
    head = [0, 0]
    knots = [[0, 0] for _ in range(1)]

    for line in input:
        direction, movements = line.split(" ")
        move(head, knots, direction, int(movements), visited)


def day9_2():
    visited = {(0, 0)}
    head = [0, 0]
    knots = [[0, 0] for _ in range(9)]  # This should work the same but it doesn't -_-

    for line in input:
        direction, movements = line.split(" ")
        move(head, knots, direction, int(movements), visited)
    print(len(visited))


day9_2()
