from utils import get_data
from collections import namedtuple

File = namedtuple("File", ["name", "size"])


class Directory:
    def __init__(self, name, parent_dir):
        self.name = name
        self.directories = []
        self.files = []
        self.size = 0
        self.parent_dir = parent_dir


def list_dir(current_dir, input, current_pos):
    def update_sizes(current_dir, size):
        if not current_dir:
            return
        current_dir.size += size
        update_sizes(current_dir.parent_dir, size)

    lines = 1
    while (current_pos + lines) < len(input) and "$" not in input[current_pos + lines]:
        metadata, name = input[current_pos + lines].split(" ")
        if metadata.isnumeric():
            current_dir.files.append(File(name, int(metadata)))
            update_sizes(current_dir, int(metadata))
        else:
            current_dir.directories.append(Directory(name, current_dir))
        lines += 1
    return lines


def read_input(input, current_dir):
    i = 0
    while i < len(input):
        line = input[i]
        if "cd" in line:
            _, _, dir = line.split(" ")
            if dir == "..":
                current_dir = current_dir.parent_dir
            elif dir != "/":
                current_dir = [d for d in current_dir.directories if d.name == dir][0]
            i += 1
        else:
            i += list_dir(current_dir, input, i)


def get_sizes(current_dir, sizes):
    sizes.append(current_dir.size)
    if not current_dir.directories:
        return
    for d in current_dir.directories:
        get_sizes(d, sizes)


def day7_1():
    root = Directory("/", None)
    read_input(get_data(7), root)
    sizes = []
    get_sizes(root, sizes)
    return sum([s for s in sizes if s <= 100000])


def day7_2():
    root = Directory("/", None)
    read_input(get_data(7), root)
    sizes = []
    get_sizes(root, sizes)
    return min([s for s in sizes if s >= 30_000_000 - (70_000_000 - root.size)])
