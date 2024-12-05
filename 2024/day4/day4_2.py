### AOC Day 4-2 ###

from collections import Counter

INPUT = "aoc/2024/day4/input.txt"


def read_lines(path):
    with open(path, "r") as file:
        lines = [[char for char in line.strip()] for line in file]
    return lines


def find_letter(lines, dirx, diry, posx, posy) -> bool:
    try:
        position_y = posy + (1 * diry)
        position_x = posx + (1 * dirx)

        if position_y < 0 or position_x < 0:
            return "Q"

        return lines[position_y][position_x]

    except IndexError:
        return "Q"
    return "Q"


def find_word(lines, posx, posy) -> bool:
    if lines[y][x] != "A":
        return 0

    diagonal_1 = [
        find_letter(lines, 0, 0, posx, posy),
        find_letter(lines, 1, 1, posx, posy),
        find_letter(lines, -1, -1, posx, posy),
    ]
    diagonal_2 = [
        find_letter(lines, 0, 0, posx, posy),
        find_letter(lines, 1, -1, posx, posy),
        find_letter(lines, -1, 1, posx, posy),
    ]
    
    if all(diagonal_1):
        d1 = ''.join(sorted(diagonal_1))
    if all(diagonal_1):
        d2 = ''.join(sorted(diagonal_2))
        
    if d1 == "AMS" and d2 == "AMS":
        return 1
    return 0


lines = read_lines(INPUT)

correct_words = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        correct_words += find_word(lines, x, y)

print(correct_words)
