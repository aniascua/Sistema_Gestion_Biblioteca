# IMPORTAMOS LAS FUNCIONES Y CLASES NECESARIAS
from utils import cargar_datos, guardar_datos, inicializar_datos  # Funciones para manejar archivos JSON e inicializar datos
from libro import Libro  # Clase para representar libros
from socio import Socio  # Clase para representar socios
import os  # Módulo para funciones relacionadas con el sistema operativo

def mostrar_menu():
    """FUNCIÓN PARA MOSTRAR EL MENÚ PRINCIPAL"""
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

class Prestamo:
    contador_id = 0

    def __init__(self, id_libro, id_socio, fecha_prestamo, fecha_devolucion=None):
        Prestamo.contador_id += 1
        self.id_prestamo = Prestamo.contador_id
        self.id_libro = id_libro
        self.id_socio = id_socio
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def to_dict(self):
        return {
            'id_prestamo': self.id_prestamo,
            'id_libro': self.id_libro,
            'id_socio': self.id_socio,
            'fecha_prestamo': self.fecha_prestamo,
            'fecha_devolucion': self.fecha_devolucion
        }

# 1. Registrar Libro
def registrar_libro():
    """FUNCIÓN PARA REGISTRAR UN NUEVO LIBRO EN EL SISTEMA"""
    id_libro = input("ID del libro: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    editorial = input("Editorial: ")
    ano_publicacion = input("Año de publicación: ")
    genero = input("Género: ")
    cantidad_disponible = int(input("Cantidad disponible: "))

    # CREAMOS OBJETO "LIBRO" CON LOS DATOS PROPORCIONADOS POR EL USUARIO
    libro = Libro(id_libro, titulo, autor, editorial, ano_publicacion, genero, cantidad_disponible)
    
    # CARGAMOS LOS DATOS ACTUALES DE LOS LIBROS DESDE EL ARCHIVO JSON
    libros = cargar_datos('data/libros.json')
    
    # AGREGAMOS EL NUEVO LIBRO A LA LISTA DE LIBROS Y GUARDAMOS LOS DATOS ACTUALIZADOS 
    libros.append(libro.to_dict())
    guardar_datos('data/libros.json', libros)
    
    # MOSTRAMOS POR PANTALLA QUE EL LIBRO SE REGISTRÓ EXITOSAMENTE
    print("Libro registrado exitosamente!")

# 2. Editar Libro
def editar_libro():
    """FUNCION PARA EDITAR UN LIBRO EXISTENTE EN EL SISTEMA"""
    id_libro = input("ID del libro a editar: ")
    libros = cargar_datos('data/libros.json')
    libro_encontrado = False

    for libro in libros:
        if libro['id_libro'] == id_libro:
            # MOSTRAMOS LOS DATOS ACTUALES DEL LIBRO Y LE PERMITIMOS AL USUARIO EDITARLOS
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

# 3. Eliminar Libro
def eliminar_libro():
    """FUNCION PARA ELIMINAR UN LIBRO"""
    id_libro = input("ID del libro a eliminar: ")
    libros = cargar_datos('data/libros.json')
    
    # FILTRAMOS LOS LIBROS PARA EXCLUIR EL LIBRO CON EL ID ESPECIFICADO
    libros = [libro for libro in libros if libro['id_libro'] != id_libro]
    
    # GUARDAMOS LOS DATOS ACTUALIZADOS EN EL ARCHIVO JSON
    guardar_datos('data/libros.json', libros)
    print("Libro eliminado exitosamente!")

# 4. Registrar Socio
def registrar_socio():
    """FUNCION PARA REGISTRAR UN NUEVO SOCIO EN EL SISTEMA"""
    id_socio = input("ID del socio: ")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")

    # CREAMOS OBJETO "SOCIO" CON LOS DATOS PROPORCIONADOS POR EL USUARIO
    socio = Socio(id_socio, nombre, direccion, telefono)
    
    # CARGAMOS LOS DATOS ACTUALES DE LOS SOCIOS DESDE EL ARCHIVO JSON
    socios = cargar_datos('data/socios.json')
    
    # AGREGAMOS EL SOCIO NUEVO A LA LISTA DE SOCIOS Y GUARDAMOS LOS DATOS ACTUALIZADOS
    socios.append(socio.to_dict())
    guardar_datos('data/socios.json', socios)
    
    # MOSTRAMOS POR PANTALLA QUE EL SOCIO SE REGISTRÓ EXITOSAMENTE
    print("Socio registrado exitosamente!")

# 5. Editar Socio
def editar_socio():
    """FUNCION PARA EDITAR UN SOCIO EXISTENTE EN EL SISTEMA"""
    id_socio = input("ID del socio a editar: ")
    socios = cargar_datos('data/socios.json')
    socio_encontrado = False

    for socio in socios:
        if socio['id_socio'] == id_socio:
            # MOSTRAMOS LOS DATOS DEL SOCIO Y LE PERMITIMOS AL USUARIO EDITARLOS
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
        print("Socio no encontrado.")

# 6. Eliminar Socio
def eliminar_socio():
    """FUNCION PARA ELIMINAR UN SOCIO DEL SISTEMA"""
    id_socio = input("ID del socio a eliminar: ")
    socios = cargar_datos('data/socios.json')
    
    # FILTRAMOS LOS SOCIOS PARA EXCLUIR EL SOCIO CON EL ID ESPECIFICADO 
    socios = [socio for socio in socios if socio['id_socio'] != id_socio]
    
    # GUARDAMOS LOS DATOS ACTUALIZADOS DE LOS SOCIOS EN EL ARCHIVO JSON
    guardar_datos('data/socios.json', socios)
    print("Socio eliminado exitosamente!")

# 7. Registrar Préstamo
def registrar_prestamo():
    """FUNCION PARA REGISTRAR UN NUEVO PRÉSTAMO EN EL SISTEMA"""
    id_prestamo = input("ID del préstamo: ")
    id_libro = input("ID del libro: ")
    id_socio = input("ID del socio: ")
    fecha_prestamo = input("Fecha de préstamo (dd-mm-aaaa): ")

    # CARGAMOS LOS LIBROS DESDE EL ARCHIVO JSON
    libros = cargar_datos('data/libros.json')
    libro_encontrado = False

    # BUSCAMOS EL LIBRO POR SU ID
    for libro in libros:
        if libro['id_libro'] == id_libro:
            if libro['cantidad_disponible'] > 0:
                # CREAMOS EL OBJETO Prestamo
                prestamo = Prestamo(id_prestamo, id_libro, id_socio, fecha_prestamo)
                # CARGAMOS LOS DATOS ACTUALES DE LOS PRÉSTAMOS DESDE EL ARCHIVO JSON
                prestamos = cargar_datos('data/prestamos.json')
                # AGREGAMOS EL NUEVO PRÉSTAMO A LA LISTA DE PRÉSTAMOS Y GUARDAMOS LOS DATOS ACTUALIZADOS
                prestamos.append(prestamo.to_dict())
                guardar_datos('data/prestamos.json', prestamos)
                
                # ACTUALIZAMOS LA CANTIDAD DISPONIBLE DEL LIBRO
                libro['cantidad_disponible'] -= 1
                guardar_datos('data/libros.json', libros)
                
                print("Préstamo registrado exitosamente!")
                libro_encontrado = True
            else:
                print("No hay copias disponibles para préstamo.")
            break

    if not libro_encontrado:
        print("Libro no encontrado.")

# 8. Devolver Libro
def devolver_libro():
    """FUNCION PARA REGISTRAR LA DEVOLUCIÓN DE UN LIBRO"""
    id_prestamo = input("ID del préstamo: ")
    fecha_devolucion = input("Fecha de devolución (dd-mm-aaaa): ")

    # CARGAMOS LOS DATOS ACTUALES DE LOS PRÉSTAMOS DESDE EL ARCHIVO JSON
    prestamos = cargar_datos('data/prestamos.json')
    prestamo_encontrado = False

    for prestamo in prestamos:
        if prestamo['id_prestamo'] == id_prestamo:
            prestamo['fecha_devolucion'] = fecha_devolucion
            prestamo_encontrado = True
            break

    if prestamo_encontrado:
        # ACTUALIZAMOS LOS DATOS DE LOS PRÉSTAMOS
        guardar_datos('data/prestamos.json', prestamos)

        # ACTUALIZAMOS LA CANTIDAD DISPONIBLE DEL LIBRO DEVUELTO
        id_libro = prestamo['id_libro']
        libros = cargar_datos('data/libros.json')
        for libro in libros:
            if libro['id_libro'] == id_libro:
                libro['cantidad_disponible'] += 1
                break

        guardar_datos('data/libros.json', libros)
        print("Libro devuelto exitosamente!")
    else:
        print("Préstamo no encontrado...")

# 9. Listar Libros
def listar_libros():
    """FUNCIÓN PARA LISTAR TODOS LOS LIBROS DISPONIBLES EN EL SISTEMA"""
    libros = cargar_datos('data/libros.json')
    if libros:
        for libro in libros:
            print(f"ID: {libro['id_libro']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Editorial: {libro['editorial']}, Año: {libro['ano_publicacion']}, Género: {libro['genero']}, Disponible: {libro['cantidad_disponible']}")
    else:
        print("No hay libros registrados.")

# 10. Listar Socios
def listar_socios():
    """FUNCIÓN PARA LISTAR TODOS LOS SOCIOS REGISTRADOS EN EL SISTEMA"""
    socios = cargar_datos('data/socios.json')
    if socios:
        for socio in socios:
            print(f"ID: {socio['id_socio']}, Nombre: {socio['nombre']}, Dirección: {socio['direccion']}, Teléfono: {socio['telefono']}")
    else:
        print("No hay socios registrados.")

# FUNCION PRINCIPAL
def main():
    """FUNCIÓN PRINCIPAL DEL PROGRAMA"""
    inicializar_datos()  # INICIALIZAMOS DATOS (SI ES NECESARIO)
    while True:
        mostrar_menu()  # MOSTRAMOS EL MENÚ PRINCIPAL
        opcion = input("Seleccioná una opción: ")

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
            print("Opción no válida. Intente nuevamente...")

if __name__ == "__main__":
    main()