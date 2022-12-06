from aocd import data, submit


def find_marker(buffer: str) -> int:
    for i in range(0, len(buffer)):
        sl = buffer[i:i+4]
        if len(sl) == len(set(sl)):
            return i + 4

    return -1


submit(find_marker(data))
