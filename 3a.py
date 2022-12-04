import string

from aocd import data, submit

lines = data.splitlines()


def get_priority(char: str) -> int:
    return string.ascii_letters.index(char) + 1


shared: list[str] = []

for line in lines:
    line_len = len(line)
    compartment1, compartment2 = line[:line_len//2], line[line_len//2:]

    shared.extend(set(compartment1).intersection(set(compartment2)))

priority_sum = sum([get_priority(x) for x in shared])

submit(priority_sum)
