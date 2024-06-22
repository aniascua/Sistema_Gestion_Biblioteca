# IMPORTAMOS LAS FUNCIONES Y CLASES 
from utils import cargar_datos, guardar_datos, inicializar_datos  # Funciones para manejar archivos JSON e inicializar datos
from libro import Libro  # Clase para representar libros
from socio import Socio  # Clase para representar socios
from prestamo import Prestamo  # Clase para representar préstamos
import os  # Módulo para funciones relacionadas con el sistema operativo

def mostrar_menu():
    """FUNCIÓN PARA MOSTRAR EL MENÚ PRINCIPAL...."""
    print("\n*** Sistema de Gestión de Biblioteca ***")
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
    print("11. Salir...")

def registrar_libro():
    """FUNCIÓN PARA REGISTRAR UN NUEVO LIBRO EN EL SISTEMA..."""
    id_libro = input("ID del libro: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    editorial = input("Editorial: ")
    ano_publicacion = input("Año de publicación: ")
    genero = input("Género: ")
    cantidad_disponible = int(input("Cantidad disponible: "))

    # CREAMOS OBJETO "LIBRO" CON LOS DATOS PROPORCIONADOS POR EL USUARIO
    libro = Libro(id_libro, titulo, autor, editorial, ano_publicacion, genero, cantidad_disponible)
    
    # SE CARGAN LOS DATOS ACTUALES DE LOS LIBROS DESDE EL ARCHIVO JSON
    libros = cargar_datos('data/libros.json')
    
    # AGREGAMOS EL NUEVO LIBRO A LA LISTA DE LIBROS Y GUARDAMOS LOS DATOS ACTUALIZADOS 
    libros.append(libro.to_dict())
    guardar_datos('data/libros.json', libros)
    # MOSTRAMOS POR PANTALLA QUE EL LIBRO SE REGISTRÓ EXITOSAMENTE
    print("Libro registrado exitosamente!")

def editar_libro():
    """Función para editar un libro existente en el sistema"""
    id_libro = input("ID del libro a editar: ")
    libros = cargar_datos('data/libros.json')
    libro_encontrado = False

    for libro in libros:
        if libro['id_libro'] == id_libro:
            # MOSTRAMOS LOS DATOS ACTUALES DEL LIBRO Y LE PERMITIMOS AL USER EDITARLOS
            libro['titulo'] = input(f"Título ({libro['titulo']}): ") or libro['titulo']
            libro['autor'] = input(f"Autor ({libro['autor']}): ") or libro['autor']
            libro['editorial'] = input(f"Editorial ({libro['editorial']}): ") or libro['editorial']
            libro['ano_publicacion'] = input(f"Año de publicación ({libro['ano_publicacion']}): ") or libro['ano_publicacion']
            libro['genero'] = input(f"Género ({libro['genero']}): ") or libro['genero']
            libro['cantidad_disponible'] = int(input(f"Cantidad disponible ({libro['cantidad_disponible']}): ") or libro['cantidad_disponible'])
            libro_encontrado = True
            break

    if libro_encontrado:
        # GUARDAMOS LOS DATOS ACTUALIZADOS EN EL ARCHIVO JSON
        guardar_datos('data/libros.json', libros)
        print("Libro editado exitosamente!")
    else:
        print("Libro no encontrado.")

def eliminar_libro():
    """Función para eliminar un libro"""
    id_libro = input("ID del libro a eliminar: ")
    libros = cargar_datos('data/libros.json')
    
    # FILTRAMOS LOS LIBROS PARA EXCLUIR EL LIBRO CON EL ID ESPECIFICADO
    libros = [libro for libro in libros if libro['id_libro'] != id_libro]
    
    # GUARDAMOS LOS DATOS ACTUALIZADOS EN EL ARCHIVO JSON
    guardar_datos('data/libros.json', libros)
    print("Libro eliminado exitosamente!")

def registrar_socio():
    """Función para registrar un nuevo socio en el sistema"""
    id_socio = input("ID del socio: ")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")

    # CREAMOS OBJETO "SOCIO" CON LOS DATOS PROPORCIONADOS POR EL USER
    socio = Socio(id_socio, nombre, direccion, telefono)
    
    # CARGAMOS LOS DATOS ACTUALES DE LOS SOCIOS DESDE EL ARCHIVO JSON
    socios = cargar_datos('data/socios.json')
    
    # AGREGAMOS EL SOCIO NUEVO A LA LISTA DE SOCIOS Y GUARDAMOS LOS DATOS ACTUALIZADOS
    socios.append(socio.to_dict())
    guardar_datos('data/socios.json', socios)
    
    print("Socio registrado exitosamente!")

def editar_socio():
    """Función para editar un socio existente en el sistema."""
    id_socio = input("ID del socio a editar: ")
    socios = cargar_datos('data/socios.json')
    socio_encontrado = False

    for socio in socios:
        if socio['id_socio'] == id_socio:
            # MOSTRAMOS LOS DATOS DEL SOCIO Y LE PERMITIMOS AL USER EDITARLOS
            socio['nombre'] = input(f"Nombre ({socio['nombre']}): ") or socio['nombre']
            socio['direccion'] = input(f"Dirección ({socio['direccion']}): ") or socio['direccion']
            socio['telefono'] = input(f"Teléfono ({socio['telefono']}): ") or socio['telefono']
            socio_encontrado = True
            break

    if socio_encontrado:
        # GUARDAMOS LOS DATOS ACTUALIZADOS DE LOS SOCIOS EN EL ARCHIVO JSON 
        guardar_datos('data/socios.json', socios)
        print("Socio editado exitosamente!")
    else:
        print("Socio no encontrado...")

def eliminar_socio():
    """Función para eliminar un socio del sistema"""
    id_socio = input("ID del socio a eliminar: ")
    socios = cargar_datos('data/socios.json')
    
    # FILTRAMOS LOS SOCIOS PARA EXCLUIR EL SOCIO CON EL ID ESPECIFICADO 
    socios = [socio for socio in socios if socio['id_socio'] != id_socio]
    
    # GUARDAMOS LOS DATOS ACTUALIZADOS DE LOS SOCIOS EN EL ARCHIVO JSON
    guardar_datos('data/socios.json', socios)
    print("Socio eliminado exitosamente!")

def registrar_prestamo():
    """Función para registrar un nuevo préstamo en el sistema"""
    id_prestamo = input("ID del préstamo: ")
    id_libro = input("ID del libro: ")
    id_socio = input("ID del socio: ")
    fecha_prestamo = input("Fecha de préstamo: (dd-mm-aaaa) ")

    # CREAMOS OBJETO "PRESTAMO" CON LOS DATOS PROPORCIONADOS POR EL USER
    prestamo = Prestamo(id_prestamo, id_libro, id_socio, fecha_prestamo)
    
    # CARGAMOS LOS DATOS ACTUALES DE PRÉSTAMOS DESDE EL ARCHIVO JSON
    prestamos = cargar_datos('data/prestamos.json')
    
    # AGREGAMOS EL NUEVO PRÉSTAMO A LA LISTA DE PRÉSTAMOS Y GUARDAMOS LOS DATOS ACTUALIZADOS
    prestamos.append(prestamo.to_dict())
    guardar_datos('data/prestamos.json', prestamos)
    
    print("Préstamo registrado exitosamente!")

def devolver_libro():
    """Función para registrar la devolución de un libro prestado"""
    id_prestamo = input("ID del préstamo: ")
    fecha_devolucion = input("Fecha de devolución: (dd-mm-aaaa)")
    prestamos = cargar_datos('data/prestamos.json')
    prestamo_encontrado = False

    for prestamo in prestamos:
        if prestamo['id_prestamo'] == id_prestamo:
            # ACTUALIZAMOS LA FECHA DE DEVOLUCIÓN DEL PRÉSTAMO ENCONTRADO
            prestamo['fecha_devolucion'] = fecha_devolucion
            prestamo_encontrado = True
            break

    if prestamo_encontrado:
        # GUARDAMOS LOS DATOS ACTUALIZADOS DE PRÉSTAMOS EN EL ARCHIVO JSON
        guardar_datos('data/prestamos.json', prestamos)
        print("Libro devuelto exitosamente!")
    else:
        print("Préstamo no encontrado....")

def listar_libros():
    """Función para listar todos los libros registrados en el sistema"""
    libros = cargar_datos('data/libros.json')
    print("\n--- Lista de Libros ---")
    for libro in libros:
        # MOSTRAMOS INFORMACIÓN DE CADA LIBRO DE MANERA ESTRUCTURADA
        print(f"ID: {libro['id_libro']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Editorial: {libro['editorial']}, Año: {libro['ano_publicacion']}, Género: {libro['genero']}, Cantidad disponible: {libro['cantidad_disponible']}")

def listar_socios():
    """Función para listar todos los socios registrados en el sistema"""
    socios = cargar_datos('data/socios.json')
    print("\n--- Lista de Socios ---")
    for socio in socios:
        # MOSTRAMOS INFORMACIÓN DE CADA SOCIO DE MANERA ESTRUCTURADA
        print(f"ID: {socio['id_socio']}, Nombre: {socio['nombre']}, Dirección: {socio['direccion']}, Teléfono: {socio['telefono']}")

def main():
    """Función principal que ejecuta el sistema de gestión de biblioteca"""
    libros, socios, prestamos = inicializar_datos()

    while True:
        mostrar_menu()
        opcion = input("Seleccioná una opción: ")

        # SEGÚN LA OPCIÓN SELECCIONADA POR EL USER, SE LLAMA A LA FUNCIÓN CORRESPONDIENTE
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
            print("Saliendo del sistema... Gracias!")
            break
        else:
            print("Opción no válida, por favor intente de nuevo")

if __name__ == "__main__":
    main()