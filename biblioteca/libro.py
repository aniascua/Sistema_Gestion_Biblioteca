class Libro:
    contador_id = 0  # Variable estática para contar los IDs

    def __init__(self, titulo, autor, editorial, ano_publicacion, genero, cantidad_disponible):
        Libro.contador_id += 1
        self.id_libro = str(Libro.contador_id)
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.ano_publicacion = ano_publicacion
        self.genero = genero
        self.cantidad_disponible = cantidad_disponible

    def to_dict(self):
        return self.__dict__
