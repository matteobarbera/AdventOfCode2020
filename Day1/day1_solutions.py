from itertools import permutations
from math import prod


def read_input():
    lst = []
    with open("day1_input.txt")as f:
        for line in f:
            lst.append(int(line))
    return lst


def sum_to_2020(lst: list, n: int):
    for p in permutations(lst, n):
        if sum(p) == 2020:
            print(tuple(p))
            return prod(p)


if __name__ == "__main__":
    entries = read_input()
    print("="*10 + " Part 1 " + "="*10)
    day1_part1_solution = sum_to_2020(entries, 2)
    print(f"Product of 2020 sum: {day1_part1_solution}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    day1_part2_solution = sum_to_2020(entries, 3)
    print(f"Product of 2020 sum: {day1_part2_solution}")
