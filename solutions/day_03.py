import os
from common.files import read_lines, INPUTS_FOLDER
from common.timing import timer
from typing import List
from collections import Counter


@timer
def compute_diagnostic(input_sequence: list) -> int:
    input_sequence_transposed = transpose_list(input_sequence)
    most_common_values = [ most_common(lst) for lst in input_sequence_transposed] 
    most_common_values_in_int = byte_to_int(most_common_values)

    least_common_values = [ least_common(lst) for lst in input_sequence_transposed] 
    least_common_values_in_int = byte_to_int(least_common_values)
    return most_common_values_in_int * least_common_values_in_int

def transpose_list(lst: list):
    return list(map(list, zip(*lst)))

def most_common(lst: list) -> int:
    max_count_value, min_count_value = get_max_min(lst)
    if max_count_value == min_count_value: 
        return 1
    else:
        return max_count_value

def least_common(lst: list) -> int:
    max_count_value, min_count_value = get_max_min(lst)
    if max_count_value == min_count_value: 
        return 0
    else:
        return min_count_value

def get_max_min(lst: list) -> int:
    dict_of_count_values = dict(Counter(lst))
    max_count_value = max(dict_of_count_values, key=dict_of_count_values.get)
    min_count_value = min(dict_of_count_values, key=dict_of_count_values.get)
    return max_count_value, min_count_value

def byte_to_int(values: list[int]) -> int:
    return int("".join(str(x) for x in values), 2)


@timer
def get_life_support_ratings(input_sequence: list) -> int:

    oxygen_generator_rating = byte_to_int(get_rating(input_sequence, most_common))

    co2_scrubber_rating = byte_to_int(get_rating(input_sequence, least_common))
    
    return oxygen_generator_rating*co2_scrubber_rating

def get_rating(input_sequence: list, most_or_least_common_method, index: int = 0) ->int:
    input_sequence_transposed = transpose_list(input_sequence)
    if len(input_sequence)==1:
        return input_sequence[0]
    most_or_least_common_value = most_or_least_common_method(input_sequence_transposed[index])
    new_input_sequence = filter_list_by_value_at_index(input_sequence, most_or_least_common_value, index)
    return get_rating(new_input_sequence, most_or_least_common_method, index+1)

def filter_list_by_value_at_index(lst: list, value: int, index: int) -> list:
    return [ el for el in lst if el[index] == value ]


if __name__ == '__main__':
    input_file_path: str = os.path.join(INPUTS_FOLDER, 'day_03', 'input.txt')
    input_list: list[int] = read_lines(input_file_path=input_file_path, line_type=str)
    input_list = [ [int(bit) for bit in byte] for byte in input_list]

    # Part 1
    part_1_result: int = compute_diagnostic(input_sequence=input_list)
    print('Part 1 result :', part_1_result)
    assert part_1_result == 1131506

    # Part 2
    part_2_result: int = get_life_support_ratings(input_sequence=input_list)
    print('Part 2 result :', part_2_result)
    assert part_2_result == 7863147
