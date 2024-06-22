class Libro:  # Creamos una clase Libro
    contador_id = 0  # Variable static para contar los IDs (INICIALIZA EN 0)

    def __init__(self, titulo, autor, editorial, ano_publicacion, genero, cantidad_disponible):
        # Método constructor para inicializar una nueva instancia de Libro
        Libro.contador_id += 1  # Incrementa el contador de IDs de 1 en 1 
        self.id_libro = str(Libro.contador_id)  # Asigna un ID único al libro y lo convierte a cadena str string
        self.titulo = titulo  # Asigna el título del libro
        self.autor = autor  # Asigna el autor del libro
        self.editorial = editorial  # Asigna la editorial del libro
        self.ano_publicacion = ano_publicacion  # Asigna el año de publicación del libro
        self.genero = genero  # Asigna el género del libro
        self.cantidad_disponible = cantidad_disponible  # Asigna la cantidad disponible del libro

    def to_dict(self):
        # Método que devuelve un diccionario con los atributos del libro
        return self.__dict__  # Retorna el diccionario con los atributos del libro