import os
from common.files import read_lines, INPUTS_FOLDER
from common.timing import timer
import statistics


@timer
def count_simple_1_4_7_8_digits(input_list: list[tuple[list[str], list[str]]]):
    return len( [ digit for item in input_list for digit in item[1] if len(digit) in (2,3,4,7) ] )


@timer
def sum_output_values(input_list):
    output_values: list[int] = []
    for row in input_list:
        encoded_digits, encoded_outputs = row[0], row[1]
        simple_digits = [ orders_letters(digit) for digit in encoded_digits if len(digit) in (2,3,4,7) ]
        complex_digits = [ orders_letters(digit) for digit in encoded_digits if len(digit) in (5,6) ]
        encoded_outputs = [ orders_letters(digit) for digit in encoded_outputs]

        letters_to_digit_dict, digit_to_letters_dict = map_easy_digits(simple_digits)

        letters_to_digit_dict = map_complex_digits(complex_digits, letters_to_digit_dict, digit_to_letters_dict)

        output_values.append(int(''.join([ str(letters_to_digit_dict[encoded_digit]) for encoded_digit in encoded_outputs ])))
    return sum(output_values)


def map_easy_digits(simple_digits: list[str]):
    letters_to_digit_dict = {}
    digit_to_letters_dict = {}
    for simple_digit in simple_digits:
        length_simple_digit = len(simple_digit)
        if length_simple_digit == 2:
            letters_to_digit_dict[simple_digit] = 1
            digit_to_letters_dict[1] = simple_digit
        elif length_simple_digit == 3:
            letters_to_digit_dict[simple_digit] = 7
            digit_to_letters_dict[7] = simple_digit
        elif length_simple_digit == 4:
            letters_to_digit_dict[simple_digit] = 4
            digit_to_letters_dict[4] = simple_digit
        elif length_simple_digit == 7:
            letters_to_digit_dict[simple_digit] = 8
            digit_to_letters_dict[8] = simple_digit

    return letters_to_digit_dict, digit_to_letters_dict

def map_complex_digits(complex_digits: list[str], letters_to_digit_dict: dict, digit_to_letters_dict: dict):
    for complex_digit in complex_digits:
        if len(complex_digit) == 6:
            if len(set(complex_digit).intersection(set(digit_to_letters_dict[4]))) == 4:
                letters_to_digit_dict[complex_digit] = 9
            elif len(set(complex_digit).intersection(set(digit_to_letters_dict[7]))) == 3:
                letters_to_digit_dict[complex_digit] = 0
            else: 
                letters_to_digit_dict[complex_digit] = 6  
        else :
            if len(set(complex_digit).intersection(set(digit_to_letters_dict[1]))) == 2:
                letters_to_digit_dict[complex_digit] = 3
            elif len(set(complex_digit).intersection(set(digit_to_letters_dict[4]))) == 3:
                letters_to_digit_dict[complex_digit] = 5
            else: 
                letters_to_digit_dict[complex_digit] = 2  
    return letters_to_digit_dict

def orders_letters(letters: str) -> str:
    return ''.join(sorted(letters))


if __name__ == '__main__':
    input_file_path: str = os.path.join(INPUTS_FOLDER, 'day_08', 'input.txt')
    raw_input_list: list[str] = read_lines(input_file_path=input_file_path, line_type=str)
    input_list: list[tuple[list[str], list[str]]] = [[ item.split() for item in row.split(' | ') ] for row in raw_input_list ]

    # Part 1
    part_1_result: int = count_simple_1_4_7_8_digits(input_list=input_list)
    print('Part 1 result :', part_1_result)
    assert part_1_result == 303

    # Part 2
    part_2_result: int = sum_output_values(input_list=input_list)
    print('Part 2 result :', part_2_result)
    assert part_2_result == 961734