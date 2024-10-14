import pytest
import puzzle

def test_puzzle_is_solved():
    puzzle = puzzle()

    puzzle.board= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

    assert puzzle.is_solved() == True




