FROM python:3.9-slim

WORKDIR /app

COPY requeriments.txt .

RUN pip install -r requeriments.txt

COPY . ./

ENV DISPLAY=host.docker.internal:0.0

CMD ["python", "src/main.py"]
