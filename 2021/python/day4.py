from typing import NamedTuple
from utils import get_data


Cell = NamedTuple("Cell", [("number", int), ("marked", int)])


def get_bingo_data():
    data = get_data(4, str)
    input = [int(x) for x in data.pop(0).split(",")]
    cells = [
        [Cell(int(b), False) for b in a if b != ""]
        for a in [x.split(" ") for x in [z for z in data if len(z) > 1]]
    ]
    bingos = [cells[i : i + 5] for i in range(0, len(cells), 5)]
    return (input, bingos)


def get_score(bingo, last_number):
    return (
        sum([sum([x.number for x in line if not x.marked]) for line in bingo])
        * last_number
    )


def is_winner_bingo(bingo, number):
    for line in bingo:
        if Cell(number, False) in line:
            line[line.index(Cell(number, False))] = Cell(number, True)
            if len([x.number for x in line if x.marked]) == 5:
                return (bingo, number)
            for i in range(5):
                if len([x[i].number for x in bingo if x[i].marked]) == 5:
                    return (bingo, number)


def get_winner_bingo(input, bingos):
    for number in input:
        for bingo in bingos:
            if is_winner_bingo(bingo, number):
                return (bingo, number)


def get_last_winner_bingo(input, bingos):
    last_winner_bingo = []
    for number in input:
        for bingo in bingos:
            if is_winner_bingo(bingo, number):
                last_winner_bingo = bingo
                bingos.remove(bingo)
                if len(bingos) == 1:
                    return (bingo, number)
    return (last_winner_bingo, input[-1])


def day4_1() -> int:
    return get_score(*get_winner_bingo(*get_bingo_data()))


def day4_2() -> int:
    return get_score(*get_last_winner_bingo(*get_bingo_data()))
