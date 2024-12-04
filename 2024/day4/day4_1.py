### AOC Day 4-1 ###

from collections import Counter

INPUT = "aoc/2024/day4/input.txt"


def read_lines(path):
    with open(path, "r") as file:
        lines = [[char for char in line.strip()] for line in file]
    return lines


def find_word(word, lines, dirx, diry, posx, posy) -> bool:
    letters = ""
    try:
        for i in range(len(word)):
            position_y = posy + (i * diry)
            position_x = posx + (i * dirx)

            if position_y < 0 or position_x < 0:
                return False

            for char in lines[position_y][position_x]:
                letters += char

    except IndexError:
        return False

    if letters == word:
        return True
    return False


def find_words(word, lines, posx, posy) -> bool:
    return Counter(
        [
            find_word(word, lines, 1, 0, posx, posy),
            find_word(word, lines, -1, 0, posx, posy),
            find_word(word, lines, 0, 1, posx, posy),
            find_word(word, lines, 0, -1, posx, posy),
            find_word(word, lines, 1, 1, posx, posy),
            find_word(word, lines, 1, -1, posx, posy),
            find_word(word, lines, -1, -1, posx, posy),
            find_word(word, lines, -1, 1, posx, posy),
        ]
    )[True]


WORD = "XMAS"
lines = read_lines(INPUT)

correct_words = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        correct_words += find_words(WORD, lines, x, y)
        
print(correct_words)
