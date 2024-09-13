# Leer el número de palabras N
N = int(input())

# Crear un diccionario para almacenar las palabras en Ewokés y sus traducciones
traductor = {}

# Leer las N líneas con las palabras Ewokés y sus traducciones
for _ in range(N):
    ewokes, castellano = input().split()
    traductor[ewokes] = castellano

# Procesar las consultas hasta encontrar la línea con el carácter '#'
while True:
    consulta = input().strip()
    if consulta == "#":
        break
    # Imprimir la traducción o el mensaje "Entrada no encontrada"
    print(traductor.get(consulta, "Entrada no encontrada"))
