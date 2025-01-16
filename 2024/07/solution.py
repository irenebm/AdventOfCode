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

def evaluate(solution, values, p2=False):
    result = []
    for i, value in enumerate(values):
        if result == []:
            operation = int(value)
            result.append(operation)
        else:
            for num in list(result):
                # Add the number with the value
                new_num = num + int(value)
                if new_num <= solution:
                    result.append(new_num)

                # Multiply the number with the value
                new_num = num * int(value)           
                if new_num <= solution:
                    result.append(new_num)

                if p2:
                    # Concatenate the number with the value -> 10 || 1 = 101 , 10 || 3 * 6 = 618
                    new_num = int(str(num) + value)
                    if new_num <= solution:
                        result.append(new_num)
                    
                result.remove(num)
    
    for num in result:
        if num == solution:
            return True

    return False


def main():
    with open('input.txt', 'r') as file:
        grid = [line.strip() for line in file.readlines()]

    count_p1 = 0
    count_p2 = 0
    for row in grid:
        solution, values = row.split(':')
        print('Evaluating: ' + solution + ' ' + values)
        if evaluate(int(solution), values.split()):
            count_p1 += int(solution) 
        if evaluate(int(solution), values.split(), True):
            count_p2 += int(solution) 

    print('count P1: ' + str(count_p1))
    print('count P2: ' + str(count_p2))

if __name__ == '__main__':
    main()
