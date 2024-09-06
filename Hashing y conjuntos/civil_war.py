def separacion_civilizada():
    # Conjuntos para almacenar los libros de Fernando y Gustavo
    libros_fernando = set()
    libros_gustavo = set()
    
    while True:
        # Leer la entrada
        entrada = input().strip()
        
        # Si la entrada es "0", terminamos
        if entrada == "0":
            break
        
        # Obtener el ISBN y el comprador
        isbn, comprador = entrada.split()
        isbn = int(isbn)
        
        if comprador == "F":
            # Si Gustavo ya tiene el libro, lo eliminamos de su conjunto y resolvemos la asignación
            if isbn in libros_gustavo:
                libros_gustavo.remove(isbn)
                if isbn % 2 == 0:
                    libros_fernando.add(isbn)
                else:
                    libros_gustavo.add(isbn)
            else:
                libros_fernando.add(isbn)
        
        elif comprador == "G":
            # Si Fernando ya tiene el libro, lo eliminamos de su conjunto y resolvemos la asignación
            if isbn in libros_fernando:
                libros_fernando.remove(isbn)
                if isbn % 2 == 0:
                    libros_fernando.add(isbn)
                else:
                    libros_gustavo.add(isbn)
            else:
                libros_gustavo.add(isbn)
    
    # Contar los libros finales de cada quien
    print(len(libros_fernando), len(libros_gustavo))

# Ejecutar la función
separacion_civilizada()
