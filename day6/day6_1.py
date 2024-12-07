### AOC Day 5-2 ###


INPUT = "aoc/2024/day6/input_custom.txt"


def read_lines(path):
    with open(path, "r") as file:
        lines = [list(line.strip()) for line in file]
    return lines


def start_position(map):
    directions = {
        "^": 0,
        "v": 90,
        ">": 180,
        "<": 270, 
    }

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] in directions.keys():
                return (x, y), directions[map[y][x]]


def get_tile(map, pos):
    return map[pos[1]][pos[0]]


def next_pos(pos, dir):
    if dir == 0:
        return(pos[0], pos[1] - 1)
    if dir == 90:
        return(pos[0] + 1, pos[1])
    if dir == 180:
        return(pos[0], pos[1] + 1)
    if dir == 270:
        return(pos[0] - 1, pos[1])


def step(next_pos):
    return next_pos


def rotate(dir):
    return (dir + 90) % 360


def out_of_bounds(pos, map):
    posx = pos[0]
    posy = pos[1]

    if posx < 0 or posx >= len(map[0]):
        return True
    if posy < 0 or posy >= len(map):
        return True
    return False


def update_map(cmap, pos):
    cmap[pos[1]][pos[0]] = 'X'


def print_map(map):
    for row in map:
        print(''.join(row))


def distinct_positions(map):
    sum = 0
    for row in map:
        sum += row.count('X')
    return sum



from collections import deque
import copy
import time


class StateQueue:
    def __init__(self, max_size=3):
        self.queue = deque(maxlen=max_size)

    def add_state(self, state):
        self.queue.append(state)

    def get_states(self):
        return list(self.queue)


map = read_lines(INPUT)
cmap = copy.deepcopy(map)
start_pos, start_dir = start_position(map)
pos = start_pos
dir = start_dir

obstacle = "#"

time_loop = 0 
loop = True
states = StateQueue(max_size=3)


for y in range(len(map)):
    for x in range(len(map[y])):

        cmap = copy.deepcopy(map)
        pos = start_pos
        dir = start_dir

        if y == 9 and x == 7:
            hello = "d"

        if map[y][x] != obstacle or map[y][x] == start_pos:
            cmap[y][x] = obstacle

        while not out_of_bounds(next_pos(pos, dir), cmap) and loop:
            states.add_state(copy.deepcopy(cmap))
            update_map(cmap, pos)
            np = next_pos(pos, dir)
            nt = get_tile(map, np)

            if nt == obstacle:
                dir = rotate(dir)
                np = next_pos(pos, dir)
                nt = get_tile(map, np)
                pos = step(np)
            else:
                pos = step(np)


            print("\033[H\033[J", end="")
            print_map(cmap)
            time.sleep(0.2)

            if len(states.get_states()) > 2:
                maps = states.get_states()
                if maps[0] == maps[2]:
                    loop = False
                    time_loop += 1

        loop = True


print(time_loop)

