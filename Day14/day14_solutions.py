import re


def process_line():
    with open("day14_input.txt") as f:
        for line in f:
            no_whitespace = "".join(line.split())
            comm, val = no_whitespace.split("=")
            yield comm, val


def apply_bitmask(mask, num):
    binary = "{:b}".format(int(num))  # convert to binary without 0b
    binary = [*binary.zfill(36)]  # pad to match bitmask length
    for i, bit in enumerate(mask):
        if bit != "X":
            binary[i] = bit
    return int("".join(binary), 2)


def day14_part1():
    initialization_values = {}
    mask = None
    for c, v in process_line():
        if c == "mask":
            mask = v
        else:
            address = re.match(r"mem\[(\d+)", c)[1]
            initialization_values[address] = apply_bitmask(mask, v)
    sum = 0
    for val in initialization_values.values():
        sum += val
    return sum


def day14_part2():
    pass


if __name__ == "__main__":
    print("=" * 10 + " Part 1 " + "=" * 10)
    print(f"Sum of initialization values: {day14_part1()}")
    print("=" * 10 + " Part 1 " + "=" * 10)
    print(f"Sum of initialization values: {day14_part2()}")
