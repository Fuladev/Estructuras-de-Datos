def definir_militancia():
    # Diccionario para almacenar los partidos por los que ha votado cada votante
    votantes = {}

    while True:
        entrada = input().strip()
        
        # Fin de la entrada
        if entrada == "#":
            break
        
        documento, partido = entrada.split()
        documento = int(documento)
        
        # Añadimos el partido al conjunto de partidos del votante
        if documento not in votantes:
            votantes[documento] = set()
        votantes[documento].add(partido)
    
    # Variables para contar los tipos de militancia
    militancia_estricta = 0
    votan_dos_partidos = 0
    votan_tres_partidos = 0
    
    # Clasificar votantes
    for partidos in votantes.values():
        if len(partidos) == 1:
            militancia_estricta += 1
        elif len(partidos) == 2:
            votan_dos_partidos += 1
        elif len(partidos) == 3:
            votan_tres_partidos += 1
    
    # Imprimir el resultado
    print(militancia_estricta, votan_dos_partidos, votan_tres_partidos)

# Ejecutar la función
definir_militancia()
