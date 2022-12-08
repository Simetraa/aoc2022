from aocd import data, submit


forest = [i for i in data.splitlines()]


def scenic_score(x: int, y: int) -> int:
    tree_height = forest[y][x]

    left_row = list(reversed(forest[y][:x]))  # left to right
    right_row = list(forest[y][x + 1:][:])  # right to left
    top_col = list(reversed([i[x] for i in forest][:y]))  # top to bottom
    bottom_col = [i[x] for i in forest][y + 1:]  # bottom to top

    score = 1
    for dir in [left_row, right_row, top_col, bottom_col]:
        distance = 0
        for t in dir:
            distance += 1
            if t >= tree_height:
                break
        score *= distance

    return score


maximum = 0
for y in range(len(forest)):
    for x in range(len(forest[y])):
        maximum = max(scenic_score(x, y), maximum)

submit(maximum)
