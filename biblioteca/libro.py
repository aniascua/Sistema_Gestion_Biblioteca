class Libro:
    contador_id = 0  # Variable estática para contar los IDs

    def __init__(self, titulo, autor, editorial, ano_publicacion, genero, cantidad_disponible):
        Libro.contador_id += 1
        self.id_libro = Libro.contador_id
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.ano_publicacion = ano_publicacion
        self.genero = genero
        self.cantidad_disponible = cantidad_disponible

    def get_id(self):
        return self.id_libro

    def to_dict(self):
        return {
            'id_libro': self.id_libro,
            'titulo': self.titulo,
            'autor': self.autor,
            'editorial': self.editorial,
            'ano_publicacion': self.ano_publicacion,
            'genero': self.genero,
            'cantidad_disponible': self.cantidad_disponible
        }
