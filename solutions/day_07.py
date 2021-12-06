import os
from common.files import read_lines, INPUTS_FOLDER
from common.timing import timer


@timer
def do_smth(input_list: list[int]) -> int:
    return 0


if __name__ == '__main__':
    input_file_path: str = os.path.join(INPUTS_FOLDER, 'day_07', 'input.txt')
    input_list: list[str] = read_lines(input_file_path=input_file_path, line_type=str)

    # Part 1
    part_1_result: int = do_smth(input_list=input_list)
    print('Part 1 result :', part_1_result)
    assert part_1_result == 0

    # Part 2
    part_2_result: int = do_smth(input_list=input_list)
    print('Part 2 result :', part_2_result)
    assert part_2_result == 0