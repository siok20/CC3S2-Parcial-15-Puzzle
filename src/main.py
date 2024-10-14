import random
import time
import pygame
from puzzle import puzzle

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

class Puzzle_GUI:
    def __init__(self):
        self.game = puzzle()

    def draw(self):
        screen.fill(BACKGROUND_COLOR)  # Se rellena  el fondo
        for row in range(BOARD_SIZE):   # recorre cada fila y columna
            for col in range(BOARD_SIZE):
                value = self.game.board[row*4 + col]   # se asigna el valor de cada casilla a value
                
                if value is not 0:  # excluir la casilla vacía
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
    puzzle = Puzzle_GUI()
    
    visualizer = puzzle.draw()
    
    #actualiza el tablero
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    puzzle.game.move("up")
                if event.key == pygame.K_DOWN:
                    puzzle.game.move("down")
                if event.key == pygame.K_RIGHT:
                    puzzle.game.move("right")
                if event.key == pygame.K_LEFT:
                    puzzle.game.move("left")
                
                puzzle.game.display_console()

                if puzzle.game.is_solved():
                    time.sleep(100)
                    running = False
        
        visualizer = puzzle.draw()
    
    pygame.quit()

# Ejecutar el programa principal
if __name__ == "__main__":
    main()



