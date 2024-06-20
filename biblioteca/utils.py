import os
import json

# Obtener el directorio base absoluto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def cargar_datos(ruta_relativa):
    ruta_absoluta = os.path.join(BASE_DIR, ruta_relativa)
    try:
        with open(ruta_absoluta, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_datos(ruta_relativa, datos):
    ruta_absoluta = os.path.join(BASE_DIR, ruta_relativa)
    with open(ruta_absoluta, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

def inicializar_datos():
    libros = cargar_datos('../data/libros.json')
    socios = cargar_datos('../data/socios.json')
    prestamos = cargar_datos('../data/prestamos.json')
    return libros, socios, prestamos
