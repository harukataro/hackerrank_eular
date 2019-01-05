#!/bin/python3

import sys


def make_arr_max(grid_in, x, y, x_mov, y_mov):
    max_num = 0
    multiple_box = [0, 0, 0, 0]
    while x < 20 and y < 20 and x >= 0 and y >= 0:
        multiple_box.pop(0)
        multiple_box.append(grid_in[x][y])
        max_num = max(max_num, multiple_box[0] * multiple_box[1] * multiple_box[2] * multiple_box[3])
        x += x_mov
        y += y_mov
    return max_num


def solve(grid_in):
    max_num = 0

    # Column
    for y in range(0, 20):
        max_num = max(max_num, make_arr_max(grid_in, 0, y, 1, 0))
    # Line
    for x in range(0, 20):
        max_num = max(max_num, make_arr_max(grid_in, x, 0, 0, 1))
    # Top Line to Right-Down
    for x1 in range(0, 17):
        max_num = max(max_num, make_arr_max(grid_in, x1, 0, 1, 1))
    # Left line to Right-Down
    for y1 in range(0, 17):
        max_num = max(max_num, make_arr_max(grid_in, 0, y1, 1, 1))
    # Top Line to Left-Down
    for x2 in range(3, 20):
        max_num = max(max_num, make_arr_max(grid_in, x2, 0, -1, 1))
    # Right line to Left-Down
    for y2 in range(0, 17):
        max_num = max(max_num, make_arr_max(grid_in, 19, y2, -1, 1))

    return max_num


grid = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.append(grid_t)

print(solve(grid))
