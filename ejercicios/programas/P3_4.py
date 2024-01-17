import subprocess


def imprimirTablero(tablero):
    for fila in tablero:
        print(" -------")
        print(" | " + " | ".join(fila) + " |")
    print(" -------")


def cambiarTurno(jugador_actual, jugador1, jugador2):
    if jugador_actual == jugador1:
        return jugador2
    elif jugador_actual == jugador2:
        return jugador1
    else:
        print("Jugador no reconocido")
        return None


def colocarFicha(tablero, pos, jugador):
    fila, columna = pos

    # Verificar si la posición está dentro del rango del tablero
    if 0 <= fila < len(tablero) and 0 <= columna < len(tablero[0]):
        # Verificar si la casilla está vacía
        if tablero[fila][columna] == ' ':
            # Casilla vacía, colocar la ficha del jugador
            tablero[fila][columna] = jugador
            return True
        else:
            # Casilla no está vacía, devolver False
            return False
    else:
        # Posición fuera de rango del tablero
        print("Posición fuera de rango del tablero. Introduce una posición válida.")
        return False


try:
    jugador_actual_bytes = subprocess.check_output(["whoami"])
    jugador_actual = jugador_actual_bytes.decode("utf-8").strip()
    print("El jugador 1 es:", jugador_actual)

    jugador2 = str(input("¿Cuál es tu nombre, J2?: "))
    print("El jugador 2 es:", jugador2)

    # Crear un nuevo tablero
    tablero = [[' ' for _ in range(3)] for _ in range(3)]

    # Imprimir el tablero inicial
    imprimirTablero(tablero)

    while True:
        try:
            # Obtener el jugador actual
            jugador_actual = cambiarTurno(
                jugador_actual, jugador_actual, jugador2)

            # Pedir al jugador actual que introduzca la posición
            posicion = tuple(map(int, input(
                f"{jugador_actual}, introduce la posición (fila columna): ").split()))

            if len(posicion) == 2:
                if colocarFicha(tablero, posicion, "X" if jugador_actual == jugador_actual else "O"):
                    print(
                        f"Ficha colocada por {jugador_actual} en la posición {posicion}")
                    # Imprimir el tablero después de colocar la ficha
                    imprimirTablero(tablero)
                else:
                    print(
                        f"La posición {posicion} ya está ocupada o es inválida, intenta de nuevo.")
            else:
                print(
                    "Por favor, ingresa dos valores numéricos separados por un espacio.")

        except ValueError:
            print(
                "Entrada inválida. Por favor, ingresa dos valores numéricos separados por un espacio.")

except subprocess.CalledProcessError as e:
    print(f"Error al obtener J1: Revisar comando lanzado. {e}")
