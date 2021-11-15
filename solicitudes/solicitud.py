
class Solicitud:
    def __init__(self, contacto):
        self.contacto = contacto

    def __repr__(self):
        nombre = self.contacto.nombre
        return f"{nombre}"
