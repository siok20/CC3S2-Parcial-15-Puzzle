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

