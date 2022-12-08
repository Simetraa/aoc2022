from aocd import data, submit


forest = [i for i in data.splitlines()]


def is_visible(x: int, y: int) -> bool:
    tree_height = forest[y][x]

    if y >= len(forest) - 1 or y <= 0:
        return True
    if x >= len(forest[y]) - 1 or x <= 0:
        return True

    left_row = forest[y][:x]  # left to right
    right_row = forest[y][x + 1:]  # right to left
    top_col = [i[x] for i in forest][:y]  # top to bottom
    bottom_col = [i[x] for i in forest][y + 1:]  # bottom to top

    return any([max(arr) < tree_height for arr in [
        left_row, right_row, top_col, bottom_col]])


count = 0
for y in range(len(forest)):
    for x in range(len(forest[y])):
        if is_visible(x, y):
            count += 1

submit(count)
