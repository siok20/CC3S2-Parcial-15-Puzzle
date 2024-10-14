# Juego de puzzles "15-Puzzle"

# ¿Como correr el juego?

### src/
Carpeta con los archivos del juego

#### main.py
Contiene la visualización del juego con la librería pygame
#### puzzle.py
Contiene la lógica del juego

### tests/
Añadiremos los tests durante el desarrollo

## Descripción:
```bash
git clone https://github.com/siok20/CC3S2-Parcial-15-Puzzle
```

## Correr localmente con pygame
```
python src/main.py
```
Juego contenerizado en Docker

```bash
docker build -t game .
```

```bash
docker run game 
```

### Características clave:

• Generación de puzzles desordenados.

• Movimiento de piezas con reglas.

• Verificación de solución y conteo de movimientos.

### Características clave:

• Generación aleatoria de puzzles.

• Movimiento de piezas con reglas específicas.

• Verificación de la solución y conteo de movimientos.

## Puzzle.py
### Generar board
Generamos un board, una lista de números del 0 al 15 desordenada, donde 0 representa a la posición vacía

```python
def generate_board_position(self):
    Fboard = [i for i in range(16)]
    board = []
    j = 0
    while Fboard != []:
        i = rd.choice(Fboard)

        if i == 0:
            position = j
        j += 1
    
    return board, position
```

![alt text](assets/generateBoard.png)

### Movimiento 
Se define un movimiento y el juego evalúa si es válido 
De serlo se procede a modificar el board

```python
def move(self, direction):
    '''
    Logica de movimiento
    obtiene una direccion y el juego cambia las posiciones
    del elemento vacio y hacia donde se dirige

    En caso de movimiento valido
    '''
    row = self.position // 4
    col = self.position % 4

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

```

Ejemplo aplicando el movimiento `'up'`

![alt text](assets/Move.png)


