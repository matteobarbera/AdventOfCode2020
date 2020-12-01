from itertools import permutations
from math import prod


def read_input():
    entries = []
    with open("day1_input.txt")as f:
        for line in f:
            entries.append(int(line))
    return entries


def sum_to_2020(n_entries: int):
    entries = read_input()
    for p in permutations(entries, n_entries):
        if sum(p) == 2020:
            print(tuple(p))
            return prod(p)


if __name__ == "__main__":
    print("="*10 + " Part 1 " + "="*10)
    day1_part1_solution = sum_to_2020(2)
    print(f"Product of 2020 sum: {day1_part1_solution}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    day1_part2_solution = sum_to_2020(3)
    print(f"Product of 2020 sum: {day1_part2_solution}")
