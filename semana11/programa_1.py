def buscar_valor_en_matriz(matriz, valor_buscado):
    """
    Busca un valor específico en una matriz bidimensional.

    Args:
        matriz: La matriz bidimensional a buscar.
        valor_buscado: El valor a buscar en la matriz.

    Returns:
        Una tupla (fila, columna) si el valor se encuentra,
        o None si no se encuentra.
    """

    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == valor_buscado:
                return i, j

    return None

# Crear una matriz
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Valor a buscar
valor_a_buscar = 9

# Buscar el valor
resultado = buscar_valor_en_matriz(matriz, valor_a_buscar)

if resultado:
    fila, columna = resultado
    print(f"El valor {valor_a_buscar} se encontró en la posición ({fila}, {columna})")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")