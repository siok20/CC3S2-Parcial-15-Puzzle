# language: es

Caracteristica: Generación del puzzle

  Escenario: Generar una cuadrícula de 4x4
    Dado que he generado un nuevo puzzle
    Entonces el puzzle debería ser un tablero de 4x4
    Y el puzzle debería contener números del 1 al 15 y un espacio vacío
    Y el puzzle debería ser resoluble
