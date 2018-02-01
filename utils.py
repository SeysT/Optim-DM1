"""
Author: Thibaut Seys
Last modified: 01/02/2018

Summary:
This file defines all functions needed to modelize crosswords problem.
"""


def parse_grid(grid):
    """
    This function returns all segments and cases from a given grid.
    + params:
        - grid: the grid to parse. Expected input: ['###...##', ...]
    + return:
        - segments: a list of list containing coordinates tuples for one segment to complete:
            [[(x, y), ...], ...]
        - cases: a list of coordinates tuples for cases to complete:
            [(x, y)]
    """
    height = len(grid)
    width = len(grid[0])

    segments = []
    cases = []
    current_row_segment = []
    current_column_segment = []

    i = 0
    while i < width:
        j = 0
        while j < height:
            if grid[i][j] == '#':
                if len(current_row_segment) > 1:
                    segments.append(current_row_segment)
                current_row_segment = []
            else:
                cases.append((i, j))
                current_row_segment.append((i, j))

            if grid[j][i] == '#':
                if len(current_column_segment) > 1:
                    segments.append(current_column_segment)
                current_column_segment = []
            else:
                current_column_segment.append((j, i))

            j += 1
        i += 1
    return segments, cases


def load_data_from_files(grid_filename, word_filename):
    """
    This function returns all data that could be extracted from files.
    + params:
        - grid_filename: the filename of the grid to parse
        - word_filename: the filename of the vocabulary to use
    + return:
        - grid: the grid model represented as a list on line:
            ['#####..####', ...]
        - words: a dict representing of vocabulary. The keys are the length ofthe value words:
            {len_worlds: [word, ...]}
        - alphabet: a set representing the possible symbol encounter in word file.
    """
    with open(grid_filename, 'r') as grid_file:
        grid = grid_file.read().strip().split('\n')

    with open(word_filename, 'r') as word_file:
        word_list = word_file.read().strip().split('\n')

    words = {}
    alphabet = set()
    for word in word_list:
        try:
            words[len(word)].append(word)
        except KeyError:
            words[len(word)] = [word]
        alphabet |= set(word)

    return grid, words, alphabet


def pretty_print(grid, sol):
    """
    Tis function print the solved grid. It needs as inputs the grid model and the found solution.
    """
    grid = [list(elt) for elt in grid]
    for key, value in sol.items():
        if key[0] == 'c':
            x, y = key[1]
            grid[x][y] = value
    grid = [' '.join(elt) for elt in grid]
    print('\n'.join(grid))
