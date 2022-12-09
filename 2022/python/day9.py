from utils import get_data

input = get_data(9)

head_pos = [0, 0]
tail_pos = [0, 0]
visited = {(0, 0): 1}


def updated_visited(visited, position):
    if position in visited:
        visited[position] += 1
    else:
        visited[position] = 1


def move_tail(head_pos, tail_pos, direction, visited):
    if head_pos[0] == tail_pos[0]:  # Same row
        if direction == "L":
            tail_pos[1] -= 1
        else:
            tail_pos[1] += 1
    elif head_pos[1] == tail_pos[1]:  # Same column
        if direction == "U":
            tail_pos[0] -= 1
        else:
            tail_pos[0] += 1
    else:  # Diagonal
        if head_pos[0] > tail_pos[0]:
            tail_pos[0] += 1
            if head_pos[1] < tail_pos[1]:
                tail_pos[1] -= 1
            else:
                tail_pos[1] += 1
        else:
            tail_pos[0] -= 1
            if head_pos[1] < tail_pos[1]:
                tail_pos[1] -= 1
            else:
                tail_pos[1] += 1
    updated_visited(visited, (tail_pos[0], tail_pos[1]))


def move(head_pos, tail_pos, direction, movements, visited):
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

        should_move_tail = abs(head_pos[0] - tail_pos[0]) >= 2 or abs(head_pos[1] - tail_pos[1]) >= 2
        if should_move_tail:
            move_tail(head_pos, tail_pos, direction, visited)


for line in input:
    direction, movements = line.split(" ")
    move(head_pos, tail_pos, direction, int(movements), visited)
