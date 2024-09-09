# Definir la estructura de datos para almacenar temperaturas
# Ciudades: Quito, Loja, Cuenca -> Semanas -> Días de la semana
temperaturas = [
    [  # Quito
        [("Lunes", 20), ("Martes", 22), ("Miércoles", 21), ("Jueves", 19), ("Viernes", 23), ("Sábado", 24), ("Domingo", 21)],  # Semana 1
        [("Lunes", 18), ("Martes", 20), ("Miércoles", 19), ("Jueves", 21), ("Viernes", 22), ("Sábado", 23), ("Domingo", 22)],  # Semana 2
        [("Lunes", 23), ("Martes", 24), ("Miércoles", 25), ("Jueves", 22), ("Viernes", 20), ("Sábado", 21), ("Domingo", 19)],  # Semana 3
        [("Lunes", 19), ("Martes", 18), ("Miércoles", 20), ("Jueves", 21), ("Viernes", 23), ("Sábado", 22), ("Domingo", 21)]   # Semana 4
    ],
    [  # Loja
        [("Lunes", 25), ("Martes", 27), ("Miércoles", 28), ("Jueves", 26), ("Viernes", 29), ("Sábado", 30), ("Domingo", 28)],  # Semana 1
        [("Lunes", 28), ("Martes", 29), ("Miércoles", 27), ("Jueves", 26), ("Viernes", 25), ("Sábado", 28), ("Domingo", 27)],  # Semana 2
        [("Lunes", 26), ("Martes", 24), ("Miércoles", 25), ("Jueves", 23), ("Viernes", 22), ("Sábado", 24), ("Domingo", 25)],  # Semana 3
        [("Lunes", 22), ("Martes", 23), ("Miércoles", 21), ("Jueves", 20), ("Viernes", 22), ("Sábado", 23), ("Domingo", 21)]   # Semana 4
    ],
    [  # Cuenca
        [("Lunes", 18), ("Martes", 20), ("Miércoles", 22), ("Jueves", 21), ("Viernes", 19), ("Sábado", 20), ("Domingo", 21)],  # Semana 1
        [("Lunes", 22), ("Martes", 23), ("Miércoles", 24), ("Jueves", 22), ("Viernes", 23), ("Sábado", 21), ("Domingo", 20)],  # Semana 2
        [("Lunes", 20), ("Martes", 19), ("Miércoles", 21), ("Jueves", 20), ("Viernes", 18), ("Sábado", 19), ("Domingo", 17)],  # Semana 3
        [("Lunes", 19), ("Martes", 20), ("Miércoles", 22), ("Jueves", 21), ("Viernes", 23), ("Sábado", 22), ("Domingo", 24)]   # Semana 4
    ]
]

# Calcular y mostrar el promedio de temperaturas para cada ciudad y semana
ciudades = ["Quito", "Loja", "Cuenca"]

for i in range(len(temperaturas)):
    print(f"Promedio de temperaturas en {ciudades[i]}:")
    for j in range(len(temperaturas[i])):
        suma = 0
        print(f"  Semana {j + 1}:")
        for dia in temperaturas[i][j]:
            suma += dia[1]
            print(f"    {dia[0]}: {dia[1]}°C")
        promedio = suma / len(temperaturas[i][j])
        print(f"    -> Promedio semanal: {promedio:.2f}°C\n")
    print("-" * 40)
