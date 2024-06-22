class Socio:  # Define una nueva clase llamada Socio
    contador_id = 0  # Variable estática para contar los IDs

    def __init__(self, nombre, direccion, telefono):
        # Método constructor para inicializar una nueva instancia de Socio
        Socio.contador_id += 1  # Incrementa el contador de IDs
        self.id_socio = str(Socio.contador_id)  # Asigna un ID único al socio y lo convierte a cadena
        self.nombre = nombre  # Asigna el nombre del socio
        self.direccion = direccion  # Asigna la dirección del socio
        self.telefono = telefono  # Asigna el teléfono del socio

    def to_dict(self):
        # Método que devuelve un diccionario con los atributos del socio
        return {
            'id_socio': self.id_socio,  # Incluye el ID del socio en el diccionario
            'nombre': self.nombre,  # Incluye el nombre del socio en el diccionario
            'direccion': self.direccion,  # Incluye la dirección del socio en el diccionario
            'telefono': self.telefono  # Incluye el teléfono del socio en el diccionario
        }