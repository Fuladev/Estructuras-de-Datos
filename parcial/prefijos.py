def encontrar_prefijo_comun(strings):
    if not strings:
        return ""
    
    # Empezamos con el primer string como prefijo inicial
    prefijo = strings[0]
    
    # Iteramos sobre el resto de strings
    for string in strings[1:]:
        # Reducimos el prefijo mientras no sea un prefijo del string actual
        while string[:len(prefijo)] != prefijo and prefijo:
            prefijo = prefijo[:-1]  # Eliminamos el último carácter del prefijo
    
    return prefijo

# Ejemplo de uso
n = int(input())
strings = [input().strip() for _ in range(n)]
resultado = encontrar_prefijo_comun(strings)
print(resultado)
