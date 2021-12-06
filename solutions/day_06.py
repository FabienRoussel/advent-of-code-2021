import os
from common.files import read_lines, INPUTS_FOLDER
from common.timing import timer
AGE_MAX: int = 8

@timer
def wait_x_days(fish, days):
    fish_ordered = [0] * (AGE_MAX+1)
    for age in fish:
        fish_ordered[age] += 1
    for i in range(days):
        fish_ordered = wait_1_day(fish_ordered)
    return sum(fish_ordered)

def wait_1_day(fish_ordered):
    new_fish_ordered = [0] * (AGE_MAX+1)
    new_fish_ordered[AGE_MAX], new_fish_ordered[6] = fish_ordered[0], fish_ordered[0]
    for i in range(8):
        new_fish_ordered[i] += fish_ordered[i+1]
    return new_fish_ordered

if __name__ == '__main__':
    input_file_path: str = os.path.join(INPUTS_FOLDER, 'day_06', 'input.txt')
    input_list: list[str] = read_lines(input_file_path=input_file_path, line_type=str)
    fish = [int(a_fish) for a_fish in ''.join(input_list).split(',')]

    # Part 1
    part_1_result: int = wait_x_days(fish=fish, days=80)
    print('Part 1 result :', part_1_result)
    assert part_1_result == 385391

    # Part 2
    part_2_result: int = wait_x_days(fish=fish, days=256)
    print('Part 2 result :', part_2_result)
    assert part_2_result == 1728611055389