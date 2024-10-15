Feature: Juego de Puzzle 

  Scenario: Mover la casilla vacía hacia arriba
    Given el juego tiene una casilla vacía en la posición 5
    When presiono la tecla de flecha arriba
    Then la casilla vacía se debería mover a la posición 1

  Scenario: Mover la casilla vacía hacia la izquierda
    Given el juego tiene una casilla vacía en la posición 5
    When presiono la tecla de flecha izquierda
    Then la casilla vacía se debería mover a la posición 4

  Scenario: Movimiento inválido hacia abajo
    Given el juego tiene una casilla vacía en la posición 13
    When presiono la tecla de flecha abajo
    Then el movimiento debería ser inválido
    And la casilla vacía debería permanecer en la posición 13

  Scenario: Resolver el puzzle
    Given el puzzle está resuelto
    When verifico si el puzzle está resuelto
    Then el resultado debería ser True
