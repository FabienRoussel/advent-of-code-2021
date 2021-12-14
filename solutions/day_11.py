import os
from common.files import read_lines, INPUTS_FOLDER
from common.timing import timer


@timer
def compute_number_of_flash(octopuses: list[list[int]], iter=1):
    print_octopuses(octopuses)
    n_rows = len(octopuses)
    n_cols = len(octopuses[0])
    count_flash = 0
    for it in range (iter):
        count_flash += one_iteration_of_flash(octopuses, n_rows, n_cols)
    return count_flash

def one_iteration_of_flash(octopuses, n_rows: int, n_cols: int)->int:
    octopus_having_flash = set()
    queue_flashing = []
    count_flash = 0
    for row in range(n_rows):
        for col in range(n_cols):
            octopuses[row][col] += 1
            if octopuses[row][col] > 9:
                queue_flashing.append((row, col))
    while len(queue_flashing):
        r, c = queue_flashing.pop(0)
        if (r,c) not in octopus_having_flash:
            count_flash += 1
            octopus_having_flash.add((r, c))
            queue_flashing.extend(update_octopuses_after_flash(octopuses, r, c, octopus_having_flash))
    return count_flash

def update_octopuses_after_flash(octopuses, r: int, c: int, octopus_having_flash):
    n_rows = len(octopuses)
    n_cols = len(octopuses[0])
    octopuses_to_queued = []
    for row in range(max(r-1,0), min(r+2, n_rows)):
        for col in range(max(c-1, 0), min(c+2, n_cols)):
            if row == r and col == c:
                octopuses[row][col] = 0
            if octopuses[row][col] != 0:
                octopuses[row][col] += 1
                if octopuses[row][col] > 9 and (row, col) not in octopus_having_flash:
                    octopuses_to_queued.append((row, col))
    return octopuses_to_queued


def print_octopuses(octopuses: list[list[int]]):
    for row in octopuses:
        print(''.join([str(col) for col in row]))
    print()


def wait_all_octopuses_flashed(octopuses: list[list[int]], iter=1):
    n_rows = len(octopuses)
    n_cols = len(octopuses[0])
    iter = 0
    while sum([ sum(row) for row in octopuses]):
        iter +=1
        one_iteration_of_flash(octopuses, n_rows, n_cols)
    return iter


if __name__ == '__main__':
    input_file_path: str = os.path.join(INPUTS_FOLDER, 'day_11', 'input.txt')
    input_list: list[list[int]] = [ [ int(power) for power in row] for row in read_lines(input_file_path=input_file_path, line_type=str)]

    # Part 1
    part_1_result: int = compute_number_of_flash(octopuses=[row[:] for row in input_list], iter=100)
    print('Part 1 result :', part_1_result)
    assert part_1_result == 1603

    # Part 2
    part_2_result: int = wait_all_octopuses_flashed(octopuses=[row[:] for row in input_list])
    print('Part 2 result :', part_2_result)
    assert part_2_result == 222