from collections import deque

def bfs_numero_paulina(I, B, parejas):
    # Crear grafo de relaciones
    grafo = [[] for _ in range(I)]
    for pareja in parejas:
        a, b = pareja
        grafo[a].append(b)
        grafo[b].append(a)
    
    # Array para almacenar los números paulina (INF = float('inf') para los no alcanzables)
    numeros_paulina = [float('inf')] * I
    numeros_paulina[0] = 0  # Paulina tiene número 0

    # BFS para calcular los números paulina
    cola = deque([0])
    
    while cola:
        actual = cola.popleft()
        for vecino in grafo[actual]:
            if numeros_paulina[vecino] == float('inf'):  # No visitado aún
                numeros_paulina[vecino] = numeros_paulina[actual] + 1
                cola.append(vecino)
    
    return numeros_paulina

def procesar_fiesta(num_casos, casos):
    resultados = []
    
    for i in range(num_casos):
        I, B = casos[i][0]
        parejas = casos[i][1]
        
        numeros_paulina = bfs_numero_paulina(I, B, parejas)
        
        resultado = [f"fiesta {i + 1}:"]
        for persona in range(1, I):  # No incluimos a Paulina (persona 0)
            num_paulina = numeros_paulina[persona]
            if num_paulina == float('inf'):
                resultado.append(f"{persona} INF")
            else:
                resultado.append(f"{persona} {num_paulina}")
        
        resultados.append("\n".join(resultado))
    
    return resultados

# Lectura dinámica de la entrada
num_casos = int(input())  # Número de casos de prueba

casos = []
for _ in range(num_casos):
    I, B = map(int, input().strip().split(", "))
    parejas = [tuple(map(int, input().strip().split())) for _ in range(B)]
    casos.append(((I, B), parejas))

# Procesar los casos
resultados = procesar_fiesta(num_casos, casos)

# Imprimir los resultados
for resultado in resultados:
    print(resultado)
    if resultado != resultados[-1]:
        print()  # Línea en blanco entre casos, pero no después del último caso
