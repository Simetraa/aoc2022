from aocd import data, submit

array = data.split("\n\n")

elves = {}

for i, elf in enumerate(array):
    calories = sum([int(c) for c in elf.split("\n")])
    elves[i] = calories

sorted_elves = list({c: elves[c]
                     for c in sorted(elves, key=elves.get, reverse=True)}.values())

submit(sum(sorted_elves[0:3]))
