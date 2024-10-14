from behave import given, when, then
from puzzle import puzzle

@given('que he generado un nuevo puzzle')
def step_new_game(context):
    puzzle()
    pass

@then('el puzzle debería ser un tablero de 4x4')
def step_show_board(context):
    assert len(context)