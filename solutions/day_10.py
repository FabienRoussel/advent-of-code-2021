import os
from common.files import read_lines, INPUTS_FOLDER
from common.timing import timer
from queue import LifoQueue

@timer
def count_corrupted_score(input_list):
    return sum([get_points_from_illegal_char(response) for response in [is_chunk_legal(chunk) for chunk in input_list] if response in [')', ']', '}', '>']])

def is_chunk_legal(chunk: str):
    lifo = LifoQueue()
    for char in chunk:
        if char in ['(', '[', '{', '<']:
            lifo.put(char)
        else:
            lifo_char = lifo.get()
            if lifo_char == '(' and not(char == ')') or lifo_char == '[' and not(char == ']') or lifo_char == '{' and not(char == '}') or lifo_char == '<' and not(char == '>'):
                return char

    if lifo.empty():
        return 'Complete'
    else:
        return ('Incomplete', lifo)

def get_points_from_illegal_char(char) -> int:
    if char == ')':
        return 3
    if char == ']':
        return 57
    if char == '}':
        return 1197
    if char == '>':
        return 25137


@timer
def get_middle_score(input_list):
    incomplete_rows = [ line[1] for line in [is_chunk_legal(chunk) for chunk in input_list] if line[0] == 'Incomplete']
    scores = sorted([ commpute_score_for_imcomplete_row(lifo_of_missing_chars) for lifo_of_missing_chars in incomplete_rows ])
    length_scores = len(scores)
    return scores[length_scores//2]


def get_points_from_missing_char(char) -> int:
    if char == '(':
        return 1
    if char == '[':
        return 2
    if char == '{':
        return 3
    if char == '<':
        return 4


def commpute_score_for_imcomplete_row(lifo: LifoQueue) -> int:
    n = lifo.qsize()
    acc = 0
    for i in range(n):
        char = lifo.get()
        acc = acc * 5 + get_points_from_missing_char(char)
    return acc


if __name__ == '__main__':
    input_file_path: str = os.path.join(INPUTS_FOLDER, 'day_10', 'input.txt')
    input_list: list[str] = read_lines(input_file_path=input_file_path, line_type=str)

    # Part 1
    part_1_result: int = count_corrupted_score(input_list=input_list)
    print('Part 1 result :', part_1_result)
    assert part_1_result == 166191

    # Part 2
    part_2_result: int = get_middle_score(input_list=input_list)
    print('Part 2 result :', part_2_result)
    assert part_2_result == 1152088313
