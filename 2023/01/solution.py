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

import re

def get_digits(str):
    # digits = re.findall(r'\d', str) # part 1
    digits = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', str) # part 2
    return digits

def digits_to_int(str):
    if str == 'one':
        return 1
    elif str == 'two':
        return 2
    elif str == 'three':
        return 3
    elif str == 'four':
        return 4
    elif str == 'five':
        return 5
    elif str == 'six':
        return 6
    elif str == 'seven':
        return 7
    elif str == 'eight':
        return 8
    elif str == 'nine':
        return 9
    else:
        return int(str)

file = open('input', 'r')

lines = file.readlines()

count = 0

for line in lines:
    digits = get_digits(line)
    count = digits_to_int(digits[0])*10 + digits_to_int(digits[-1]) + count

print('Solution ' + str(count))
