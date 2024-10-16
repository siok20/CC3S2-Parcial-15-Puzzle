from src.puzzle import puzzle

def test_invalid_move_does_not_increment_counter():

    game = puzzle()

    new_board = [0, 1, 2, 8,
                 4, 7, 6, 5,
                 3, 9, 11, 15,
                 12, 13, 10, 14]
    game.set_board(new_board)
    game.position = 0 

    assert game.cont_move == 0

    assert game.move('up') == False

    assert game.cont_move==0 #debería seguir en cero ya que no es un movimiento valido por la posicion del tablero

    game.move('down')
    assert game.cont_move==1 #Ahora debería incrementar porque es movimiento válido

    assert game.move('left') == False
    assert game.cont_move==1 #Debería estar en 1 porque no puede ir a la izquierda

    game.move('right')
    assert game.cont_move==2 #Debería estar en dos ya que se puede mover a la derecha

