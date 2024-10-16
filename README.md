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

En esta rama se implemento la visualizacion y generación del tablero para el juego. 
Para implementar la interfaz al juego primero se hizo la salida en consola luego se decidió usar la librería `pygame` con lo cual ya teniamos mayor facilidad para hacer los movimientos con las flechas del teclado.

Primera salida por consola 
![](assets/console_initial.png)

Salida luego de implementarlo con la libreria pygame
![](assets/pygame.png)

Tammbién se implemento los eventos para los movimeintos de las flechas en el teclado.

```python
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
```

Luego se decidio implementar la actualización de los movimientos en la consola usando la función display, esos cambios se realizaron en la rama `feature/eladio` ya que contenía la lógica de los movimientos con lo cual ya se podía tener el estado del tablero por cada movimiento.

![](assets/console_gui.png)


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


### Configuración del pipeline

En el directorio `.github/workflows` se creo el archivo `ci.yml` que configura un pipeline de integración continua (CI) utilizando GitHub Actions. Este pipeline está diseñado para automatizar el proceso de pruebas.

```yaml
name: CI - Pipeline

on:
  push:
    branches:
      - develop
      - feature/daniela
  pull_request:
    branches:
      - develop
      - feature/daniela

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'  

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requeriments.txt
        pip install behave pytest 

    - name: Run Unit Tests  
      run: pytest tests/  
      

    - name: Run Behave Tests  
      run: behave tests/features/ 
```
