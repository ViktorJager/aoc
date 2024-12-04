### AOC Day 3-2 ###

import re

# INPUT = "aoc/2024/day2/input.txt"
INPUT = "/home/vjager/dev/apip/tools/z-test/aoc/day3/input.txt"


def read_file(path):
    with open(path, 'r') as file:
        content = file.read()
    return content

memory = read_file(INPUT)

# pattern = 'mul\([0-9]+\*([0-9]+)\)'
pattern = 'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)'
instructions = re.findall(pattern, memory)

valid_instructions = []
include_instruction = True
for instruction in instructions:
    if instruction == "don't()":
        include_instruction = False
        continue
    if instruction == "do()":
        include_instruction = True
        continue
    
    if include_instruction:
        valid_instructions.append(instruction)


sum_of_products = 0
pattern = '[0-9]+'
for instruction in valid_instructions:
    mul = re.findall(pattern, instruction)
    sum_of_products += int(mul[0]) * int(mul [1])


# print(memory)
print(sum_of_products)

a = 1