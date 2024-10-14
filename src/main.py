import random

class Puzzle_15:
    def __init__(self):
        self.grid = self.generate_puzzle()
    
    def generate_puzzle(self):
        numbers = list(range(1,16)) + [None]    #genera numeros del 1 al 15 y le añade uno vacio
        random.shuffle(numbers)
        board = []   # Almacena todas las cuadrículas
        for i in range(4):  # Itera sobre las filas
            row = []  # Crear una nueva fila vacía
            for j in range(4):  # Itera sobre las columnas
                row.append(numbers[i * 4 + j])  # Añadir el número correspondiente
            board.append(row)  # Añadir la fila a la cuadrícula
        return board

    def display(self):
        # Recorrer cada fila en la cuadrícula
        for row in self.board:
            # Crear una lista para almacenar los valores de la fila formateados
            print_row = []
            
            #recorre cada valor de la fila
            for val in row:
                if val is None:
                    print_row.append('  ')  # deja un espacio en blanco para la casilla vacia
                else:
                    print_row.append(f"{val:>2}")  # formatea el número para que se alinee a la derecha
            # une los valores formateados con un separador '|' y los imprime
            print(' | '.join(print_row))


# Uso de ejemplo
puzzle = Puzzle_15()
# print(puzzle.generate_puzzle())
puzzle.display()


