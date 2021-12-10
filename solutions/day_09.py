import os
from common.files import read_lines, INPUTS_FOLDER
from common.timing import timer
import numpy as np


@timer
def sum_risk_level_for_lowest_point(heightmap: list[list[int]]) -> int:
    lowest_points = get_lowest_points(heightmap)
    return sum([point+1 for point in lowest_points])


def get_lowest_points(heightmap: list[list[int]]) -> list:
    nb_rows = len(heightmap)
    nb_cols = len(heightmap[0])
    lowest_points = []
    for row in range(nb_rows):
        for col in range(nb_cols):
            point = heightmap[row][col]
            neighbors = []
            if row > 0:
                neighbors.append(heightmap[row-1][col])
            if row + 1 < nb_rows:
                neighbors.append(heightmap[row+1][col])
            if col > 0:
                neighbors.append(heightmap[row][col-1])
            if col + 1 < nb_cols:
                neighbors.append(heightmap[row][col+1])
            if point < min(neighbors):
                lowest_points.append(point)
    return lowest_points


@timer
def multiply_three_largest_basins(heightmap: list[list[int]]) -> int:
    return np.prod(get_three_largest_basins(heightmap))


def get_three_largest_basins(heightmap: list[list[int]]) -> list:
    nb_rows = len(heightmap)
    nb_cols = len(heightmap[0])
    all_basins_size = []
    queue_current_basin = []
    seen_points = set()
    for row in range(nb_rows):
        for col in range(nb_cols):
            height = heightmap[row][col]

            if (row, col) not in seen_points and height != 9:
                seen_points.add((row, col))
                size_basin = 1
                queue_current_basin.extend(get_neigbors_below_9(heightmap, seen_points, row, col, nb_rows, nb_cols))

                while len(queue_current_basin):
                    r, c = queue_current_basin.pop(0)
                    size_basin += 1
                    queue_current_basin.extend(get_neigbors_below_9(heightmap, seen_points, r, c, nb_rows, nb_cols))
                all_basins_size.append(size_basin)

    return sorted(all_basins_size)[-3:]

def get_neigbors_below_9(heightmap, seen_points, point_row, point_col, nb_rows, nb_cols):
    neighbors = []
    if point_row > 0 and            (point_row-1, point_col) not in seen_points and heightmap[point_row-1][point_col] < 9:
        neighbors.append((point_row-1, point_col))
        seen_points.add((point_row-1, point_col))
    if point_row + 1 < nb_rows and  (point_row+1, point_col) not in seen_points and heightmap[point_row+1][point_col] < 9:
        neighbors.append((point_row+1, point_col))
        seen_points.add((point_row+1, point_col))
    if point_col > 0 and            (point_row, point_col-1) not in seen_points and heightmap[point_row][point_col-1] < 9:
        neighbors.append((point_row, point_col-1))
        seen_points.add((point_row, point_col-1))
    if point_col + 1 < nb_cols and  (point_row, point_col+1) not in seen_points and heightmap[point_row][point_col+1] < 9:
        neighbors.append((point_row, point_col+1))
        seen_points.add((point_row, point_col+1))
    return neighbors


if __name__ == '__main__':
    input_file_path: str = os.path.join(INPUTS_FOLDER, 'day_09', 'input.txt')
    input_list: list[int] = read_lines(input_file_path=input_file_path, line_type=str)
    input_list = [[int(val) for val in item] for item in input_list]

    # Part 1
    part_1_result: int = sum_risk_level_for_lowest_point(heightmap=input_list)
    print('Part 1 result :', part_1_result)
    assert part_1_result == 468

    # Part 2
    part_2_result: int = multiply_three_largest_basins(heightmap=input_list)
    print('Part 2 result :', part_2_result)
    assert part_2_result == 1280496