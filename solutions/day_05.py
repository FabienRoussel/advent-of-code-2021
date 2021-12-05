import os
from common.files import read_lines, INPUTS_FOLDER
from common.timing import timer


@timer
def count_overlapping_hydrothermal_vents(coordinates: list[tuple[tuple[int]]], with_diagonal: bool = False) -> int:
    grid = dict()
    for coords in coordinates:
        grid = draw_line(coords, grid, with_diagonal)
    return count_coords_with_overalapping_lines(grid)

def draw_line(coords:tuple[tuple[int]], grid: dict, with_diagonal: bool = False) -> dict:
    start, end = coords
    x0, y0 = start
    x1, y1 = end
    dx = x1 - x0
    dy = y1 - y0
    if with_diagonal==False and dx != 0 and dy != 0:
        return grid

    l = max(abs(dx), abs(dy))
    is_x_forward = (1 if dx > 0 else -1) if dx != 0 else 0
    is_y_forward = (1 if dy > 0 else -1) if dy != 0 else 0
    for i in range(l+1):
        x = x0 + i * is_x_forward 
        y = y0 + i * is_y_forward 
        grid[(x, y)] = grid[(x, y)] + 1 if (x, y) in grid else 1
    return grid

def count_coords_with_overalapping_lines(grid: dict):
    return len([val for val in grid if grid[val]>1])

if __name__ == '__main__':
    input_file_path: str = os.path.join(INPUTS_FOLDER, 'day_05', 'input.txt')
    input_list: list[str] = read_lines(input_file_path=input_file_path, line_type=str)
    lines = [el.split(' -> ') for el in input_list]
    coordinates = [tuple([tuple([int(coord) for coord in coords.split(',')]) for coords in line]) for line in lines]

    # Part 1
    part_1_result: int = count_overlapping_hydrothermal_vents(coordinates=coordinates)
    print('Part 1 result :', part_1_result)
    assert part_1_result == 5373

    # Part 2
    part_2_result: int = count_overlapping_hydrothermal_vents(coordinates=coordinates, with_diagonal=True)
    print('Part 2 result :', part_2_result)
    assert part_2_result == 21514