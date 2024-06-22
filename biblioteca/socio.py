class Socio:
    contador_id = 0  # Variable estática para contar los IDs

    def __init__(self, nombre, direccion, telefono):
        Socio.contador_id += 1
        self.id_socio = Socio.contador_id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def to_dict(self):
        return self.__dict__
