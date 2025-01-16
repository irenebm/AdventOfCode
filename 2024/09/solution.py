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

def get_disk(line):
    free_space = {}
    blocks = {}
    id = 0
    i = 0
    for digit in line:
        # check if its a digit
        if not digit.isdigit():
            continue
        # odd 
        if i % 2 != 0:
            free_space[id] = int(digit)
            id += 1
            
        # even
        else:
            blocks[id] = int(digit)
        
        i += 1
    
    return(free_space, blocks)

def status_disk(free_space, blocks):
    disk = []
    for i in range(0, len(blocks)):
        for j in range(0, blocks[i]):
            disk.append(str(i))
        if i >= len(free_space):
            continue
        for j in range(0, free_space[i]):
            disk.append('.')
    
    return disk

def move_disk_p1(disk):
    for i in range(len(disk)):
        if disk[i] == '.':
            # Find the last non-'.' character
            j = len(disk) - 1
            while j > i and disk[j] == '.':
                j -= 1

            # If no non-'.' characters are found, return the current state
            if j == i:
                return disk

            # Replace the current '.' with the last non-'.' character
            disk[i] = disk[j]
            disk[j] = '.'  # Swap the position with a '.'

    return disk

def move_disk_p2(disk):

    pass

def filesystem_checksum(disk):
    checksum = 0
    index = 0
    for i in range(len(disk)):
        if disk[i] == '.':
            return checksum
        checksum += int(disk[i]) * index
        index += 1

    return checksum 

def main():
    with open('input.txt', 'r') as file:
        line = file.readline()

    
    free_space, blocks = get_disk(line)
    disk = status_disk(free_space, blocks)
    disk_p1 = move_disk_p1(disk)
    disk_p2 = move_disk_p2(disk)

    count_p1 = filesystem_checksum(disk_p1)
    count_p2 = filesystem_checksum(disk_p2)

    print(disk)
    print('Part 1:', count_p1)
    print('Part 2:', count_p2)

if __name__ == '__main__':
    main()
