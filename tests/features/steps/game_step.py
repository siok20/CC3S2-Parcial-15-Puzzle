from behave import given, when, then
from puzzle import puzzle

@given('que he generado un nuevo puzzle')
def step_new_game(context):
    puzzle()
    pass

