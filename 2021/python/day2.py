from utils import get_data

def day2_1():
    "Return the multiplication of depth and horizontal lengh"
    data = get_data(2, str)
    horizontal = sum([int(st.split(" ")[1]) for st in data if "forward" in st])
    down = sum([int(st.split(" ")[1]) for st in data if "down" in st])
    up = sum([int(st.split(" ")[1]) for st in data if "up" in st])
    return horizontal * (down - up)


def day2_2():
    "Return the multiplication of depth and horizontal lengh"
    data = get_data(2, str)
    aim = 0
    horizontal = 0
    depth = 0
    for movement, unit in [(x.split(" ")[0], int(x.split(" ")[1])) for x in data]:
        match movement:
            case "forward":
                horizontal += unit
                depth += aim * unit
            case "down":
                aim += unit
            case "up":
                aim -= unit
    return horizontal * depth