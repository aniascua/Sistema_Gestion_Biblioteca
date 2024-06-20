class Prestamo:
    def __init__(self, id_prestamo, id_libro, id_socio, fecha_prestamo, fecha_devolucion=None):
        self.id_prestamo = id_prestamo
        self.id_libro = id_libro
        self.id_socio = id_socio
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def to_dict(self):
        return self.__dict__
