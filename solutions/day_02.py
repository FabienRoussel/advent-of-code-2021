import os
from common.files import read_lines, INPUTS_FOLDER
from common.timing import timer
from typing import List


@timer
def compute_position(input_sequence: list[int], increase_position_method) -> int:
    depth = 0
    horizontal_position = 0
    aim = 0
    for val in input_sequence:
        depth, horizontal_position, aim = increase_position_method(val, depth, horizontal_position, aim)
    return depth*horizontal_position

def increase_position(action, depth, horizontal_position, aim) -> (int, int, int):
    direction = action[0]
    step = int(action[1])
    if direction == 'forward':
        return depth, horizontal_position + step, aim
    elif direction == 'down':
        return depth + step, horizontal_position, aim
    elif direction == 'up':
        return depth - step, horizontal_position, aim 
    else: 
        return depth, horizontal_position, aim

def increase_position_and_aim(action, depth, horizontal_position, aim) -> (int, int, int):
    direction = action[0]
    step = int(action[1])
    if direction == 'forward':
        return depth + step * aim, horizontal_position + step, aim
    elif direction == 'down':
        return depth, horizontal_position, aim + step
    elif direction == 'up':
        return depth, horizontal_position, aim - step
    else: 
        return depth, horizontal_position, aim

if __name__ == '__main__':
    input_file_path: str = os.path.join(INPUTS_FOLDER, 'day_02', 'input.txt')
    input_list: list[int] = read_lines(input_file_path=input_file_path, line_type=str)
    input_list = [ x.split(' ') for x in input_list]

    # Part 1
    part_1_result: int = compute_position(input_sequence=input_list, increase_position_method=increase_position)
    print('Part 1 result :', part_1_result)
    #assert part_1_result == 150

    # Part 2
    part_2_result: int = compute_position(input_sequence=input_list, increase_position_method=increase_position_and_aim)
    print('Part 2 result :', part_2_result)
    #assert part_2_result == 1217