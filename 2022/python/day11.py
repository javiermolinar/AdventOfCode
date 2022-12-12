from utils import get_data
from math import lcm


class Operation:
    def __init__(self, operand_a, operand_b, operation):
        self.operand_a = operand_a
        self.operand_b = operand_b
        self.operation = operation

    def execute(self, item):
        a = item if self.operand_a == "old" else int(self.operand_a)
        b = item if self.operand_b == "old" else int(self.operand_b)
        match self.operation:
            case "+":
                return a + b
            case "*":
                return a * b


class Test:
    def __init__(self, divisor, true_monkey, false_monkey):
        self.divisor = divisor
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

    def test(self, item):
        return self.true_monkey if item % self.divisor == 0 else self.false_monkey


class Monkey:
    def __init__(self, starting_items, operation, test, relief=True):
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.inspected_items = 0
        self.lcm = 0
        self.relief = relief

    def turn(self):
        if not self.items:
            return (-1, 0)
        else:
            self.inspected_items += 1
            item = self.operation.execute(self.items.pop(0))
            item = item // 3 if self.relief else item % self.lcm
            return (self.test.test(item), item)


def get_monkey_bussiness(rounds, relief):
    input = get_data(11)
    monkeys_input = [input[i : i + 7] for i in range(0, len(input), 7)]
    monkeys = []
    worries = []
    for m in monkeys_input:
        starting_items = [int(a) for a in m[1].split(":")[1].split(",")]
        operand_a, operation, operand_b = m[2].split("=")[1].strip().split(" ")
        test_divisor = int(m[3].split("by")[1])
        monkey_true = int(m[4].split("monkey")[1])
        monkey_false = int(m[5].split("monkey")[1])
        operation = Operation(operand_a, operand_b, operation)
        test = Test(test_divisor, monkey_true, monkey_false)
        worries.extend(starting_items)
        monkeys.append(Monkey(starting_items, operation, test, relief))

    least_common_multiple = lcm(*worries)
    for monkey in monkeys:
        monkey.lcm = least_common_multiple

    for _ in range(rounds):
        for monkey in monkeys:
            throw_to = 0
            while throw_to != -1:
                throw_to, item = monkey.turn()
                if throw_to != -1:
                    monkeys[throw_to].items.append(item)

    activity = sorted([m.inspected_items for m in monkeys], reverse=True)
    return activity[0] * activity[1]


def day11_1():
    print(get_monkey_bussiness(20, True))


def day11_2():
    print(get_monkey_bussiness(10000, False))


day11_1()
