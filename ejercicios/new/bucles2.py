def fibonacci_iterativa(n):
    """
    Calcula el n-ésimo número de Fibonacci de forma iterativa.

    Parámetros:
      n (int): La posición del número de Fibonacci que se desea calcular.

    Retorno:
      int: El n-ésimo número de Fibonacci.
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
