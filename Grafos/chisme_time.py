from collections import deque, defaultdict

def bfs_amigos(grafo, inicio):
    if len(grafo[inicio]) == 0 or grafo[inicio] == [-1]:
        return 0, 0  # Si no tiene amigos, nadie escucha el chisme

    dias = defaultdict(int)  # Para contar cuántos escuchan el chisme en cada día
    visitados = [False] * len(grafo)
    visitados[inicio] = True
    cola = deque([(inicio, 0)])  # (persona, día en el que escuchan el chisme)
    
    while cola:
        actual, dia = cola.popleft()
        for amigo in grafo[actual]:
            if not visitados[amigo]:
                visitados[amigo] = True
                dias[dia + 1] += 1
                cola.append((amigo, dia + 1))
    
    if not dias:  # Si no hay propagación
        return 0, 0
    
    # Encontrar el día de máximo chismorreo
    max_dia = max(dias, key=lambda x: (dias[x], -x))
    return max_dia, dias[max_dia]

def procesar_chismes(P, relaciones, casos):
    grafo = []
    
    # Leer las relaciones de amistad
    for i in range(P):
        amigos = list(map(int, relaciones[i].split()))
        if amigos == [-1]:
            grafo.append([])
        else:
            grafo.append(amigos)
    
    # Procesar cada caso de prueba
    resultados = []
    for caso in casos:
        dia_max, max_chismorreo = bfs_amigos(grafo, caso)
        if max_chismorreo == 0:
            resultados.append("0")
        else:
            resultados.append(f"{dia_max} {max_chismorreo}")
    
    return resultados

# Lectura dinámica de la entrada
P = int(input())  # Número de personas en la comunidad

# Leer las relaciones de amistad para cada persona
relaciones = []
for _ in range(P):
    relaciones.append(input().strip())

# Leer la línea con los casos de prueba (separados por comas y espacios)
casos = list(map(int, input().strip().split(", ")))

# Procesar los casos
resultados = procesar_chismes(P, relaciones, casos)

# Imprimir los resultados
for resultado in resultados:
    print(resultado)
