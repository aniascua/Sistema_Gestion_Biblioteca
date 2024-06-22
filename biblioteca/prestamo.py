def registrar_prestamo():
    id_prestamo = input("ID del préstamo: ")
    id_libro = input("ID del libro: ")
    id_socio = input("ID del socio: ")
    fecha_prestamo = input("Fecha de préstamo (dd-mm-aaaa): ")

    libros = cargar_datos('data/libros.json')
    libro_encontrado = False

    for libro in libros:
        if libro['id_libro'] == id_libro:
            if libro['cantidad_disponible'] > 0:
                prestamo = Prestamo(id_prestamo, id_libro, id_socio, fecha_prestamo)
                prestamos = cargar_datos('data/prestamos.json')
                prestamos.append(prestamo.to_dict())
                guardar_datos('data/prestamos.json', prestamos)

                libro['cantidad_disponible'] -= 1
                guardar_datos('data/libros.json', libros)

                print(f"Préstamo registrado exitosamente. Cantidad disponible de {libro['titulo']}: {libro['cantidad_disponible']}")
                libro_encontrado = True
            else:
                print("No hay copias disponibles para prestar.")
            break

    if not libro_encontrado:
        print("Libro no encontrado.")
