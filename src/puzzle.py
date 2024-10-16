import random as rd
import time
from prometheus_client import Counter

graphs = {}
graphs['c'] = Counter('python_request_operations_total', 'The total number of processed requests')
graphs['m'] = Counter('game_moves_total', 'The total number of move')

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
        self.cont_move = 0
        self.board, self.position = self.generate_board_position()

    def generate_board_position(self):
        '''
        Genera board y nos da la posicion del elemento vacio y ademas
        verificamos que el juego tenga solucion
        '''
        flag = True

        while flag:
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

            if self.is_solvable(board, position):
                break

        return board, position
    
    def is_solvable(self, board, position):
        '''
        Verificamos que el tablero sea soluble 
        Criterio:
            inversion: con dos numeros uno en la posicion i y el otro en j, i<j
                       sumamos una inversion si board[i] > board[j]
            
            para un tablero nxn, donde n es par
            El juego es soluble si y solo si el numero de inversiones mas la fila   
            del cuadrado en blanco es par
        '''

        inversions = 0
        #contamos la cantidad de inversiones
        for i in range(len(board)):
            for t in range(i+1, len(board)):
                if board[i]>board[t]:
                    inversions += 1

        row = position//4 + 1

        return (inversions + row) % 2 !=0


    
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
        


        if direction == 'up':
            if row == 0: 
                self.display_error()
                return False

            self.board[self.position],self.board[self.position-4] = self.board[self.position-4],self.board[self.position] 
            self.position -=4
            self.cont_move+=1

        elif direction == 'down':
            if row == 3: 
                self.display_error()
                return False
            
            self.board[self.position],self.board[self.position+4] = self.board[self.position+4],self.board[self.position] 
            self.position +=4
            self.cont_move+=1

        elif direction =='left':
            if col == 0:
                self.display_error()
                return False
            
            self.board[self.position],self.board[self.position-1] = self.board[self.position-1],self.board[self.position] 
            self.position -= 1
            self.cont_move+=1

        elif direction == 'right':
            if col == 3:
                self.display_error()
                return False
            
            self.board[self.position],self.board[self.position+1] = self.board[self.position+1],self.board[self.position] 
            self.position += 1
            self.cont_move+=1
        return True
        
    def increase_move(self,movement):
        if self.verify_move(self.position, movement):

            self.cont_move+=1
        print(f"Total de movimientos: {self.cont_move}")
        

    def is_solved(self):
        for i in range(15):
            if i + 1 != self.board[i]:
                return False
            
        if self.board[15] != 0:
            return False
        
        self.display_end()

        return True

    def display_error(self):
        print("="*50)

        print("#\t\t" + "-----ERROR----- "+ "\t" *2 + " #")
        print("="*50)

    def display_end(self):
        print("="*50)

        print("#\t\t" + "------FIN------ "+ "\t" *2 + " #")
        print("="*50)


    def display_console(self):
        '''
        Escribe en la consola el estado del tablero
        '''
        print("="*50)
        print("#Tablero Actualizado" + "\t"*4 + " #")
        print("#\t" + "-"*33 + "\t" + " #")
        for i in range(4):
            print("#\t|",end=" ")
            for j in range(4):
                print(f'{self.board[4*i+ j]}', end="\t| ")
            print("\t #", end="\n")
            print("#\t" + "-"*33 + "\t" + " #")

        print("="*50)
        

def main():
    game = puzzle()
    game.display_console()
    
    #actualiza el tablero
    running = True
    while running:
        print("Movimientos permitidos: up, down, left, right")
        move = input("Ingrese movimiento o salir (quit): ")

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
        
    print(f"Total de movimientos: {game.cont_move}")

    
    
if __name__ == "__main__":
    main()

