def nuevoTablero():
    tablero = [[' ' for i in range(3)] for i in range(3)]
    return tablero


def imprimirTablero(tablero):
    for fila in tablero:
        print('| ' + ' | '.join(fila) + ' |')


# Ejemplo de uso
tablero_vacio = nuevoTablero()
imprimirTablero(tablero_vacio)
