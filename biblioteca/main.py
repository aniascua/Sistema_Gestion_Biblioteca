# IMPORTAMOS LAS FUNCIONES Y CLASES NECESARIAS
from utils import cargar_datos, guardar_datos, inicializar_datos  # Funciones para manejar archivos JSON e inicializar datos
from libro import Libro  # Clase para representar libros
from socio import Socio  # Clase para representar socios
from prestamo import Prestamo  # Clase para representar préstamos

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
    print("12. Eliminar Todos los Libros")  # Nueva opción añadida

# 1. Registrar Libro
def registrar_libro():
    """FUNCIÓN PARA REGISTRAR UN NUEVO LIBRO EN EL SISTEMA"""
    titulo = input("Título: ")
    autor = input("Autor: ")
    editorial = input("Editorial: ")
    ano_publicacion = int(input("Año de publicación: "))
    genero = input("Género: ")
    cantidad_disponible = int(input("Cantidad disponible: "))

    libro = Libro(titulo, autor, editorial, ano_publicacion, genero, cantidad_disponible)
    
    libros = cargar_datos('libros.json')
    libros.append(libro.to_dict())
    guardar_datos('libros.json', libros)
    
    print("Libro registrado exitosamente!")

# 2. Editar Libro
def editar_libro():
    """FUNCIÓN PARA EDITAR UN LIBRO EXISTENTE EN EL SISTEMA"""
    id_libro = int(input("ID del libro a editar: "))
    libros = cargar_datos('libros.json')
    libro_encontrado = False

    for libro in libros:
        if libro['id_libro'] == id_libro:
            libro['titulo'] = input(f"Título ({libro['titulo']}): ") or libro['titulo']
            libro['autor'] = input(f"Autor ({libro['autor']}): ") or libro['autor']
            libro['editorial'] = input(f"Editorial ({libro['editorial']}): ") or libro['editorial']
            libro['año_publicacion'] = int(input(f"Año de publicación ({libro['año_publicacion']}): ") or libro['año_publicacion'])
            libro['genero'] = input(f"Género ({libro['genero']}): ") or libro['genero']
            libro['cantidad_disponible'] = int(input(f"Cantidad disponible ({libro['cantidad_disponible']}): ") or libro['cantidad_disponible'])
            libro_encontrado = True
            break

    if libro_encontrado:
        guardar_datos('libros.json', libros)
        print("Libro editado exitosamente!")
    else:
        print("Libro no encontrado.")

# 3. Eliminar Libro
def eliminar_libro():
    """FUNCIÓN PARA ELIMINAR UN LIBRO DEL SISTEMA"""
    id_libro = int(input("ID del libro a eliminar: "))
    libros = cargar_datos('libros.json')
    
    libros = [libro for libro in libros if libro['id_libro'] != id_libro]
    
    guardar_datos('libros.json', libros)
    print("Libro eliminado exitosamente!")

# 4. Registrar Socio
def registrar_socio():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    fecha_nacimiento = input("Fecha de nacimiento (yyyy-mm-dd): ")
    direccion = input("Dirección: ")
    correo_electronico = input("Correo electrónico: ")
    telefono = input("Teléfono: ")

    socio = Socio(nombre, apellido, fecha_nacimiento, direccion, correo_electronico, telefono)
    
    socios = cargar_datos('socios.json')
    socios.append(socio.to_dict())
    guardar_datos('socios.json', socios)
    
    print("Socio registrado exitosamente!")

# 5. Editar Socio
def editar_socio():
    """FUNCIÓN PARA EDITAR UN SOCIO EXISTENTE EN EL SISTEMA"""
    id_socio = input("ID del socio a editar: ")
    socios = cargar_datos('socios.json')
    
    print("Socios cargados desde el archivo:")
    print(socios)  # Agregar esta línea para verificar qué socios se están cargando
    
    socio_encontrado = False

    for socio in socios:
        if socio['id_socio'] == id_socio:
            socio['nombre'] = input(f"Nombre ({socio['nombre']}): ") or socio['nombre']
            socio['apellido'] = input(f"Apellido ({socio['apellido']}): ") or socio['apellido']
            socio['fecha_nacimiento'] = input(f"Fecha de nacimiento ({socio['fecha_nacimiento']}): ") or socio['fecha_nacimiento']
            socio['direccion'] = input(f"Dirección ({socio['direccion']}): ") or socio['direccion']
            socio['correo_electronico'] = input(f"Correo electrónico ({socio['correo_electronico']}): ") or socio['correo_electronico']
            socio['telefono'] = input(f"Teléfono ({socio['telefono']}): ") or socio['telefono']
            socio_encontrado = True
            break

    if socio_encontrado:
        guardar_datos('socios.json', socios)
        print("Socio editado exitosamente!")
    else:
        print("Socio no encontrado.")


