def calcular_promedio_temperaturas(temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad en un conjunto de datos.

    Args:
        temperaturas:las claves son los nombres de las ciudades
            y los valores son listas de listas, donde cada lista interna representa una semana
            y contiene las temperaturas diarias de esa semana.

    Returns:
        las claves son los nombres de las ciudades y los valores
        son las temperaturas promedio de cada ciudad.
    """

    promedios = {}
    for ciudad, semanas in temperaturas.items():
        temperaturas_totales = 0
        num_temperaturas = 0
        for semana in semanas:
            temperaturas_totales += sum(semana)
            num_temperaturas += len(semana)
        promedios[ciudad] = temperaturas_totales / num_temperaturas
    return promedios

# Ejemplo de uso:
datos_temperaturas = {
    "Ciudad 1": [[20, 22, 21, 23], [25, 24, 26, 27], [28, 29, 30, 29], [22, 21, 23, 24]],
    "Ciudad 2": [[18, 19, 20, 19], [22, 23, 24, 25], [26, 27, 28, 27], [20, 21, 22, 21]],
    "Ciudad 3": [[15, 16, 17, 18], [20, 21, 22, 23], [24, 25, 26, 25], [18, 19, 20, 19]]
}

resultado = calcular_promedio_temperaturas(datos_temperaturas)
print(resultado)
