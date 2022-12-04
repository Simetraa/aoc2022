import string

from aocd import data, submit

lines = data.splitlines()


def get_priority(char: str) -> int:
    return string.ascii_letters.index(char) + 1


items: list[str] = []

for i in range(0, len(lines), 3):
    group = [set(x) for x in lines[i:i+3]]

    item = set.intersection(*group).pop()
    items.append(item)

priority_sum = sum([get_priority(x) for x in items])

submit(priority_sum)
