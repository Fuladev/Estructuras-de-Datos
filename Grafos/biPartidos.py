from collections import deque

def es_bipartito(nodos, aristas):
    # Inicializar lista de adyacencia
    grafo = [[] for _ in range(nodos)]
    
    # Construir grafo a partir de las aristas
    for u, v in aristas:
        grafo[u - 1].append(v - 1)
        grafo[v - 1].append(u - 1)
    
    # Colores: -1 sin colorear, 0 y 1 para los dos colores
    colores = [-1] * nodos
    
    # Función BFS para colorear el grafo
    def bfs(inicio):
        queue = deque([inicio])
        colores[inicio] = 0  # Asignamos el primer color
        
        while queue:
            nodo = queue.popleft()
            color_actual = colores[nodo]
            
            for vecino in grafo[nodo]:
                if colores[vecino] == -1:
                    # Asignar el color contrario al vecino
                    colores[vecino] = 1 - color_actual
                    queue.append(vecino)
                elif colores[vecino] == color_actual:
                    # Si un vecino tiene el mismo color, no es bipartito
                    return False
        return True
    
    # Verificar cada componente del grafo (por si está desconectado)
    for nodo in range(nodos):
        if colores[nodo] == -1:
            if not bfs(nodo):
                return "no bipartito"
    
    return "bipartito"

def procesar_grafos_bipartitos(C, casos):
    resultados = []
    for nodos, aristas in casos:
        resultado = es_bipartito(nodos, aristas)
        resultados.append(resultado)
    return resultados

# Lectura dinámica de la entrada
C = int(input())  # Número de casos de prueba
casos = []

for _ in range(C):
    N, M = map(int, input().split())
    aristas = [tuple(map(int, input().split(", "))) for _ in range(M)]
    casos.append((N, aristas))

# Procesar los casos
resultados = procesar_grafos_bipartitos(C, casos)

# Imprimir los resultados
for resultado in resultados:
    print(resultado)