# 6. Eliminar Socio
def eliminar_socio():
    listar_socios()  # Mostrar la lista de socios para que el usuario seleccione uno
    id_socio_a_eliminar = input("Ingrese el ID del socio a eliminar: ")

    # Cargar la lista de socios desde el archivo JSON
    socios = cargar_datos('socios.json')
    
    print("Socios cargados desde el archivo:")
    print(socios)  # Añadir esta línea para verificar qué socios se están cargando
    
    # Filtrar y eliminar el socio por su ID
    socios_actualizados = [socio for socio in socios if socio['id_socio'] != id_socio_a_eliminar]
    
    # Guardar los datos actualizados en el archivo JSON
    guardar_datos('socios.json', socios_actualizados)
    
    print(f"Socio con ID {id_socio_a_eliminar} eliminado correctamente.")

# 7. Registrar Préstamo
def registrar_prestamo():
    """FUNCIÓN PARA REGISTRAR UN NUEVO PRÉSTAMO EN EL SISTEMA"""
    id_libro = int(input("ID del libro: "))
    id_socio = int(input("ID del socio: "))
    fecha_prestamo = input("Fecha de préstamo (yyyy-mm-dd): ")

    prestamo = Prestamo(id_libro, id_socio, fecha_prestamo)
    prestamos = cargar_datos('prestamos.json')
    prestamos.append(prestamo.to_dict())
    guardar_datos('prestamos.json', prestamos)

    libros = cargar_datos('libros.json')
    libro_encontrado = False

    for libro in libros:
        if libro['id_libro'] == id_libro:
            if libro['cantidad_disponible'] > 0:
                libro['cantidad_disponible'] -= 1
                guardar_datos('libros.json', libros)
                print("Préstamo registrado exitosamente!")
                libro_encontrado = True
            else:
                print("No hay copias disponibles para préstamo.")
            break

    if not libro_encontrado:
        print("Libro no encontrado.")

# 8. Devolver Libro
def devolver_libro():
    """FUNCIÓN PARA REGISTRAR LA DEVOLUCIÓN DE UN LIBRO"""
    id_prestamo = input("ID del préstamo: ")
    fecha_devolucion = input("Fecha de devolución (yyyy-mm-dd): ")

    prestamos = cargar_datos('prestamos.json')
    prestamo_encontrado = False

    for prestamo in prestamos:
        try:
            if 'id_prestamo' in prestamo and str(prestamo['id_prestamo']) == id_prestamo:
                prestamo['fecha_devolucion'] = fecha_devolucion
                prestamo['estado_prestamo'] = 'Devuelto'  # Añadir estado de préstamo
                guardar_datos('prestamos.json', prestamos)

                id_libro = prestamo['id_libro']
                libros = cargar_datos('libros.json')
                for libro in libros:
                    if libro['id_libro'] == id_libro:
                        libro['cantidad_disponible'] += 1
                        guardar_datos('libros.json', libros)
                        break

                print("Libro devuelto exitosamente.")
                prestamo_encontrado = True
                break
        except KeyError as e:
            print(f"Error: KeyError - {e} en préstamo {prestamo}")

    if not prestamo_encontrado:
        print("Préstamo no encontrado.")

# 9. Listar Libros
def listar_libros():
    """FUNCIÓN PARA LISTAR TODOS LOS LIBROS DISPONIBLES EN EL SISTEMA"""
    libros = cargar_datos('libros.json')
    if libros:
        for libro in libros:
            print(f"ID: {libro['id_libro']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Editorial: {libro['editorial']}, Año: {libro['año_publicacion']}, Género: {libro['genero']}, Disponible: {libro['cantidad_disponible']}")
    else:
        print("No hay libros registrados.")

# 10. Listar Socios
def listar_socios():
    """FUNCIÓN PARA LISTAR TODOS LOS SOCIOS REGISTRADOS EN EL SISTEMA"""
    socios = cargar_datos('socios.json')
    if socios:
        for socio in socios:
            print(f"ID: {socio['id_socio']}, Nombre: {socio['nombre']}, Apellido: {socio['apellido']}, Fecha de nacimiento: {socio['fecha_nacimiento']}, Dirección: {socio['direccion']}, Correo electrónico: {socio['correo_electronico']}, Teléfono: {socio['telefono']}")
    else:
        print("No hay socios registrados.")

# 11. Eliminar Todos los Libros
def eliminar_todos_libros():
    """FUNCIÓN PARA ELIMINAR TODOS LOS LIBROS DEL SISTEMA"""
    libros = []
    guardar_datos('libros.json', libros)
    print("Todos los libros fueron eliminados del sistema.")

# FUNCION PRINCIPAL
def main():
    """FUNCIÓN PRINCIPAL DEL PROGRAMA"""
    inicializar_datos()  # Inicializamos los datos si es necesario
    
    while True:
        mostrar_menu()  # Mostramos el menú principal
        opcion = input("Selecciona una opción: ")

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
            print("Saliendo del sistema... ¡Hasta luego!")
            break
        elif opcion == '12':
            eliminar_todos_libros()
        else:
            print("Opción no válida. Inténtalo nuevamente.")

if __name__ == "__main__":
    main()
