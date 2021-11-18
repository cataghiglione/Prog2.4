class Solicitud:
    def __init__(self, emisor):
        self.emisor = emisor

    def __repr__(self):
        return f"Solicitud de {self.emisor.nombre} con cuil {self.emisor.cuil}"

    def getCuilEmisor(self):
        return self.emisor.cuil
