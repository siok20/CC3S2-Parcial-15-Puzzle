import pytest
from main import Puzzle_15

@pytest.fixture
def puzzle():
    return puzzle()

def test_estructura_del_puzzle(puzzle):
    # Verificar que el puzzle tenga una estructura de 4x4
    assert len(puzzle.board) == 4
    for row in puzzle.board:
        assert len(row) == 4