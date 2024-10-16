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


## Implementación de la interfaz gáfica del juego

Para implementar la interfaz al juego primero se hizo la salida en consola luego se decidió usar la librería `pygame` con lo cual ya teniamos mayor facilidad para hacer los movimientos con las flechas del teclado

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

