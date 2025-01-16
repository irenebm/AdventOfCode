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

def decreasing_order(list, differ=3, bad_level=0) -> bool:
    print(list)
    print('with bad level ' + str(bad_level))
    for i in range(len(list) - 1):
        if list[i] - list[i + 1] > differ:
            if bad_level == 1:
                print('returning false')
                return False
            bad_level = 1
            # remove this level
            cp_list1 = list.copy()
            cp_list1.pop(i+1)
            cp_list2 = list.copy()
            cp_list2.pop(i)
            return decreasing_order(cp_list1, differ, bad_level) or decreasing_order(cp_list2, differ, bad_level)
        if list[i] <= list[i + 1]:
            if bad_level == 1:
                print('returning false')
                return False
            bad_level = 1
            # remove this level
            cp_list1 = list.copy()
            cp_list1.pop(i+1)
            cp_list2 = list.copy()
            cp_list2.pop(i)
            return decreasing_order(cp_list1, differ, bad_level) or decreasing_order(cp_list2, differ, bad_level)
    print('---')
    print('decreasing')
    return True

def increasing_order(list, differ=3, bad_level=0) -> bool:
    print(list)
    print('with bad level ' + str(bad_level))
    for i in range(len(list) - 1):
        if list[i + 1] - list[i] > differ:
            print('bad')
            if bad_level == 1:
                print('returning false')
                return False
            bad_level = 1
            # remove this level
            # remove this level
            cp_list1 = list.copy()
            cp_list1.pop(i+1)
            cp_list2 = list.copy()
            cp_list2.pop(i)
            return increasing_order(cp_list1, differ, bad_level) or increasing_order(cp_list2, differ, bad_level)
        if list[i] >= list[i + 1]:
            print('bad')
            if bad_level == 1:
                print('returning false')
                return False
            bad_level = 1
            # remove this level
            # remove this level
            cp_list1 = list.copy()
            cp_list1.pop(i+1)
            cp_list2 = list.copy()
            cp_list2.pop(i)
            return increasing_order(cp_list1, differ, bad_level) or increasing_order(cp_list2, differ, bad_level)
    print('---')
    print('increasing')
    return True

def main():
    file = open('input.txt', 'r')

    lines = file.readlines()

    safe = 0
    for line in lines:
        ids_list = list(map(int, line.split(' ')))
        if decreasing_order(ids_list) or increasing_order(ids_list):
            safe += 1

    print('Safe ' + str(safe))


if __name__ == '__main__':
    main()