def criba_eratostenes(max_n):
    # Inicializar un array para marcar los primos
    es_primo = [True] * (max_n + 1)
    es_primo[0] = es_primo[1] = False  # 0 y 1 no son primos

    # Aplicar la criba
    for i in range(2, int(max_n**0.5) + 1):
        if es_primo[i]:
            for j in range(i * i, max_n + 1, i):
                es_primo[j] = False
    
    # Crear la lista de números primos
    primos = [i for i in range(2, max_n + 1) if es_primo[i]]
    return primos, es_primo

def contar_parejas_goldbach(n, primos, es_primo):
    conteo = 0
    for p1 in primos:
        if p1 > n // 2:
            break
        if es_primo[n - p1]:
            conteo += 1
    return conteo

def main():
    # Leer la cantidad de casos de prueba
    C = int(input())
    
    # Leer todos los números para los que se pide la solución
    casos = [int(input()) for _ in range(C)]
    
    # Preprocesar los primos hasta el máximo número posible en los casos
    max_n = max(casos)
    primos, es_primo = criba_eratostenes(max_n)
    
    # Para cada caso, calcular la cantidad de parejas
    for n in casos:
        print(contar_parejas_goldbach(n, primos, es_primo))

# Ejecutar la función principal
if __name__ == "__main__":
    main()
