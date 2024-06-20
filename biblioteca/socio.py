class Socio:
    def __init__(self, id_socio, nombre, direccion, telefono):
        self.id_socio = id_socio
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def to_dict(self):
        return self.__dict__
