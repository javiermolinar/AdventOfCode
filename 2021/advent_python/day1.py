from utils import get_data


def day1_1():
    "Count the number of times a number increases respect to the previous one"
    data = get_data(1, int)
    count = 0
    last_measurent = data[0]
    for num in data:
        if num > last_measurent:
            count += 1
        last_measurent = num
    return count


def day1_2():
    data = get_data(1, int)
    count = 0
    index = 0
    last_measurement = sum(data[:3])
    while last_measurement != 0:
        measurement = sum(data[index : index + 3])
        if measurement > last_measurement:
            count += 1
        index += 1
        last_measurement = measurement

    return count
