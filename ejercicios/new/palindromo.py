def es_palindromo_recursivo(cadena):
    """
    Comprueba si una cadena es un palíndromo de forma recursiva.

    Parámetros:
      cadena (str): La cadena que se desea comprobar.

    Retorno:
      bool: True si la cadena es un palíndromo, False si no lo es.
    """
    if len(cadena) <= 1:
        return True
    else:
        return cadena[0] == cadena[-1] and es_palindromo_recursivo(cadena[1:-1])


cadena = input("Introduzca una cadena: ")

if es_palindromo_recursivo(cadena):
    print(f"La cadena '{cadena}' es un palíndromo.")
else:
    print(f"La cadena '{cadena}' no es un palíndromo.")
