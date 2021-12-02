from utils import get_data


def day2_1():
    "Return the multiplication of depth and horizontal lengh"
    data = [(st.split(" ")[0], int(st.split(" ")[1])) for st in get_data(2, str)]
    horizontal = sum([st[1] for st in data if "forward" in st[0]])
    down = sum([st[1] for st in data if "down" in st[0]])
    up = sum([st[1] for st in data if "up" in st[0]])
    return horizontal * (down - up)


def day2_2():
    "Return the multiplication of depth and horizontal lengh with aim"
    data = [(st.split(" ")[0], int(st.split(" ")[1])) for st in get_data(2, str)]
    aim = 0
    horizontal = 0
    depth = 0
    for measurement, unit in data:
        match measurement:
            case "forward":
                horizontal += unit
                depth += aim * unit
            case "down":
                aim += unit
            case "up":
                aim -= unit
    return horizontal * depth


print(day2_1())
