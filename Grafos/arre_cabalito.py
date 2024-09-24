from collections import deque

# Movimientos posibles del caballo
movimientos = [(2, 1), (2, -1), (-2, 1), (-2, -1),
               (1, 2), (1, -2), (-1, 2), (-1, -2)]

# Función para convertir una celda de ajedrez como "A1" a índices de matriz
def convertir_celda(celda):
    columna = ord(celda[0]) - ord('A')
    fila = int(celda[1]) - 1
    return (fila, columna)

# Función para determinar la cantidad mínima de movimientos usando BFS
def min_movimientos(inicio, destino):
    if inicio == destino:
        return 0
    
    # Cola para la BFS
    cola = deque([inicio])
    visitado = [[False] * 8 for _ in range(8)]
    distancias = [[0] * 8 for _ in range(8)]
    
    visitado[inicio[0]][inicio[1]] = True
    
    while cola:
        x, y = cola.popleft()
        
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < 8 and 0 <= ny < 8 and not visitado[nx][ny]:
                visitado[nx][ny] = True
                distancias[nx][ny] = distancias[x][y] + 1
                cola.append((nx, ny))
                
                # Si llegamos a la celda destino, retornamos la distancia
                if (nx, ny) == destino:
                    return distancias[nx][ny]
    
    return -1  # Este caso no debería ocurrir en un tablero válido

# Leer el número de casos de prueba
C = int(input())

for _ in range(C):
    # Leer las celdas de inicio y destino
    inicio, destino = input().split()
    
    # Convertir las celdas a índices de matriz
    inicio = convertir_celda(inicio)
    destino = convertir_celda(destino)
    
    # Calcular la cantidad mínima de movimientos
    resultado = min_movimientos(inicio, destino)
    
    # Imprimir el resultado
    print(resultado)
