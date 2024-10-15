import random as rd
import time
from prometheus_client import Counter, Gauge, push_to_gateway

# Definimos las metricas
total_operations = Counter(
    'python_request_operations_total', 
    'El número total de operaciones procesadas'
)

total_moves = Counter(
    'game_moves_total', 
    'El número total de movimientos'
)

average_move_time = Gauge(
    'game_average_move_time_seconds', 
    'Tiempo promedio por movimiento en segundos'
)

def registrar_movimiento(): #para hacer el push al gateway de prometheus e incrementar moves
    total_moves.inc()
    push_to_gateway('pushgateway:9091', job='game', registry=total_moves._registry)

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

        start_move_time = time.time() 

        if direction == 'up':
            if row == 0: 
                print("Movimiento invalido")
                return

            self.board[self.position],self.board[self.position-4] = self.board[self.position-4],self.board[self.position] 
            self.position -=4
            registrar_movimiento()

        elif direction == 'down':
            if row == 3: 
                print("Movimiento invalido")
                return
            
            self.board[self.position],self.board[self.position+4] = self.board[self.position+4],self.board[self.position] 
            self.position +=4
            registrar_movimiento()

        elif direction =='left':
            if col == 0:
                print("Movimiento invalido")
                return
            
            self.board[self.position],self.board[self.position-1] = self.board[self.position-1],self.board[self.position] 
            self.position -= 1
            registrar_movimiento()

        elif direction == 'right':
            if col == 3:
                print("Movimiento invalido")
                return
            
            self.board[self.position],self.board[self.position+1] = self.board[self.position+1],self.board[self.position] 
            self.position += 1
            registrar_movimiento()
            
        move_time = time.time() - start_move_time
        average_move_time.set(move_time)
        
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

def main():
    global total_operations

    game = puzzle()
    game.display_console()
    
    #actualiza el tablero
    running = True
    while running:
        print("Movimientos permitidos: up, down, left, right")
        move = input("Ingrese movimiento o salir (quit): ")
        total_operations.inc()

        if move.lower() == 'quit':
            running = False
        else:
            if move.lower() == 'up':
                game.move("up")
            if move.lower() == 'down':
                game.move("down")
            if move.lower() == 'right':
                game.move("right")
            if move.lower() == 'left':
                game.move("left")
            
            game.display_console()

            if game.is_solved():
                time.sleep(100)
                running = False
        

    print("juego finalizado")
    
    
if __name__ == "__main__":
    main()

