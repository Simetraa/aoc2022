from aocd import data, submit

lines = data.splitlines()

score = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

conv = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

counters = {
    "Rock": "Scissors",
    "Scissors": "Paper",
    "Paper": "Rock"
}

total = 0
for line in lines:
    a, b = line.split(" ")
    a, b = conv[a], conv[b]

    if a == b:
        total += 3 + score[b]
    elif a == counters[b]:
        total += 6 + score[b]
    else:
        total += 0 + score[b]

submit(total)