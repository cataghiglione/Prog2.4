from collections import defaultdict


class Contacto:
    def __init__(self, cuil, numero, nombre):
        self.cuil = cuil
        self.numero = numero
        self.nombre = nombre


class Solicitud:
    def __init__(self, emisor):
        self.emisor = emisor


class Error(Exception):
    pass


class NoExiste(Exception):
    pass


class DatosIncorrectos(Exception):
    pass


class Diccionario:

    def __init__(self):
        self.dict = defaultdict()

    def agregar(self, cuil, ciudadano):
        self.dict[cuil] = ciudadano

    def quitar(self, cuil):
        for key, value in self.dict.items():
            if key == cuil:
                self.dict.pop(key)
                return True
        raise Error
        # "el cuil no fue encontrado"

    def buscar(self, cuil):
        for key, value in self.dict.items():
            if key == cuil:
                return value
        raise Error
        # "el cuil no fue encontrado"


ciudadanoList = Diccionario()

try:
    ciudadanoList.agregar('Valentina', 12345678999)
except Error:
    print('algo, cualquier cosa')

