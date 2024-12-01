INPUT = "aoc/2024/day1/input.txt"


def read_lines(path):
    with open(path, 'r') as file:
        lines = [line.strip() for line in file]
    return lines


lines = read_lines(INPUT)

distance = 0
left_list = []
right_list = []

for line in lines:
    entries = line.split("   ")
    left_list.append(int(entries[0]))
    right_list.append(int(entries[1]))

left_list.sort()
right_list.sort()

for i in range(len(left_list)):
    if left_list[i] > right_list[i]:
        distance += left_list[i] - right_list[i]
    else:
        distance += right_list[i] - left_list[i]

print(distance)
