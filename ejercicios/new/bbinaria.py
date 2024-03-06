def busqueda_binaria(lista, elemento):
    """
    Realiza una búsqueda binaria en una lista ordenada.

    Parámetros:
      lista (list): La lista ordenada en la que se realiza la búsqueda.
      elemento (int): El elemento que se desea buscar.

    Retorno:
      bool: True si el elemento está en la lista, False si no lo está.
    """
    if len(lista) == 0:
        return False
    else:
        medio = len(lista) // 2
        if lista[medio] == elemento:
            return True
        elif lista[medio] > elemento:
            return busqueda_binaria(lista[:medio], elemento)
        else:
            return busqueda_binaria(lista[medio + 1:], elemento)


lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
elemento = int(input("Introduzca el elemento que desea buscar: "))

if busqueda_binaria(lista, elemento):
    print(f"El elemento {elemento} está en la lista.")
else:
    print(f"El elemento {elemento} no está en la lista.")
