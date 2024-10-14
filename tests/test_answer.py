import pytest
from src.puzzle import puzzle

@pytest.fixture
def play():
    return puzzle()

@pytest.mark.parametrize("board, position, direction", [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 13, 14, 15, 12], 11,  "down"),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15], 14, "right"),
    
])
def test_move(play, board, position, direction):
    play.set_board(board)
    play.position = position

    play.move(direction)

    assert play.is_solved() == True


