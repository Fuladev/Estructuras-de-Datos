def poblacion_konoha():
    estado_habitantes = {}  # Diccionario para rastrear el estado de cada habitante
    poblacion = 0  # Inicia la población en 0

    while True:
        entrada = input().strip()
        if entrada == "E":
            break
        
        tipo, doc_id = entrada.split()
        doc_id = int(doc_id)
        
        if tipo == "B":  # Nacimiento
            if doc_id not in estado_habitantes:  # Si no ha sido registrado
                estado_habitantes[doc_id] = "vivo"
                poblacion += 1
            # Si ya está registrado, es un error y no hacemos nada

        elif tipo == "D":  # Deceso
            if estado_habitantes.get(doc_id) == "vivo":  # Solo cuenta si estaba vivo
                estado_habitantes[doc_id] = "muerto"
                poblacion -= 1
            # Si ya estaba muerto o no existía, es un error y no hacemos nada

        elif tipo == "R":  # Resucitación
            if estado_habitantes.get(doc_id) == "muerto":  # Solo cuenta si estaba muerto
                estado_habitantes[doc_id] = "vivo"
                poblacion += 1
            # Si ya estaba vivo o no existía, es un error y no hacemos nada

    # Imprimir la población final
    print(poblacion)

# Ejecutar la función
poblacion_konoha()
