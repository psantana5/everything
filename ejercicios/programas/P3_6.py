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

    if 0 <= fila < len(tablero) and 0 <= columna < len(tablero[0]):
        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = jugador
            return True
        else:
            return False
    else:
        print("Posición fuera de rango del tablero. Introduce una posición válida.")
        return False


def comprobarGanador(tablero):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != ' ':
            return tablero[i][0]

        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != ' ':
            return tablero[0][i]

    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != ' ':
        return tablero[0][0]

    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != ' ':
        return tablero[0][2]

    for fila in tablero:
        if ' ' in fila:
            return True

    return False


try:
    jugador_actual_bytes = subprocess.check_output(["whoami"])
    jugador_actual = jugador_actual_bytes.decode("utf-8").strip()
    print("El jugador 1 es:", jugador_actual)

    jugador2 = str(input("¿Cuál es tu nombre, J2?: "))
    print("El jugador 2 es:", jugador2)

    tablero = [[' ' for _ in range(3)] for _ in range(3)]

    imprimirTablero(tablero)

    while True:
        try:
            jugador_actual = cambiarTurno(
                jugador_actual, jugador_actual, jugador2)

            posicion = tuple(map(int, input(
                f"{jugador_actual}, introduce la posición (fila columna): ").split()))

            if len(posicion) == 2:
                if colocarFicha(tablero, posicion, "X" if jugador_actual == jugador_actual else "O"):
                    print(
                        f"Ficha colocada por {jugador_actual} en la posición {posicion}")
                    imprimirTablero(tablero)

                    resultado = comprobarGanador(tablero)

                    if resultado == True:
                        print("El juego continúa.")
                    elif resultado == False:
                        print("¡Es un empate!")
                        break
                    else:
                        print(f"¡Ha ganado el jugador {resultado}!")
                        break
                else:
                    print(
                        f"La posición {posicion} ya está ocupada o es inválida, intenta de nuevo.")
            else:
                print(
                    "Por favor, pon dos valores numéricos separados por un espacio.")

        except ValueError:
            print(
                "Entrada inválida. Por favor, pon dos valores numéricos separados por un espacio.")

except subprocess.CalledProcessError as e:
    print(f"Error al obtener J1: Revisar comando lanzado. {e}")
