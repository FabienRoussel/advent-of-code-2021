import os
from common.files import read_lines, INPUTS_FOLDER
from common.timing import timer


def compute_grids_and_header(input_list: list[int]) -> (list, list, list):
    header = input_list[0].split(',')
    nb_grid = len(input_list)//6
    bingo_grids = []
    for i in range(nb_grid):
        bingo_grids.append([row.split() for row in input_list[i*6+2:i*6+7]])
    find_grids = [[[False for col in range(5)] for row in range(10)] for n in range(len(bingo_grids))]

    grids = []
    for n in range(nb_grid):
        grids.append({})
        for row in range(5):
            for col in range(5):
                grids[n][bingo_grids[n][row][col]] = (row, col)
    return header, grids, find_grids


@timer
def start_bingo(header: list[int], grids: list[dict], find_grids: list[list[list[bool]]]) -> int:
    return play_bingo(header, grids, find_grids)

def play_bingo(header: list[int], grids: list[dict], find_grids: list[list[list[bool]]]) -> int:
    draw_number, *new_header = header
    find_grids = update_find_grids(draw_number, grids, find_grids)

    for n in range(len(find_grids)):
        if grid_has_won(find_grids[n]):
            return compute_winner_score(grids[n], find_grids[n], draw_number)
    return play_bingo(new_header, grids, find_grids)

def update_find_grids(draw_number, grids, find_grids):
    for n in range(len(grids)):
        grid = grids[n]
        if draw_number in grid:
            row, col = grid[draw_number]
            find_grids[n][row][col] = True
            find_grids[n][col+5][row] = True
    return find_grids

def grid_has_won(find_grid: list[list[bool]]):
    for row_or_col in find_grid:
        if False not in row_or_col:
            return True
    return False

def compute_winner_score(grid, find_grid, draw_number):
    inv_grid = {v: k for k, v in grid.items()}
    acc = 0
    for row in range(5):
        for col in range(5):
            if find_grid[row][col] == False:
                acc += int(inv_grid[(row, col)])
    return acc * int(draw_number)


@timer
def start_bingo_part_2(header: list[int], grids: list[dict], find_grids: list[list[list[bool]]]) -> int:
    winning_grids = loose_bingo(header, grids, find_grids, [[], []])
    return compute_winner_score(grids[winning_grids[0][-1]], find_grids[winning_grids[0][-1]], winning_grids[1][-1])

def loose_bingo(header: list[int], grids: list[dict], find_grids: list[list[list[bool]]], winning_grids:list):
    if len(header) and len(winning_grids[0]) < len(grids): 
        draw_number, *new_header = header
        find_grids = update_find_grids(draw_number, grids, find_grids)

        for n in range(len(find_grids)):
            if n not in winning_grids[0] and grid_has_won(find_grids[n]):
                winning_grids[0].append(n)
                winning_grids[1].append(draw_number)
        return loose_bingo(new_header, grids, find_grids, winning_grids)
    return winning_grids


if __name__ == '__main__':
    input_file_path: str = os.path.join(INPUTS_FOLDER, 'day_04', 'input.txt')
    input_list: list[str] = read_lines(input_file_path=input_file_path, line_type=str)
    header, grids, find_grids = compute_grids_and_header(input_list)

    # Part 1
    part_1_result: int = start_bingo(header=header[:], grids=grids[:], find_grids=find_grids[:])
    print('Part 1 result :', part_1_result)
    assert part_1_result == 10374

    # Part 2
    part_2_result: int = start_bingo_part_2(header=header[:], grids=grids[:], find_grids=find_grids[:])
    print('Part 2 result :', part_2_result)
    assert part_2_result == 24742