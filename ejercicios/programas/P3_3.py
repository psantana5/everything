import subprocess


def imprimirTablero(tablero):
    for fila in tablero:
        print(" -------")
        print(" | " + " | ".join(fila) + " |")
    print(" -------")


tablero = [["X", "O", "X"], ["O", "O", " "], [" ", "X", " "]]
imprimirTablero(tablero)


def cambiarTurno(jugador):
    if jugador == jugador_actual:
        return "O"
    elif jugador2 == "O":
        return "X"
    else:
        print("Jugador no reconocido")
        return None


try:
    jugador_actual_bytes = subprocess.check_output(["whoami"])
    jugador_actual = jugador_actual_bytes.decode("utf-8").strip()
    print("El jugador 1 es:", jugador_actual)

    jugador2 = str(input("¿Cuál es tu nombre, J2?: "))
    print("El jugador 2 es:", jugador2)
except subprocess.CalledProcessError as e:
    print(f"Error al obtener J1: Revisar comando lanzado. {e}")
