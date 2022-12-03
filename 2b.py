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

inverted_counters = {v: k for k, v in counters.items()}

total = 0
for line in lines:
    a, outcome = line.split()
    a = conv[a]

    if outcome == "X":  # lose
        move = counters[a]
        print(
            f"[LOSE] Enemy has {a} so we play {move}")
        total += 0 + score[move]
    elif outcome == "Z":  # win
        move = inverted_counters[a]
        print(
            f"[WIN] Enemy has {a} so we play {move}")
        total += 6 + score[move]
    else:  # draw
        move = a
        print(f"[DRAW] Enemy has {a} so we play {move}")
        total += 3 + score[a]

submit(total)
