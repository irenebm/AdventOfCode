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

def main():
    file = open('input.txt', 'r')

    lines = file.readlines()

    ids_list_left= []
    ids_list_right = []
    for line in lines:
        id_left = int(line.split(' ')[0])
        id_right = int(line.split(' ')[-1])
        ids_list_left.append(id_left)
        ids_list_right.append(id_right)

    # Sort the lists
    ids_list_left.sort()
    ids_list_right.sort()

    distance = 0
    for i in range(len(ids_list_left)):
        distance += abs(ids_list_left[i] - ids_list_right[i])

    similarity_score = 0
    for i in range(len(ids_list_left)):
        # number of times the id appears in the right list
        similarity_score += ids_list_left[i] * ids_list_right.count(ids_list_left[i])

    print('Distance ' + str(distance))
    print('Similarity score ' + str(similarity_score))

if __name__ == '__main__':
    main()