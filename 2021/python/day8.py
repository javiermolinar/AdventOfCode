from utils import get_data


data = [(x.split("|")[0].strip(), x.split("|")[1].strip()) for x in get_data(8, str)]
times = sum([len([x for x in y[1].split(" ") if len(x) in [2, 3, 4, 7]]) for y in data])
