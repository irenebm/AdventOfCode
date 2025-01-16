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

def count_word(grid, word, start, delta):
    """
    Count occurrences of a word in the grid starting from a point and moving in a specific direction.
    :param grid: 2D list of characters representing the grid.
    :param word: String to search for in the grid.
    :param start: Tuple (row, col) indicating the starting point.
    :param delta: Tuple (row_delta, col_delta) indicating direction of search.
    :return: Count of occurrences found in the grid in this direction.
    """
    row, col = start
    row_delta, col_delta = delta
    for k in range(len(word)):
        r, c = row + k * row_delta, col + k * col_delta
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != word[k]:
            return 0
    return 1

def find_word(grid, word):
    """
    Find occurrences of a word in all directions in the grid.
    :param grid: 2D list of characters.
    :param word: Word to search for.
    :return: Total number of occurrences.
    """
    # Part 1
    directions = [
        (0, 1), (0, -1),  # Horizontal right, left
        (1, 0), (-1, 0),  # Vertical down, up
        (1, 1), (-1, -1), # Diagonal \ down, up
        (1, -1), (-1, 1)  # Diagonal / down, up
    ]
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for direction in directions:
                count += count_word(grid, word, (i, j), direction)

    # Part 2
    directions = [
        (1, 1), (-1, -1), # Diagonal \ down, up
        (1, -1), (-1, 1)  # Diagonal / down, up
    ]
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'A':
                if ((count_word(grid, word, (i-1, j-1), (1, 1)) or count_word(grid, word, (i+1, j+1), (-1, -1))) and
                    (count_word(grid, word, (i-1, j+1), (1, -1)) or count_word(grid, word, (i+1, j-1), (-1, 1)))):
                    count += 1
    return count

def main():
    with open('input.txt', 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    
    # Part 1
    word = 'XMAS'
    # Part 2
    word = 'MAS'
    count = find_word(grid, word)
    print(f'The word {word} appears {count} times in the grid.')

if __name__ == '__main__':
    main()
