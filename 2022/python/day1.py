from utils import read_lines


def get_calories():
    calory = 0
    for calory_count in read_lines(1):
        if calory_count == "\n":
            yield calory
            calory = 0
        else:
            calory += int(calory_count)


def day1_1():
    "Find the biggest sum of calories"
    return max(get_calories())


def day1_2():
    "Get the sum of the top tree calories"
    calories = [calory for calory in get_calories()]
    calories.sort(reverse=True)
    return sum(calories[:3])
