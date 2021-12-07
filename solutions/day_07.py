import os
from common.files import read_lines, INPUTS_FOLDER
from common.timing import timer
import statistics

@timer
def count_minimum_fuel_consumption(crabs, summing_method):
    minimal_fuel_consumption = 1e15
    std = statistics.stdev(crabs)
    mean = average(crabs)
    min_list = int(max(min(crabs), mean-std))
    max_list = int(min(max(crabs), mean+std))

    for potential_best_pos in range(min_list, max_list+1):
        aritmetic_sum = 0
        for crabs_pos in crabs:
            step = abs(crabs_pos-potential_best_pos)
            aritmetic_sum += summing_method(n=step)
        if aritmetic_sum < minimal_fuel_consumption:
            minimal_fuel_consumption = aritmetic_sum
    return int(minimal_fuel_consumption)

def arithmetic_sum_with_un_equal_to_n(n):
    u0 = 1
    un = n 
    return n * (un + u0) / 2

def simple_1_sum(n):
    return n

def average(lst):
    return sum(lst) / len(lst)

if __name__ == '__main__':
    input_file_path: str = os.path.join(INPUTS_FOLDER, 'day_07', 'input.txt')
    input_list: list[int] = [int(v) for v in read_lines(input_file_path=input_file_path, line_type=str)[0].split(',')]

    # Part 1
    part_1_result: int = count_minimum_fuel_consumption(crabs=input_list, summing_method=simple_1_sum)
    print('Part 1 result :', part_1_result)
    assert part_1_result == 348996

    # Part 2
    part_2_result: int = count_minimum_fuel_consumption(crabs=input_list, summing_method=arithmetic_sum_with_un_equal_to_n)
    print('Part 2 result :', part_2_result)
    assert part_2_result == 98231647