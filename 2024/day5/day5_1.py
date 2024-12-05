### AOC Day 5-1 ###

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
        


# for i, numbers in enumerate(page_rules):
#     first = numbers[0]
#     second = numbers[1]
    
#     primary_number = first
    
#     for j, following_numbers in enumerate(page_rules[i+1:], 1):
#         following_first = following_numbers[0]
#         following_second = following_numbers[1]
        
#         if first == following_second and following_first > first:
#             primary_number = following_first
#             if primary_number not in order:
#                 order.insert(i, primary_number)
#             page_rules.pop(j)
            
#             i += 1
#             continue
#             pass
#         pass
#     pass
     

     
# lines = read_lines(INPUT)
# page_rules, page_ordering = parse_data(lines)

# order = [page_rules[0][0], page_rules[0][1]]


# for i, numbers in enumerate(page_rules, 1):
#     first = numbers[0]

#     for following_numbers in page_rules[i+1:]:
#         following_first = following_numbers[0]
#         following_second = following_numbers[1]
        
#         if first == following_second:
#             if first in order and following_first not in order:
#                 idx = order.index(first)
#                 order.insert(idx, following_first) 
#                 continue
#             else:
#                 if following_first not in order:
#                     order.append(following_first)
                

# lines = read_lines(INPUT)
# page_rules, page_ordering = parse_data(lines)


# order = [page_rules[0][0], page_rules[0][1]]

# rules_copy = page_rules.copy()


# current_number = order[0]

# for i, numbers in enumerate(rules_copy):
#     if current_number == numbers[1]:
#         order.index(current_number)
#         order.insert(order.index(current_number), numbers[0])



# def find_first(num_mapping):
#     for k, v in num_mapping.items():
#         if len(v["after"]) == 0:
#             return k

# def rm_references(entry, num_mapping):
#     for k, v in num_mapping.items():
#         if k == entry:
#             continue
#         if entry in v["after"]:
#             v["after"].remove(entry)
#         if entry in v["before"]:
#             v["before"].remove(entry)
            
#     num_mapping.pop(entry, None)
       
# lines = read_lines(INPUT)
# page_rules, page_ordering = parse_data(lines)

# flatten_list = list(set(sum(page_rules, [])))

# num_mapping = {}
# for number in flatten_list:
#     num_mapping[number] = {
#         "before": [],
#         "after": [],
#     }
#     for n in page_rules:
#         if n[0] == number:
#             num_mapping[number]["before"].append(n[1])
#         if n[1] == number:
#             num_mapping[number]["after"].append(n[0])
 
        

# order = []
    
# for x in range(len(num_mapping)):
#     first = find_first(num_mapping)
#     rm_references(first, num_mapping)
#     order.append(first)
    
    
# print(order)
# for k, v in num_mapping.items():
#     print("after")
#     print(f"{(v['after'])}")
#     print("before")
#     print(f"{(v['before'])}")
#     print()
# import json
# b = json.dumps(num_mapping, indent=4)
# print(b)

import math

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