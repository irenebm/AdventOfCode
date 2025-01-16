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

def get_antennas(values):
    antennas = {}
    for i in range(len(values)):
        for j in range(len(values[i])):
            # check if is lowercase letter, uppercase letter, or digit
            if values[i][j].isalnum() or values[i][j].isalpha():
                if values[i][j] not in antennas:
                    antennas[values[i][j]] = []
                antennas[values[i][j]].append((i,j))
    return antennas

def get_antinodes(antennas, grid, p2=False):
    limit_x, limit_y = len(grid), len(grid[0])

    antinodes = []
    for antenna in antennas:
        positions = antennas[antenna]
        for i in range(len(positions)-1):
            for j in range(i+1, len(positions)):
                pos_1 = positions[i]
                pos_2 = positions[j]
                diff = ((pos_2[0] - pos_1[0]), (pos_2[1] - pos_1[1]))
                if p2:
                    for n in range(1, len(grid)):
                        antinodes_pos_1 = pos_1[0] + diff[0]*n, pos_1[1] + diff[1]*n
                        if 0 <= antinodes_pos_1[0] < limit_x and 0 <= antinodes_pos_1[1] < limit_y:
                            if antinodes_pos_1 not in antinodes:
                                antinodes.append(antinodes_pos_1)
                        antinodes_pos_2 = pos_2[0] - diff[0]*n, pos_2[1] - diff[1]*n
                        if 0 <= antinodes_pos_2[0] < limit_x and 0 <= antinodes_pos_2[1] < limit_y:
                            if antinodes_pos_2 not in antinodes:
                                antinodes.append(antinodes_pos_2)
                else:
                    antinodes_pos_1 = pos_1[0] - diff[0], pos_1[1] - diff[1]
                    if 0 <= antinodes_pos_1[0] < limit_x and 0 <= antinodes_pos_1[1] < limit_y:
                        if antinodes_pos_1 not in antinodes:
                            antinodes.append(antinodes_pos_1)
                    antinodes_pos_2 = pos_2[0] + diff[0], pos_2[1] + diff[1]
                    if 0 <= antinodes_pos_2[0] < limit_x and 0 <= antinodes_pos_2[1] < limit_y:
                        if antinodes_pos_2 not in antinodes:
                            antinodes.append(antinodes_pos_2)

    return antinodes

def main():
    with open('input.txt', 'r') as file:
        grid = [line.strip() for line in file.readlines()]

    antennas = get_antennas(grid)
    antinodes_p1 = get_antinodes(antennas, grid)
    antinodes_p2 = get_antinodes(antennas, grid, True)

    print('Part 1:', len(antinodes_p1))
    print('Part 2:', len(antinodes_p2))

if __name__ == '__main__':
    main()
