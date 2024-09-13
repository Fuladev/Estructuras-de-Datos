# Leer todas las palabras de la entrada
palabras = []
while True:
    palabra = input().strip()
    if palabra == '#':
        break
    palabras.append(palabra)

# Convertir la lista de palabras en un conjunto para búsqueda rápida
palabras_set = set(palabras)

# Lista para almacenar las palabras compuestas
compuestas = []

# Revisar cada palabra del diccionario
for palabra in palabras:
    # Intentar dividir la palabra en dos partes
    for i in range(1, len(palabra)):
        parte1 = palabra[:i]
        parte2 = palabra[i:]
        # Verificar si ambas partes están en el conjunto de palabras
        if parte1 in palabras_set and parte2 in palabras_set:
            compuestas.append(f"{palabra} = {parte1} + {parte2}")

# Imprimir las palabras compuestas encontradas
for compuesta in compuestas:
    print(compuesta)
