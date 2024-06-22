# Trabajo Final Integrador de Programación 1 - UNER - TUDW

## Sistema de Gestión de Bibliotecas en Python con Visual Studio Code

Este proyecto es mi trabajo final integrador del primer semestre de Programación 1 en la UNER - Tecnicatura Universitaria en Desarrollo Web (2024).
Entre las 2 opciones, elegí desarrollar una solución de software para gestionar el préstamo y devolución de libros en una biblioteca utilizando Python y sus extensiones en Visual Studio Code.

### Objetivo

Desarrollar una aplicación de usuarios para gestionar el préstamo y devolución de libros en una biblioteca, permitiendo a los usuarios registrarse, eliminar su registro, solicitar préstamos de libros y devolverlos. 
Todo esto se realiza a través de un menú que se actualiza según las acciones que realiza el usuario. Cada usuario y libro tiene un ID único para identificación

### Requerimientos del Trabajo Final Integrador TUDW 2024:

1. **Registro de Libros:**
   - ID de Libro (número único y autoincremental)
   - Título
   - Autor
   - Editorial
   - Año de Publicación
   - Género
   - Cantidad Disponible

2. **Gestión de Socios:**
   - ID de Socio (número único y autoincremental)
   - Nombre
   - Apellido
   - Fecha de Nacimiento
   - Dirección
   - Correo Electrónico
   - Teléfono

3. **Registro de Préstamos y Devoluciones:**
   - ID de Préstamo (número único y autoincremental)
   - ID de Socio
   - ID de Libro
   - Fecha de Préstamo
   - Costo (en caso de que lo hubiera)
   - Fecha de Devolución
   - Estado del Préstamo (En Curso/Devuelto)

### Características del Software

- **Almacenamiento de Información:** Utilización de archivos JSON para almacenar los datos solicitados.
- **Interfaces de Usuario Interactivas:** 
Permiten:
  - Registrar, editar y eliminar libros.
  - Registrar, editar y eliminar socios.
  - Registrar préstamos y devoluciones.
  - Búsqueda de libros por título, género, autor y editorial.
  - Generar reportes de préstamos y devoluciones por socio, libro y rango de fechas.

### Funcionalidad Extra

Como parte del trabajo final, se incluye una funcionalidad extra del software a criterio del alumno/grupo. Esto puede incluir el desarrollo de una interfaz gráfica, consumo de una API externa, implementación de búsquedas avanzadas, o cualquier otra funcionalidad que aporte valor agregado al sistema.

## Uso del Sistema

Para ejecutar el sistema en tu entorno local, sigue estos pasos:

1. Clona el repositorio desde GitHub: (terminar esta parte)

