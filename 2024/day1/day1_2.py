INPUT = "aoc/2024/day1/input.txt"


def read_lines(path):
    with open(path, 'r') as file:
        lines = [line.strip() for line in file]
    return lines

def number_occurance(n, list):
    occurances = 0
    for i in list:
        if i == n:
            occurances += 1
    return occurances

lines = read_lines(INPUT)

similarity = 0
left_list = []
right_list = []

for line in lines:
    entries = line.split("   ")
    left_list.append(int(entries[0]))
    right_list.append(int(entries[1]))


for num in left_list:
    similarity += num * number_occurance(num, right_list)

print(similarity)




