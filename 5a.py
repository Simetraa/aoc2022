from aocd import data, submit

stack_data, instructions_data = data.split(
    "\n\n")[0].splitlines(), data.split("\n\n")[1].splitlines()

# ignore first char - it is a space
col_nums = stack_data[-1][1:-1].split("   ")
stacks = stack_data[:-1]


dict_stacks = {}
for s in reversed(stacks):
    for i in range(len(col_nums)):
        # extract formatted / padded data
        item = s[i * 3 + (1 * i) + 1]
        col_num = int(col_nums[i])
        if item != " ":
            if col_num not in dict_stacks:
                dict_stacks[col_num] = []
            dict_stacks[col_num].append(item)

for line in instructions_data:
    _, count, _, start, _, dest = line.split()
    count, start, dest = int(count), int(start), int(dest)
    for i in range(count):
        popped = dict_stacks[start].pop()
        dict_stacks[dest].append(popped)


out = ""
for i in range(len(col_nums)):
    out += dict_stacks[i+1][-1]

submit(out)
