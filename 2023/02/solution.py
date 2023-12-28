# Copyright 2023 Irene Bandera Moreno
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

file = open('input', 'r')

lines = file.readlines()

count = 0

n_red = 12
n_green = 13
n_blue = 14

for line in lines:
    balls = line.split(' ')
    id = balls[1][:-1]
    valid= True

    game = line[7+len(id):].split(';')

    red = 0
    green = 0
    blue = 0

    for i in game:
        values = i.split(' ')
        for i in range(len(values)):
            # Part A
            # if 'red' in values[i] and int(values[i-1]) > n_red:
            #     valid = False
            # if 'green' in values[i] and int(values[i-1]) > n_green:
            #     valid = False
            # if 'blue' in values[i] and int(values[i-1]) > n_blue:
            #     valid = False
            # Part B
            if 'red' in values[i] and int(values[i-1]) > red:
                red = int(values[i-1])
            if 'green' in values[i] and int(values[i-1]) > green:
                green = int(values[i-1])
            if 'blue' in values[i] and int(values[i-1]) > blue:
                blue = int(values[i-1])

    # Part A
    # if(valid):
    #     count += int(id)

    # Part B
    count = count + (red * blue * green)

print('Solution ' + str(count))
