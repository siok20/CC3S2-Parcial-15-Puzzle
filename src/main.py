import random
import time
import pygame
from puzzle import puzzle
from prometheus_client import CollectorRegistry, Counter, Gauge, push_to_gateway

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

# Definimos las metricas
registry = CollectorRegistry()
total_operations = Counter(
    'python_request_operations_total', 
    'El número total de operaciones procesadas',registry=registry
)

total_moves = Counter(
    'game_moves_total', 
    'El número total de movimientos',registry=registry
)

average_move_time = Gauge(
    'game_average_move_time_seconds', 
    'Tiempo promedio por movimiento en segundos',registry=registry
)
def registrar_total_moves():
    total_moves.inc()  # Incrementa el contador de movimientos
    push_to_gateway('pushgateway:9091', job='game', registry=registry)

def registrar_average_move_time(move_time):
    average_move_time.set(move_time)  # Establece el tiempo de movimiento
    push_to_gateway('pushgateway:9091', job='game', registry=registry)

def registrar_total_operations():
    total_operations.inc()  # Incrementa el contador de operaciones
    push_to_gateway('pushgateway:9091', job='game', registry=registry)


class Puzzle_GUI:
    def __init__(self):
        self.game = puzzle()
        self.last_move_time = time.time() #Metrica: Empezar a tomar el tiempo

    def draw(self):
        screen.fill(BACKGROUND_COLOR)  # Se rellena  el fondo
        for row in range(BOARD_SIZE):   # recorre cada fila y columna
            for col in range(BOARD_SIZE):
                value = self.game.board[row*4 + col]   # se asigna el valor de cada casilla a value
                
                if value != 0:  # excluir la casilla vacía
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
                current_time = time.time()  # Tiempo actual
                time_between_moves = current_time - puzzle.last_move_time 
                try:
                    if event.key == pygame.K_UP:
                        puzzle.game.move("up")
                        registrar_total_moves()
                    elif event.key == pygame.K_DOWN:
                        puzzle.game.move("down")
                        registrar_total_moves()
                    elif event.key == pygame.K_RIGHT:
                        puzzle.game.move("right")
                        registrar_total_moves()
                    elif event.key == pygame.K_LEFT:
                        puzzle.game.move("left")
                        registrar_total_moves()
                    
                    registrar_average_move_time(time_between_moves) #registramos la metrica del tiempo entre movimeintos
                    puzzle.last_move_time = current_time #Actualizamos el tiempo al actual
                except Exception as e:
                    print(f"Ocurrió un error: {e}")

                puzzle.game.display_console()

                if puzzle.game.is_solved():
                    print("¡Has resuelto el puzzle!")
                    running = False
        visualizer = puzzle.draw()
    
    pygame.quit()

# Ejecutar el programa principal
if __name__ == "__main__":
    main()



