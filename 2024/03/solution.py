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

import re

def get_instructions(line):
    # get the instructions that are mul(num,num)
    print(line)
    # get the instructions
    # regexp = r'mul\((\d+),(\d+)\)'    # part 1
    regexp = r"mul\(\d+,\d+\)|do\(\)|don't\(\)" # part 2

    instructions = re.findall(regexp, line)
    return instructions

def main():
    file = open('input.txt', 'r')

    lines = file.readlines()

    enabled = True
    sum = 0
    for line in lines:
        instructions = get_instructions(line)
        for instruction in instructions:
            if instruction == "do()":
                enabled = True
            elif instruction == "don't()":
                enabled = False
            else:
                if enabled:
                    # get nums of mul(num,num)
                    nums = re.match(r"mul\((\d+),(\d+)\)", instruction)
                    sum += int(nums.group(1)) * int(nums.group(2))
            
    print('The sum of the numbers is: ' + str(sum))

if __name__ == '__main__':
    main()