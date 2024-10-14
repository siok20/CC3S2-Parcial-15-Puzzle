import random
import pygame

pygame.init()   # inicializamos pygame

# Configurar colores
BACKGROUND_COLOR = (187, 173, 160)  # Color de fondo de la ventana
CELL_COLOR = (238, 228, 218)        # Color de los cuadros
NUMBER_COLOR = (119, 110, 101)      # Color de los números en los cuadros

# Configurar dimensiones de la ventana
CELL_SIZE = 100
BOARD_SIZE = 4
WINDOW_SIZE = CELL_SIZE * BOARD_SIZE

# Inicializar la pantalla de pygame
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("15 Puzzle Game")

# Configurar fuente
font = pygame.font.Font(None, 50)


class Puzzle_15:
    def __init__(self):
        self.board = self.generate_puzzle()
        
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


class Puzzle_GUI:
    def __init__(self, board):
        self.board = board

    def draw(self):
        screen.fill(BACKGROUND_COLOR)  # Se rellena  el fondo
        for row in range(BOARD_SIZE):   # recorre cada fila y columna
            for col in range(BOARD_SIZE):
                value = self.board[row][col]    # se asigna el valor de cada casilla a value
                if value is not None:  # excluir la casilla vacía
                    # dibujar la casilla con el número
                    pygame.draw.rect(screen, CELL_COLOR, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    text = font.render(str(value), True, NUMBER_COLOR)
                    text_rect = text.get_rect(center=((col * CELL_SIZE) + CELL_SIZE // 2, (row * CELL_SIZE) + CELL_SIZE // 2))
                    screen.blit(text, text_rect)
                else:
                    # dibujar la casilla vacío
                    pygame.draw.rect(screen, BACKGROUND_COLOR, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(screen, CELL_COLOR, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)
        
        pygame.display.flip()

def main():
    # Crear puzzle
    puzzle = Puzzle_15()
    
    # Visualizar en consola
    print("Visualización en consola:")
    puzzle.display()
    
    # Visualización gráfica con pygame
    visualizer = Puzzle_GUI(puzzle.board)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        visualizer.draw()
    
    pygame.quit()

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
# Uso de ejemplo
#puzzle = Puzzle_15()
# print(puzzle.generate_puzzle())
#puzzle.display()


