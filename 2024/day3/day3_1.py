### AOC Day 3-1 ###

import re

INPUT = "aoc/2024/day3/input.txt"


def read_file(path):
    with open(path, "r") as file:
        content = file.read()
    return content


memory = read_file(INPUT)

pattern = "mul\([0-9]+,[0-9]+\)"
valid_instructions = re.findall(pattern, memory)

sum_of_products = 0
pattern = "[0-9]+"
for instruction in valid_instructions:
    mul = re.findall(pattern, instruction)
    sum_of_products += int(mul[0]) * int(mul[1])

print(sum_of_products)
