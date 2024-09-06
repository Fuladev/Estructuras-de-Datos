def pokemones():
    felipe_set = set()
    vanesa_set = set()

    while True:
        entrada = input().strip()
        if entrada == '#':
            break
        persona, pokemon = entrada.split()
        pokemon = int(pokemon)

        if persona == 'F':
            felipe_set.add(pokemon)
        elif persona == 'V':
            vanesa_set.add(pokemon)

    # Cantidad de Pokémon diferentes para Felipe, Vanesa y la colección conjunta
    felipe_count = len(felipe_set)
    vanesa_count = len(vanesa_set)
    total_count = len(felipe_set.union(vanesa_set))

    print(f"{felipe_count} {vanesa_count} {total_count}")

# Ejecutar la función
pokemones()