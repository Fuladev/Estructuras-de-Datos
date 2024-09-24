# Función para realizar DFS en el mapa y contar el tamaño del área contigua
def dfs(mapa, visitado, i, j, A, B):
    # Definir las 4 direcciones de movimiento (arriba, abajo, izquierda, derecha)
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Pila para DFS
    pila = [(i, j)]
    visitado[i][j] = True
    area = 0
    
    while pila:
        x, y = pila.pop()
        area += 1
        
        # Revisar las 4 direcciones
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if 0 <= nx < A and 0 <= ny < B and not visitado[nx][ny] and mapa[nx][ny] == 'X':
                visitado[nx][ny] = True
                pila.append((nx, ny))
    
    return area

# Función para procesar cada caso de prueba
def mayor_area_deforestada(A, B, mapa):
    visitado = [[False] * B for _ in range(A)]
    mayor_area = 0
    
    for i in range(A):
        for j in range(B):
            if mapa[i][j] == 'X' and not visitado[i][j]:
                # Encontrar el área contigua deforestada usando DFS
                area_actual = dfs(mapa, visitado, i, j, A, B)
                mayor_area = max(mayor_area, area_actual)
    
    return mayor_area

# Entrada dinámica de datos
C = int(input())  # Número de casos de prueba

for _ in range(C):
    # Leer A y B
    A, B = map(int, input().split())
    # Leer el mapa
    mapa = [input().strip() for _ in range(A)]
    
    # Calcular y mostrar la mayor área deforestada
    print(mayor_area_deforestada(A, B, mapa))
