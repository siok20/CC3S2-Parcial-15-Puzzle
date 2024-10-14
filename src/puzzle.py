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
    
    def set_board(self, new_board):
        self.board = new_board

    def get_board(self):
        return self.board

    def move(self, direction):
        '''
        Logica de movimiento
        obtiene una direccion y el juego cambia las posiciones
        del elemento vacio y hacia donde se dirige

        En caso de movimiento valido intercambia las posiciones 
        en board
        '''
        row = self.position // 4
        col = self.position % 4
        self.cont_move = 0

        if direction == 'up':
            if row == 0: 
                print("Movimiento invalido")
                return

            self.board[self.position],self.board[self.position-4] = self.board[self.position-4],self.board[self.position] 
            self.position -=4

        elif direction == 'down':
            if row == 3: 
                print("Movimiento invalido")
                return
            
            self.board[self.position],self.board[self.position+4] = self.board[self.position+4],self.board[self.position] 
            self.position +=4

        elif direction =='left':
            if col == 0:
                print("Movimiento invalido")
                return
            
            self.board[self.position],self.board[self.position-1] = self.board[self.position-1],self.board[self.position] 
            self.position -= 1
        elif direction == 'right':
            if col == 3:
                print("Movimiento invalido")
                return
            
            self.board[self.position],self.board[self.position+1] = self.board[self.position+1],self.board[self.position] 
            self.position += 1

    def verify_move(self, curr_position, movement):
        if (self.movement=='up'or self.movement=='down'):
            return True
        
    def increase_move(self,movement):
        if self.verify_move(self.position, movement):
            self.cont_move+=1

    def is_solved(self):
        for i in range(15):
            if i + 1 != self.board[i]:
                return False
            
        if self.board[15] != 0:
            return False
        
        return True

        

    def display_console(self):
        '''
        Escribe en la consola el estado del tablero
        '''
        print("="*20)
        print("Tablero Actualizado")
        for i in range(4):
            for j in range(4):
                print(f'{self.board[4*i+ j]}', end=" | ")
            print()

        print("="*20)
        



