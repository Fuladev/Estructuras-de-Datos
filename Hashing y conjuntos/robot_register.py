def registro_civil_robotico():
    # Leer la cantidad inicial de robots
    F = int(input().strip())
    
    # Crear un conjunto con los identificadores iniciales de los robots (1 a F)
    robots = set(range(1, F + 1))
    
    while True:
        # Leer el comando
        comando = input().strip()
        
        # Si es la línea final, terminamos
        if comando == "#":
            break
        
        # Si el comando es "new"
        if comando.startswith("new"):
            _, M, N = comando.split()
            M, N = int(M), int(N)
            nuevo_robot = M + N
            
            # Encontrar un identificador disponible
            while nuevo_robot in robots:
                nuevo_robot += 1
            
            # Agregar el nuevo robot al conjunto
            robots.add(nuevo_robot)
        
        # Si el comando es "search"
        elif comando.startswith("search"):
            _, X = comando.split()
            X = int(X)
            
            # Verificar si el robot existe
            if X in robots:
                print("existe")
            else:
                print("no existe")

# Ejecutar la función
registro_civil_robotico()
