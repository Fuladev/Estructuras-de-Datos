from collections import defaultdict

# Diccionarios para almacenar los votos y el estado de cada votante
votos_candidatos = defaultdict(int)
votos_votantes = {}
votantes_anulados = set()

# Procesar la entrada
while True:
    votante, candidato = map(int, input().split())
    
    if votante == 0 and candidato == 0:
        break

    # Si el votante ya ha sido anulado, ignorar
    if votante in votantes_anulados:
        continue
    
    # Si el votante ya ha votado, anular todos sus votos
    if votante in votos_votantes:
        votos_candidatos[votos_votantes[votante]] -= 1
        votantes_anulados.add(votante)
        del votos_votantes[votante]
    else:
        # Si es la primera vez que vota, almacenar su voto
        votos_votantes[votante] = candidato
        votos_candidatos[candidato] += 1

# Filtrar los candidatos que han recibido al menos un voto
resultado = [(candidato, votos) for candidato, votos in votos_candidatos.items() if votos > 0]

# Ordenar según los criterios: descendentemente por cantidad de votos y luego por documento
resultado.sort(key=lambda x: (-x[1], -x[0]))

# Imprimir los resultados
for candidato, votos in resultado:
    print(f"{candidato} {votos}")
