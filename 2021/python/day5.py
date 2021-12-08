from utils import get_data

data = [x.split(" -> ") for x in get_data(5, str)]
vents = [[(int(z.split(",")[0]), int(z.split(",")[1])) for z in y] for y in data]


def next_position(current, end):
    if current == end:
        return current
    return current + 1 if current < end else current - 1


def get_points(vent_lines):
    lines = {}
    for line in vent_lines:
        current_position = (line[0][0], line[0][1])
        while True:
            if current_position in lines:
                lines[current_position] += 1
            else:
                lines[current_position] = 1
            next = (
                next_position(current_position[0], line[1][0]),
                next_position(current_position[1], line[1][1]),
            )
            if current_position == next:
                break
            current_position = next
    return len([x for x in lines.values() if x >= 2])


def day5_1():
    lines = [
        lines
        for lines in vents
        if lines[0][0] == lines[1][0] or lines[0][1] == lines[1][1]
    ]
    print(get_points(lines))


def day5_2():
    print(get_points(vents))
