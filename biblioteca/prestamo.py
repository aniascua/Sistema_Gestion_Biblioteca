class Prestamo:
    contador_id = 0

    def __init__(self, id_libro, id_socio, fecha_prestamo):
        Prestamo.contador_id += 1
        self.id_prestamo = Prestamo.contador_id
        self.id_libro = id_libro
        self.id_socio = id_socio
        self.fecha_prestamo = fecha_prestamo

    def to_dict(self):
        return {
            'id_prestamo': self.id_prestamo,
            'id_libro': self.id_libro,
            'id_socio': self.id_socio,
            'fecha_prestamo': self.fecha_prestamo
        }