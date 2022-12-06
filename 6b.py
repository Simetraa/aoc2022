from aocd import data, submit


def find_message(buffer: str) -> int:
    for i in range(0, len(buffer)):
        sl = buffer[i:i+14]
        if len(sl) == len(set(sl)):
            return i + 14

    return -1


submit(find_message(data))
