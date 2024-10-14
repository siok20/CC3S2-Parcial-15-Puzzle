import pytest
from src.puzzle import puzzle

@pytest.fixture
def play():
    return puzzle()

@pytest.mark.parametrize("board, position, direction, expected_board, expected_position", [
    ([10, 13, 15, 12, 2, 1, 14, 0, 11, 3, 6, 9, 5, 7, 8, 4], 7, "up", [10, 13, 15, 0, 2, 1, 14, 12, 11, 3, 6, 9, 5, 7, 8, 4], 3),
    
])
def test_move(play, board, position, direction, expected_board, expected_position):
    play.set_board(board)
    play.position = position

    play.move(direction)

    assert play.get_board() == expected_board
    assert play.position == expected_position
