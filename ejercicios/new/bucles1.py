def busqueda_binaria_iterativa(lista, elemento):
    """
    Realiza una búsqueda binaria en una lista ordenada sin usar recursividad.

    Parámetros:
      lista (list): La lista ordenada en la que se realiza la búsqueda.
      elemento (int): El elemento que se desea buscar.

    Retorno:
      bool: True si el elemento está en la lista, False si no lo está.
    """
    bajo = 0
    alto = len(lista) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == elemento:
            return True
        elif lista[medio] > elemento:
            alto = medio - 1
        else:
            bajo = medio + 1

    return False
