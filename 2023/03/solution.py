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
    digits = re.findall(r'\d+', str)
    return digits

def find_symbol(str, index0, index1, find_in_between):
    print("index 0: ")
    print(index0)
    print("index 1: ")
    print(index1)
    if (index0-1) >= 0:
        if not bool(re.match(r'\d|.', str[index0-1])):
            print("true1")
            return True
    if (index1+1) < len(str):
        if not bool(re.match(r'\d|.', str[index1+1])):
            print("true2")
            return True
    if find_in_between:
        for i in range(index0, index1):
            print(i)
            if not bool(re.match(r'\d|.', str[index0+i])):
                print("true3")
                return True
    print("false")
    return False

file = open('input', 'r')

lines = file.readlines()

count = 0

for i in range(len(lines)):
    digits = get_digits(lines[i])
    print("Line: " + lines[i])

    print("Digits: " + str(digits))

    for j in range(len(digits)):
        print("Digit: " + digits[j])
        index_0 = lines[i].index(digits[j])
        index_1 = lines[i].index(digits[j]) + len(digits[j])
        if find_symbol(lines[i], index_0, index_1, False):
            count += int(digits[j])
        elif (i - 1) >= 0:
            if find_symbol(lines[i-1], index_0, index_1, True):
                count += int(digits[j])
        elif (i + 1) < len(lines):
            print("next line")
            if find_symbol(lines[i+1], index_0, index_1, True):
                count += int(digits[j])

print('Solution ' + str(count))
