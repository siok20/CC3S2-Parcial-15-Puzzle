# Juego de puzzles "15-Puzzle"

## Estructura del proyecto 

### src/
Carpeta con los archivos del juego

#### main.py
Contiene la visualización del juego con la librería pygame
#### puzzle.py
Contiene la lógica del juego

### tests/
Añadiremos los tests durante el desarrollo

## Descripción:
Consiste en un juego de rompecabezas deslizante donde el jugador debe ordenar las piezas numeradas en una cuadrícula.

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


## Pruebas de comportamiento

Para las pruebas de comportamiento utilizamos Gherkin con Behave, definimos los escenarios y luego traducimos los pasaos a lenguaje python.

Po ejemplo definimos el escenario donde un movimiento es invalido de la siguiente forma:

```gherkin
  Scenario: Movimiento inválido hacia abajo
    Given el juego tiene una casilla vacía en la posición 13
    When presiono la tecla de flecha abajo
    Then el movimiento debería ser inválido
    And la casilla vacía debería permanecer en la posición 13
```

Esto se traduce con behave como:

```python
@given('el juego tiene una casilla vacía en la posición {position}')
def step_given_juego_con_casilla_vacia(context, position):
    context.game = puzzle()
    position = int(position)
    
    tablero = [i for i in range(1, 16)] #crea una lista de numeros del 1 al 15
    tablero.insert(position, 0) #inserta el 0 en la posicion que se especifica

    context.game.set_board(tablero) #se asigna el tablero generado al juegp
    context.game.position = position  #se establece la posición de la casilla vacía

@when('presiono la tecla de flecha abajo')
def step_when_mover_abajo(context):
    context.result = context.game.move("down")

@then('el movimiento debería ser inválido')
def step_then_movimiento_invalido(context):
    assert context.result == False, "El movimiento debería ser inválido"

@then('la casilla vacía debería permanecer en la posición {position}')
def step_then_casilla_vacia_posicion(context, position):
    position = int(position)
    assert context.game.position == position, f"La posición esperada era {position} pero resultó {context.game.position}"

```

De esa misma forma definimos 3 escenarios más. Luego para correr las pruebas debemos ejecutar el comando:

```bash
behave tests/features/
```

Debería obtener un resultado como este:

![](assets/behave_test.png)

