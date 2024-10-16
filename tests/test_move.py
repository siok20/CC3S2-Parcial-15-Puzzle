import pytest
from src.puzzle import puzzle

@pytest.fixture
def play():
    return puzzle()

@pytest.mark.parametrize("board, position, direction, expected_board, expected_position", [
    ([10, 13, 15, 12, 2, 1, 14, 0, 11, 3, 6, 9, 5, 7, 8, 4], 7, "up", [10, 13, 15, 0, 2, 1, 14, 12, 11, 3, 6, 9, 5, 7, 8, 4], 3),
    ([10, 13, 15, 12, 2, 1, 14, 0, 11, 3, 6, 9, 5, 7, 8, 4], 7, "down", [10, 13, 15, 12, 2, 1, 14, 9, 11, 3, 6, 0, 5, 7, 8, 4], 11),
    ([10, 13, 15, 12, 2, 1, 14, 0, 11, 3, 6, 9, 5, 7, 8, 4], 7, "left", [10, 13, 15, 12, 2, 1, 0, 14, 11, 3, 6, 9, 5, 7, 8, 4], 6),
    ([10, 13, 15, 12, 2, 1, 0, 14, 11, 3, 6, 9, 5, 7, 8, 4], 6, "right", [10, 13, 15, 12, 2, 1, 14, 0, 11, 3, 6, 9, 5, 7, 8, 4], 7),
    
])
def test_move(play, board, position, direction, expected_board, expected_position):
    play.set_board(board)
    play.position = position

    play.move(direction)

    assert play.get_board() == expected_board
    assert play.position == expected_position


@pytest.mark.parametrize("board, position", [
    ([1, 2, 4, 8, 9, 0, 3, 12, 7, 11, 14, 10, 5, 13, 6, 15], 5),
    ([3, 1, 6, 2, 5, 7, 15, 13, 4, 11, 8, 9, 14, 10, 12, 0], 15),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 13, 14, 15, 12], 11),
    
])
def test_solvable(play, board, position):
    assert play.is_solvable(board=board, position=position)