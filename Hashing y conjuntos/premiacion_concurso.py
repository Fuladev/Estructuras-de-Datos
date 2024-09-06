def premiacion_curso():
    # Leer el número de estudiantes que resolvieron el ejercicio 1
    N1 = int(input().strip())
    estudiantes_ejercicio1 = set(int(input().strip()) for _ in range(N1))
    
    # Leer el número de estudiantes que resolvieron el ejercicio 2
    N2 = int(input().strip())
    estudiantes_ejercicio2 = set(int(input().strip()) for _ in range(N2))
    
    # Leer el número de estudiantes que resolvieron el ejercicio 3
    N3 = int(input().strip())
    estudiantes_ejercicio3 = set(int(input().strip()) for _ in range(N3))
    
    # Leer el número de estudiantes que resolvieron el ejercicio 4
    N4 = int(input().strip())
    estudiantes_ejercicio4 = set(int(input().strip()) for _ in range(N4))
    
    # Leer el número de estudiantes que resolvieron el ejercicio 5
    N5 = int(input().strip())
    estudiantes_ejercicio5 = set(int(input().strip()) for _ in range(N5))
    
    # Encontrar la intersección de los 5 conjuntos para identificar a los ganadores
    ganadores = (estudiantes_ejercicio1 & estudiantes_ejercicio2 & 
                 estudiantes_ejercicio3 & estudiantes_ejercicio4 & 
                 estudiantes_ejercicio5)
    
    # Si hay ganadores, calcular el premio por persona
    if ganadores:
        premio_por_ganador = 1000000 // len(ganadores)
        print(premio_por_ganador)
    else:
        print("Nadie gana")

# Ejecutar la función
premiacion_curso()
