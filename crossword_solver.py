"""
Author: Thibaut Seys
Last modified: 01/02/2018

This file modelize and solve our crosswords problem.

Usages:
    crossword_solver.py <crossword_filename> <words_filename> [<maintain_arc>]

Arguments:
    crossword_filename: [Mandatory] the path of the crossword grid file
    words_filename: [Mandatory] the path of the words file
    maintain_arc: [Optional] whatever you put here will maintain arc consistency

Model:
    + variables: We have to different types of variables:
        - the 'case' variables which correspond to cases to complete in the grid. Their domain is
        composed by letters of the alphabet problem.
        - the 'segment' variables which correspond to a segment to complete in the grid. Their
        domain is composed with words of the same length.
    + constraints: Our constraints link the two different types of variables. A 'case' variable
    has to have the same letter than the one of the word in the segment.
"""
from sys import argv
from time import time

from constraint_programming import constraint_programming
from utils import load_data_from_files, parse_grid, pretty_print


if __name__ == '__main__':
    print('Loading data from file...')
    grid, words, alphabet = load_data_from_files(argv[1], argv[2])

    print('Creating solveur and variables...')
    segments, cases = parse_grid(grid)
    var = {('s', tuple(segment)): set(words[len(segment)]) for segment in segments}
    var.update({('c', tuple(case)): set(alphabet) for case in cases})
    p = constraint_programming(var)
    if len(argv) > 3:
        p.maintain_arc_consistency()

    print('Adding constraints...')
    for case in cases:
        for segment in segments:
            try:
                index = segment.index(case)
            except ValueError:
                continue
            rel = set((word[index], word) for word in var[('s', tuple(segment))])
            p.addConstraint(('c', tuple(case)), ('s', tuple(segment)), rel)

    print('Solving...')
    start = time()
    sol = p.solve()
    duration = time() - start
    print('Solved in {} seconds'.format(duration))

    if sol:
        pretty_print(grid, sol)
    else:
        print('No solution')
