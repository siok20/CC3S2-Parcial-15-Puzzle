import random as rd

class puzzle:
    '''
    Clase que contiene la logica del juego
    y sus componentes internos
    '''
    def __init__(self):
        '''
        Constructor
        atributos: 
            * board: el array que contiene la posicion 
                     de los numeros del tablero, 
                     Numeros del 0 al 15 donde 0 es el elemento vacio

            * position: indice donde se encuentra el elemento vacio
        '''
        self.board, self.position = self.generate_board_position()
    

    def generate_board_position(self):
        '''
        Genera board y nos da la posicion del elemento vacio
        '''
        Fboard = [i for i in range(16)]
        board = []
        j = 0
        while Fboard != []:
            i = rd.choice(Fboard)

            if i == 0:
                position = j
            Fboard.remove(i)
            board.append(i)
            j += 1

        return board, position
    

        