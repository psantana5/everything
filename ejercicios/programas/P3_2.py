def imprimirTablero(tablero):
    for fila in tablero:
        print(" -------")
        print(" | " + " | ".join(fila) + " |")
    print(" -------")


tablero = [["X", "O", "X"], ["O", "O", " "], [" ", "X", " "]]
imprimirTablero(tablero)
