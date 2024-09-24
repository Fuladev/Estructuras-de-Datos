class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Union by size
            if self.size[rootX] < self.size[rootY]:
                rootX, rootY = rootY, rootX
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
    
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1

def procesar_juego_de_tronos(C, casos):
    resultados = []
    
    for r, relaciones in casos:
        uf = UnionFind()
        
        # Procesar las relaciones de parentesco
        for a, b in relaciones:
            uf.add(a)
            uf.add(b)
            uf.union(a, b)
        
        # Contar las familias y encontrar la familia más grande
        familias = set(uf.find(x) for x in uf.parent)  # Todas las raíces distintas
        tamano_max_familia = max(uf.size[uf.find(x)] for x in uf.parent)
        
        resultados.append(f"{len(familias)} {tamano_max_familia}")
    
    return resultados

# Lectura dinámica de la entrada
C = int(input())  # Número de casos de prueba
casos = []

for _ in range(C):
    R = int(input())  # Número de relaciones de parentesco
    relaciones = [tuple(map(int, input().split())) for _ in range(R)]
    casos.append((R, relaciones))

# Procesar los casos
resultados = procesar_juego_de_tronos(C, casos)

# Imprimir los resultados
for resultado in resultados:
    print(resultado)
