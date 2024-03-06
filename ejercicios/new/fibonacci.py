def fibonacci(n):
    """
    Calcula el n-ésimo número de Fibonacci de forma recursiva.

    Parámetros:
      n (int): La posición del número de Fibonacci que se desea calcular.

    Retorno:
      int: El n-ésimo número de Fibonacci.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


numero = int(
    input("Introduzca la posición del número de Fibonacci que desea calcular: "))
print(f"El {numero}-ésimo número de Fibonacci es: {fibonacci(numero)}")
