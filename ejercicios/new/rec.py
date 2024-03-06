def pedir_numero():
    """
    Función recursiva que pide al usuario un número entre 1 y 10.

    Devuelve:
      El número introducido por el usuario.
    """
    numero = int(input("Introduce un número entre 1 y 10: "))
    if 1 <= numero <= 10:
        return numero
    else:
        print("¡Error! El número debe estar entre 1 y 10.")
        return pedir_numero()


# Ejemplo de uso
numero = pedir_numero()
print("El número introducido es:", numero)
