from utils import cargar_datos, guardar_datos, inicializar_datos
from libro import Libro
from socio import Socio
from prestamo import Prestamo
import os

def mostrar_menu():
    print("\n--- Sistema de Gestión de Biblioteca ---")
    print("1. Registrar Libro")
    print("2. Editar Libro")
    print("3. Eliminar Libro")
    print("4. Registrar Socio")
    print("5. Editar Socio")
    print("6. Eliminar Socio")
    print("7. Registrar Préstamo")
    print("8. Devolver Libro")
    print("9. Listar Libros")
    print("10. Listar Socios")
    print("11. Salir")

def registrar_libro():
    id_libro = input("ID del libro: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    editorial = input("Editorial: ")
    ano_publicacion = input("Año de publicación: ")
    genero = input("Género: ")
    cantidad_disponible = int(input("Cantidad disponible: "))

    libro = Libro(id_libro, titulo, autor, editorial, ano_publicacion, genero, cantidad_disponible)
    libros = cargar_datos('data/libros.json')
    libros.append(libro.to_dict())
    guardar_datos('data/libros.json', libros)
    print("Libro registrado exitosamente.")

def editar_libro():
    id_libro = input("ID del libro a editar: ")
    libros = cargar_datos('data/libros.json')
    libro_encontrado = False

    for libro in libros:
        if libro['id_libro'] == id_libro:
            libro['titulo'] = input(f"Título ({libro['titulo']}): ") or libro['titulo']
            libro['autor'] = input(f"Autor ({libro['autor']}): ") or libro['autor']
            libro['editorial'] = input(f"Editorial ({libro['editorial']}): ") or libro['editorial']
            libro['ano_publicacion'] = input(f"Año de publicación ({libro['ano_publicacion']}): ") or libro['ano_publicacion']
            libro['genero'] = input(f"Género ({libro['genero']}): ") or libro['genero']
            libro['cantidad_disponible'] = int(input(f"Cantidad disponible ({libro['cantidad_disponible']}): ") or libro['cantidad_disponible'])
            libro_encontrado = True
            break

    if libro_encontrado:
        guardar_datos('data/libros.json', libros)
        print("Libro editado exitosamente.")
    else:
        print("Libro no encontrado.")

def eliminar_libro():
    id_libro = input("ID del libro a eliminar: ")
    libros = cargar_datos('data/libros.json')
    libros = [libro for libro in libros if libro['id_libro'] != id_libro]
    guardar_datos('data/libros.json', libros)
    print("Libro eliminado exitosamente.")

def registrar_socio():
    id_socio = input("ID del socio: ")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")

    socio = Socio(id_socio, nombre, direccion, telefono)
    socios = cargar_datos('data/socios.json')
    socios.append(socio.to_dict())
    guardar_datos('data/socios.json', socios)
    print("Socio registrado exitosamente.")

def editar_socio():
    id_socio = input("ID del socio a editar: ")
    socios = cargar_datos('data/socios.json')
    socio_encontrado = False

    for socio in socios:
        if socio['id_socio'] == id_socio:
            socio['nombre'] = input(f"Nombre ({socio['nombre']}): ") or socio['nombre']
            socio['direccion'] = input(f"Dirección ({socio['direccion']}): ") or socio['direccion']
            socio['telefono'] = input(f"Teléfono ({socio['telefono']}): ") or socio['telefono']
            socio_encontrado = True
            break

    if socio_encontrado:
        guardar_datos('data/socios.json', socios)
        print("Socio editado exitosamente.")
    else:
        print("Socio no encontrado.")

def eliminar_socio():
    id_socio = input("ID del socio a eliminar: ")
    socios = cargar_datos('data/socios.json')
    socios = [socio for socio in socios if socio['id_socio'] != id_socio]
    guardar_datos('data/socios.json', socios)
    print("Socio eliminado exitosamente.")

def registrar_prestamo():
    id_prestamo = input("ID del préstamo: ")
    id_libro = input("ID del libro: ")
    id_socio = input("ID del socio: ")
    fecha_prestamo = input("Fecha de préstamo: ")

    prestamo = Prestamo(id_prestamo, id_libro, id_socio, fecha_prestamo)
    prestamos = cargar_datos('data/prestamos.json')
    prestamos.append(prestamo.to_dict())
    guardar_datos('data/prestamos.json', prestamos)
    print("Préstamo registrado exitosamente.")

def devolver_libro():
    id_prestamo = input("ID del préstamo: ")
    fecha_devolucion = input("Fecha de devolución: ")
    prestamos = cargar_datos('data/prestamos.json')
    prestamo_encontrado = False

    for prestamo in prestamos:
        if prestamo['id_prestamo'] == id_prestamo:
            prestamo['fecha_devolucion'] = fecha_devolucion
            prestamo_encontrado = True
            break

    if prestamo_encontrado:
        guardar_datos('data/prestamos.json', prestamos)
        print("Libro devuelto exitosamente.")
    else:
        print("Préstamo no encontrado.")

def listar_libros():
    libros = cargar_datos('data/libros.json')
    print("\n--- Lista de Libros ---")
    for libro in libros:
        print(f"ID: {libro['id_libro']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Editorial: {libro['editorial']}, Año: {libro['ano_publicacion']}, Género: {libro['genero']}, Cantidad disponible: {libro['cantidad_disponible']}")

def listar_socios():
    socios = cargar_datos('data/socios.json')
    print("\n--- Lista de Socios ---")
    for socio in socios:
        print(f"ID: {socio['id_socio']}, Nombre: {socio['nombre']}, Dirección: {socio['direccion']}, Teléfono: {socio['telefono']}")

def main():
    libros, socios, prestamos = inicializar_datos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_libro()
        elif opcion == '2':
            editar_libro()
        elif opcion == '3':
            eliminar_libro()
        elif opcion == '4':
            registrar_socio()
        elif opcion == '5':
            editar_socio()
        elif opcion == '6':
            eliminar_socio()
        elif opcion == '7':
            registrar_prestamo()
        elif opcion == '8':
            devolver_libro()
        elif opcion == '9':
            listar_libros()
        elif opcion == '10':
            listar_socios()
        elif opcion == '11':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
