# Copyright 2024 Irene Bandera Moreno
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import copy

def get_starting_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '<':
                return (i, j) , 'west'
            if grid[i][j] == '>':
                return (i, j), 'east'
            if grid[i][j] == '^': 
                return (i, j), 'north'
            if grid[i][j] == 'v':
                return (i, j), 'south'

    return None

def move(grid, pos, orientation):
    i, j = pos
    if orientation == 'north':
        if i == 0:
            return None, None
        if grid[i-1][j] == '#':
            return (i, j), 'east'
        return (i-1, j), orientation
    if orientation == 'south':
        if i == len(grid) -1:
            return None, None
        if grid[i+1][j] == '#':
            return (i, j), 'west'
        return (i+1, j), orientation
    if orientation == 'east':
        if j == len(grid[i]) - 1:
            return None, None
        if grid[i][j+1] == '#':
            return (i, j), 'south'
        return (i, j+1), orientation
    if orientation == 'west':
        if j == 0:
            return None, None
        if grid[i][j-1] == '#':
            return (i, j), 'north'
        return (i, j-1), orientation
    
def print_pos(grid, pos, orientation):
    if orientation == 'north':
        grid[pos[0]][pos[1]] = '^'
    elif orientation == 'south':
        grid[pos[0]][pos[1]] = 'v'
    elif orientation == 'east':
        grid[pos[0]][pos[1]] = '>'
    elif orientation == 'west':
        grid[pos[0]][pos[1]] = '<'

def visited_positions(grid):
    count = 0
    for row in grid:
        for cell in row:
            if cell == 'X':
                count += 1
    return count

def get_obstacle(pos, orientation, grid, seen_positions):
    obstacle_x, obstacle_y = None, None
    if orientation == 'north':
        obstacle_x, obstacle_y = pos[0] - 1, pos[1]
    elif orientation == 'south':
        obstacle_x, obstacle_y = pos[0] + 1, pos[1]
    elif orientation == 'east':
        obstacle_x, obstacle_y = pos[0], pos[1] + 1
    elif orientation == 'west':
        obstacle_x, obstacle_y = pos[0], pos[1] - 1

    if obstacle_x < 0 or obstacle_x >= len(grid) or obstacle_y < 0 or obstacle_y >= len(grid[0]):
        return None
    if grid[obstacle_x][obstacle_y] == '#':
        return None
    
    # check if the obstacle makes a loop
    tmp_grid = copy.deepcopy(grid)
    tmp_grid[obstacle_x][obstacle_y] = '#'
    new_pos, new_orientation = move(tmp_grid, pos, orientation)
    
    if new_pos is not None and (new_pos, new_orientation) in seen_positions:
        return obstacle_x, obstacle_y

    return None

def main():
    with open('input.txt', 'r') as file:
        grid_0 = [list(line.strip()) for line in file.readlines()]

    with open('input.txt', 'r') as file:
        grid_1 = [list(line.strip()) for line in file.readlines()]

    with open('input.txt', 'r') as file:
        grid_2 = [list(line.strip()) for line in file.readlines()]


    pos0, orientation0 = get_starting_position(grid_0)
    pos, orientation = pos0, orientation0
    print('The robot starts at position ', pos, ' facing ', orientation)
    
    while True:
        grid_0[pos[0]][pos[1]] = 'X'
        pos, orientation = move(grid_0, pos, orientation)
        print('\n')
        if pos is None:
            break
        print_pos(grid_0, pos, orientation)

    for row in grid_0:
            print(''.join(row))

    count_pos = visited_positions(grid_0)

    pos, orientation = pos0, orientation0
    position = pos0, orientation0
    obstructions = []
    seen_positions = []
    seen_positions_orientations = []
    prev_pos = None
    while True:
        # if pos in seen_positions:
        obstacle = get_obstacle(pos, orientation, grid_1, seen_positions_orientations)
        if obstacle not in obstructions and obstacle is not None:
            seen_positions = []
            seen_positions_orientations = []
            obstructions.append(obstacle)
            print('\n')
            grid_1[obstacle[0]][obstacle[1]] = 'O'
            for row in grid_1:
                print(''.join(row))
            pos, orientation = pos0, orientation0
            grid_1 = copy.deepcopy(grid_2)
        if pos == prev_pos:
            grid_1[pos[0]][pos[1]] = '+'
        elif orientation == 'north' or orientation == 'south':
            grid_1[pos[0]][pos[1]] = '|'
        elif orientation == 'east' or orientation == 'west':
            grid_1[pos[0]][pos[1]] = '-'
        seen_positions.append(pos)
        seen_positions_orientations.append(position)
        prev_pos = pos
        pos, orientation = move(grid_1, pos, orientation)
        if pos is None:
            break
        position = pos, orientation
    
    print('The robot visited ', count_pos, ' positions.')
    print('The robot found ', len(obstructions), ' obstructions.')
    print('The robot found the obstructions at positions ', obstructions)


if __name__ == '__main__':
    main()
