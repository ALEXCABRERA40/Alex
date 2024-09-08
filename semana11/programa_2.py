def bubble_sort(arr):
    """Ordena una lista usando el algoritmo Bubble Sort."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def ordenar_fila( matriz, fila):
    """Ordena una fila específica de la matriz en orden ascendente."""
    if fila < 0 or fila >= len( matriz):
        raise IndexError("Índice de fila fuera de rango.")
    bubble_sort( matriz[fila])

def mostrar_matriz( matriz):
    """Muestra la matriz en formato legible."""
    for fila in matriz:
        print(fila)

# Matriz de ejemplo 3x3
matriz = [
    [3, 1, 2],
    [9, 5, 6],
    [4, 8, 7]
]

# Mostrar la matriz original
print("Matriz original:")
mostrar_matriz(matriz)

# Ordenar la fila 1 (segunda fila)
fila_a_ordenar = 0
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz después de ordenar la fila
print(f"\nMatriz después de ordenar la fila {fila_a_ordenar}:")
mostrar_matriz(matriz)