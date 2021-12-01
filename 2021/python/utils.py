def get_data(day: int, parser=str, sep="\n") -> list:
    "Split the day's input file into sections separated by `sep`, and apply `parser` to each."
    sections = open(f"../data/input{day}.txt").read().rstrip().split(sep)
    return [parser(section) for section in sections]
