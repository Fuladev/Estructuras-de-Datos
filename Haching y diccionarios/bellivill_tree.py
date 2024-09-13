# Leer la entrada
N, T = map(int, input().split())
A = [int(input()) for _ in range(N)]

# Ordenar el arreglo
A.sort()

# Lista para almacenar las ternas encontradas
ternas = []

# Búsqueda de ternas
for i in range(N):
    # Usar dos punteros: uno al inicio (izquierda) y otro al final (derecha)
    izquierda, derecha = i + 1, N - 1
    while izquierda < derecha:
        suma = A[i] + A[izquierda] + A[derecha]
        if suma == T:
            ternas.append((A[i], A[izquierda], A[derecha]))
            izquierda += 1
            derecha -= 1
        elif suma < T:
            izquierda += 1
        else:
            derecha -= 1

# Verificar si encontramos al menos una terna
if ternas:
    # Imprimir las ternas encontradas, cada una en una línea
    for terna in ternas:
        print(terna[0], terna[1], terna[2])
else:
    print("No hay trillizas")
