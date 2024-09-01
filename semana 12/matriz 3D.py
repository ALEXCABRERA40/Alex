# Definición de las temperaturas en una matriz 3D
temperaturas = [
    [  # Ciudad 1
        [  # Semana 1
            {"dia": "Lunes", "temp": 28},
            {"dia": "Martes", "temp": 30},
            {"dia": "Miércoles", "temp": 32},
            {"dia": "Jueves", "temp": 29},
            {"dia": "Viernes", "temp": 35},
            {"dia": "Sábado", "temp": 28},
            {"dia": "Domingo", "temp": 32}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temp": 26},
            {"dia": "Martes", "temp": 29},
            {"dia": "Miércoles", "temp": 33},
            {"dia": "Jueves", "temp": 31},
            {"dia": "Viernes", "temp": 27},
            {"dia": "Sábado", "temp": 29},
            {"dia": "Domingo", "temp": 33}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temp": 27},
            {"dia": "Martes", "temp": 31},
            {"dia": "Miércoles", "temp": 25},
            {"dia": "Jueves", "temp": 32},
            {"dia": "Viernes", "temp": 28},
            {"dia": "Sábado", "temp": 31},
            {"dia": "Domingo", "temp": 25}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temp": 25},
            {"dia": "Martes", "temp": 28},
            {"dia": "Miércoles", "temp": 30},
            {"dia": "Jueves", "temp": 29},
            {"dia": "Viernes", "temp": 34},
            {"dia": "Sábado", "temp": 27},
            {"dia": "Domingo", "temp": 31}
        ]
    ],
    [  # Ciudad 2
        [  # Semana 1
            {"dia": "Lunes", "temp": 32},
            {"dia": "Martes", "temp": 34},
            {"dia": "Miércoles", "temp": 28},
            {"dia": "Jueves", "temp": 30},
            {"dia": "Viernes", "temp": 33},
            {"dia": "Sábado", "temp": 25},
            {"dia": "Domingo", "temp": 29}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temp": 33},
            {"dia": "Martes", "temp": 36},
            {"dia": "Miércoles", "temp": 30},
            {"dia": "Jueves", "temp": 32},
            {"dia": "Viernes", "temp": 25},
            {"dia": "Sábado", "temp": 27},
            {"dia": "Domingo", "temp": 31}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temp": 31},
            {"dia": "Martes", "temp": 35},
            {"dia": "Miércoles", "temp": 28},
            {"dia": "Jueves", "temp": 30},
            {"dia": "Viernes", "temp": 32},
            {"dia": "Sábado", "temp": 26},
            {"dia": "Domingo", "temp": 30}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temp": 34},
            {"dia": "Martes", "temp": 27},
            {"dia": "Miércoles", "temp": 29},
            {"dia": "Jueves", "temp": 21},
            {"dia": "Viernes", "temp": 34},
            {"dia": "Sábado", "temp": 27},
            {"dia": "Domingo", "temp": 30}
        ]
    ],
    [  # Ciudad 3
        [  # Semana 1
            {"dia": "Lunes", "temp": 30},
            {"dia": "Martes", "temp": 32},
            {"dia": "Miércoles", "temp": 34},
            {"dia": "Jueves", "temp": 31},
            {"dia": "Viernes", "temp": 28},
            {"dia": "Sábado", "temp": 25},
            {"dia": "Domingo", "temp": 32}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temp": 29},
            {"dia": "Martes", "temp": 31},
            {"dia": "Miércoles", "temp": 33},
            {"dia": "Jueves", "temp": 30},
            {"dia": "Viernes", "temp": 27},
            {"dia": "Sábado", "temp": 34},
            {"dia": "Domingo", "temp": 31}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temp": 31},
            {"dia": "Martes", "temp": 23},
            {"dia": "Miércoles", "temp": 35},
            {"dia": "Jueves", "temp": 32},
            {"dia": "Viernes", "temp": 29},
            {"dia": "Sábado", "temp": 26},
            {"dia": "Domingo", "temp": 23}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temp": 28},
            {"dia": "Martes", "temp": 30},
            {"dia": "Miércoles", "temp": 22},
            {"dia": "Jueves", "temp": 39},
            {"dia": "Viernes", "temp": 36},
            {"dia": "Sábado", "temp": 33},
            {"dia": "Domingo", "temp": 20}
        ]
    ]
]

# Calcular y mostrar el promedio de temperaturas para cada ciudad y semana
ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]

print("Promedio de temperaturas por ciudad y semana:")
for i in range(len(temperaturas)):  # Iterar sobre las ciudades
    for j in range(len(temperaturas[i])):  # Iterar sobre las semanas
        suma_temp = 0
        for dia in temperaturas[i][j]:  # Iterar sobre los días de la semana
            suma_temp += dia["temp"]  # Sumar las temperaturas
        promedio = suma_temp / len(temperaturas[i][j])  # Calcular el promedio
        print(f"Promedio de {ciudades[i]} para la semana {j + 1}: {promedio:.2f} °C")
