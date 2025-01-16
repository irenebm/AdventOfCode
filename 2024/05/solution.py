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


def get_info(grid):
    index = -1
    for i, row in enumerate(grid):
        if not '|' in row:
            index = i
            break

    return grid[:index], grid[index+1:] # Skip the empty line

def correctly_ordered(update, graph):
    for num in update:
        if not check_num(num, graph[num], update):
            return False
        
    return True

def check_num(num, neighbours, update):
    for neighbour in neighbours:
        if neighbour in update:
            if update.index(neighbour) < update.index(num):
                return False
    return True    

def get_graph(rules):
    graph = {}
    in_degree = {}

    for rule in rules:
        X, Y = rule.split('|')
        if X not in graph:
            graph[X] = []
        if Y not in graph:
            graph[Y] = []
        graph[X].append(Y)
        
        if Y not in in_degree:
            in_degree[Y] = 0
        in_degree[Y] = in_degree[Y] + 1
        if X not in in_degree:
            in_degree[X] = 0
        
    return graph, in_degree

def correct(update, graph):
    corrected_update = []   
    for num in update:
        if check_num(num, graph[num], update):
            corrected_update.append(num)
        else:
            index_neighbour = 100000000
            tmp = corrected_update
            for neighbour in graph[num]:
                if neighbour in corrected_update:
                    if corrected_update.index(neighbour) < index_neighbour:
                        index_neighbour = corrected_update.index(neighbour)
            corrected_update = tmp[:index_neighbour] + [num] + tmp[index_neighbour:]

    return corrected_update

def main():
    with open('input.txt', 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    
    rules, updates = get_info(grid)

    graph, _ = get_graph(rules)
    count_correctly = 0
    count_wrong = 0
    for update in updates:
        update_list = update.split(',')
        if correctly_ordered(update_list, graph):
            middle_number = update_list[len(update_list) // 2]
            count_correctly += int(middle_number)
        else:
            update_list = correct(update_list, graph)
            middle_number = update_list[len(update_list) // 2]
            count_wrong += int(middle_number)
        print('Update:', update, ' checked.')

    print('Correct:', count_correctly)
    print('Wrong:', count_wrong)

if __name__ == '__main__':
    main()
