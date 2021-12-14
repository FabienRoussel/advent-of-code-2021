import os
from common.files import read_lines, INPUTS_FOLDER
from common.timing import timer
from collections import Counter
import time


@timer
def paths_with_max_one_small_cave_visit(dict_cave_connections: dict):
    paths = [['start']]
    paths_with_end = []
    while(len(paths)):
        len_paths = len(paths)
        for i in range(len_paths):
            path = paths.pop(0)
            last_cave = path[-1]
            if last_cave != 'end':
                for cave_connected in dict_cave_connections[last_cave]:
                    new_path = [*path, cave_connected]
                    if cave_connected == 'end':
                        if path not in paths_with_end:
                            paths_with_end.append(new_path)
                    elif new_path not in paths and cave_connected != 'start' and (not cave_connected.islower() or cave_connected not in path):
                        paths.append(new_path)
            else:
                paths.append(path)
    return len(paths_with_end)


def does_all_paths_end(paths):
    for path in paths:
        if path[-1] != 'end':
            return False
    return True


def build_dict(input_list: list[list[str]]) -> dict:
    dict_of_connection = {}
    for row in input_list:
        dict_of_connection[row[0]] = dict_of_connection.get(row[0], []) + [row[1]]
        dict_of_connection[row[1]] = dict_of_connection.get(row[1], []) + [row[0]]
    return dict_of_connection


@timer
def paths_with_max_two_small_cave_visits(dict_cave_connections: dict):
    paths = [['start']]
    paths_with_end = []
    while(len(paths)):
        len_paths = len(paths)
        for i in range(len_paths):
            path = paths.pop(0)
            last_cave = path[-1]
            if last_cave != 'end':
                for cave_connected in dict_cave_connections[last_cave]:
                    counter_cave = dict(Counter(path))
                    new_path = [*path, cave_connected]
                    if cave_connected == 'end':
                        if path not in paths_with_end:
                            paths_with_end.append(path)
                    elif cave_connected != 'start' and new_path not in paths and (not cave_connected.islower() or is_only_one_small_caves_visited_twice(new_path)):
                        paths.append(new_path)
    return len(paths_with_end)


def is_only_one_small_caves_visited_twice(path):
    lower_path = [cave for cave in path if cave.islower()]
    counter_cave = dict(Counter(lower_path))
    is_small_cave_has_been_visited_twice = 0
    for item in counter_cave.values():
        if item > 1:
            is_small_cave_has_been_visited_twice += item - 1
        if is_small_cave_has_been_visited_twice > 1:
            return False
    return True


if __name__ == '__main__':
    input_file_path: str = os.path.join(INPUTS_FOLDER, 'day_12', 'input.txt')
    input_list: list[list[str]] = [ row.split('-') for row in read_lines(input_file_path=input_file_path, line_type=str)]
    dict_cave_connections = build_dict(input_list)

    # Part 1
    part_1_result: int = paths_with_max_one_small_cave_visit(dict_cave_connections=dict_cave_connections)
    print('Part 1 result :', part_1_result)
    #assert part_1_result == 4104

    # Part 2
    part_2_result: int = paths_with_max_two_small_cave_visits(dict_cave_connections=dict_cave_connections)
    print('Part 2 result :', part_2_result)
    #assert part_2_result == 119760
