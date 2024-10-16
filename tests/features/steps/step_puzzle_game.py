from behave import given, when, then
from src.puzzle import puzzle

# inicia el juego con la casilla vacía en una posición específica
@given('el juego tiene una casilla vacía en la posición {position}')
def step_given_juego_con_casilla_vacia(context, position):
    context.game = puzzle()
    position = int(position)
    
    tablero = [i for i in range(1, 16)] #crea una lista de numeros del 1 al 15
    tablero.insert(position, 0) #inserta el 0 en la posicion que se especifica

    context.game.set_board(tablero) #se asigna el tablero generado al juegp
    context.game.position = position  #se establece la posición de la casilla vacía

@when('presiono la tecla de flecha arriba')
def step_when_mover_arriba(context):
    context.result = context.game.move("up")

@then('la casilla vacía se debería mover a la posición {new_position}')
def step_then_casilla_vacia_posicion(context, new_position):
    new_position = int(new_position)    
    assert context.game.position == new_position, f"La posición esperada era {new_position} pero resultó {context.game.position}"

#-----------------------------------------------------------------------------------------------------------------------------------
@when('presiono la tecla de flecha izquierda')
def step_when_mover_izquierda(context):
    context.result = context.game.move("left")

#-----------------------------------------------------------------------------------------------------------------------------------
@when('presiono la tecla de flecha abajo')
def step_when_mover_abajo(context):
    context.result = context.game.move("down")

#verifica que el movimiento sea inválido
@then('el movimiento debería ser inválido')
def step_then_movimiento_invalido(context):
    assert context.result == False, "El movimiento debería ser inválido"

@then('la casilla vacía debería permanecer en la posición {position}')
def step_then_casilla_vacia_posicion(context, position):
    position = int(position)
    assert context.game.position == position, f"La posición esperada era {position} pero resultó {context.game.position}"

#-----------------------------------------------------------------------------------------------------------------------------------
@given('el puzzle está resuelto')
def step_given_puzzle_resuelto(context):
    context.game = puzzle()
    tablero_resuelto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    context.game.set_board(tablero_resuelto)
    context.game.position = 15      #establece la posición de la casilla vacía
    
     #asegura que el tablero está en el estado resuelto
    assert context.game.get_board() == tablero_resuelto
    assert context.game.position == 15, "La posición del elemento vacío debería ser 15"     

@when('verifico si el puzzle está resuelto')
def step_when_verificar_resuelto(context):
    context.result = context.game.is_solved()       #llama a la función para verificar si el puzzle está resuelto

@then('el resultado debería ser True')
def step_then_puzzle_resuelto(context):
    assert context.result == True, "El puzzle debería estar resuelto"       
