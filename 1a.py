from aocd import data, submit

array = data.split("\n\n")

max_index = 0
max_count = 0

for i, elf in enumerate(array):
    calories = sum([int(c) for c in elf.split("\n")])
    if calories > max_count:
        max_count = calories
        max_index = i

submit(max_count)