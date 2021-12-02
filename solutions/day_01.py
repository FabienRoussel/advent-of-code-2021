import os
from common.files import read_lines, INPUTS_FOLDER
from common.timing import timer
from typing import List

#from functools import reduce
#from itertools import combinations
#from operator import mul


@timer
def count_number_of_increase(input_sequence: list[int]) -> int:
    init = input_sequence[0]
    acc = 0
    for val in input_sequence[1:]:
        if init < val:
            acc += 1
        init = val
    return acc

def create_a_sliding_list(input_sequence: list[int]):
    return [input_sequence[i] + input_sequence[i+1] + input_sequence[i+2] for i in range(len(input_sequence)-2)]

@timer
def count_number_of_increase_in_sliding_list(input_sequence: list[int]):
    sliding_list = create_a_sliding_list(input_sequence)
    return count_number_of_increase(sliding_list)

if __name__ == '__main__':
    input_file_path: str = os.path.join(INPUTS_FOLDER, 'day_01', 'input.txt')
    input_list: list[int] = read_lines(input_file_path=input_file_path, line_type=int)

    # Part 1
    part_1_result: int = count_number_of_increase(input_sequence=input_list)
    print('Part 1 result :', part_1_result)
    assert part_1_result == 1266

    # Part 2
    part_2_result: int = count_number_of_increase_in_sliding_list(input_sequence=input_list)
    print('Part 2 result :', part_2_result)
    assert part_2_result == 1217