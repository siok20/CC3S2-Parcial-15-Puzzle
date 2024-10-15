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

![](assets/Move.png)

## Prometheus y Grafana
Primero añadimos en requirements.txt el prometheus_client para que al construir y alzar el docker-compose se instale y podamos definir los contadores.

![](assets/def_metrics.png)  

En el archivo prometheus.yml dentro de scrape_configs configuramos un job, el cual sera pushgateway ya que luego apuntará al pushgateway de docker-compose

![](assets/prometheus.png)  

Le decimos al docker-compose.yml que prometheus correrá en el puerto 9090 mientras que grafana en el 3000, y el pushgateway en el 9091, ahí último veremos cómo se recogen las métricas.

![](assets/compose.png) 

Nos vamos al puerto 9090 y veriicamos que el endpoint `pushgateway:9091` esté alzado.
![](assets/verificamos_endpoint.png) 

También verificamos que las métricas generales estén en 9091/metrics y que cambien de acuerdo a los movimientos del juego.
![](assets/metricas_3000.png) 

Nos dirigimos a localhost:3000 para entrar a la interfaz de Grafana, lo conectamos con Prometheus pasándole el url correspondiente.
![](assets/connection.png) 
Verificamos si se ha podido conectar:
![](assets/successfully.png)
Luego realizamos movimientos en el puzzle y seleccionamos algunas métricas para monitorear la aplicación.
![](assets/grafica1.png)
![](assets/grafica2.png)

## Dockerfile y docker-compose.yml
Fue necesario cambiar el docker-compose.yml de acuerdo a las necesidades de nuestro proyecto.
Y lo que nosotros necesitábamos era correr el programa con pygame dentro del contenedor, para ello se necesitaba instalar algunas librerías relacionadas con el sistema X11 de Linux.
Luego de estos cambios se puede correr docker junto al juego con interfaz gráfica y ya no solo localmente con `python3 src/main.py`
```
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos y instala las dependencias de Python
COPY requeriments.txt .
RUN pip install --no-cache-dir -r requeriments.txt

# Copia el resto del código fuente
COPY . ./

# Instala las dependencias del sistema necesarias para Pygame
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libxinerama1 \
    libxi6 \
    libxcursor1 \
    libxtst6 \
    tk-dev \
    x11-apps\
    && rm -rf /var/lib/apt/lists/*

# Comando por defecto para ejecutar el juego
CMD ["python", "src/main.py"]

```