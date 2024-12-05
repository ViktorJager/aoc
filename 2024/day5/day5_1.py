### AOC Day 5-1 ###

import math

INPUT = "aoc/2024/day5/input.txt"


def read_lines(path):
    with open(path, "r") as file:
        lines = [line.strip() for line in file]
    return lines


def parse_data(data):
    page_rules = []
    page_ordering = []
    for entry in data:
        if '|' in entry:
            page_rules.append(entry.split('|'))
        if ',' in entry:
            page_ordering.append(entry.split(','))
    return page_rules, page_ordering
        

lines = read_lines(INPUT)
page_rules, page_ordering = parse_data(lines)
correct_orderings = []

rule_break = False
for order in page_ordering:
    rule_break = False
    print(order)
    for i, number in enumerate(order):
        for upcoming_number in order[i+1:]:
            if [upcoming_number, number] in page_rules:
                rule_break = True
                continue
            
    if not rule_break:
        correct_orderings.append(order)


sum = 0
for order in correct_orderings:
    mid_index = math.ceil((len(order) - 1) / 2)
    sum += int(order[mid_index])
    
    
print(sum)