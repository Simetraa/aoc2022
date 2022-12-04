from aocd import data, submit

lines = data.splitlines()

count = 0
for line in lines:
    a, b = line.split(",")
    a, b = a.split("-"), b.split("-")
    a = range(int(a[0]), int(a[1]) + 1)
    b = range(int(b[0]), int(b[1]) + 1) # increment by one as stop is omitted from the resulting range

    a = set(a)
    b = set(b)

    if a.issubset(b) or b.issubset(a):
        count += 1

submit(count)