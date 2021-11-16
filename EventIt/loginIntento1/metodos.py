import csv

from EventIt.solicitudes.contacto import Contacto
from EventIt.solicitudes.solicitud import Solicitud

class Metodo:
    @classmethod
    def CuilANombre(cls, cuil):
        Anses = open("Anses.csv", "r")
        reader = csv.reader(Anses, delimiter="|")
        for fila in reader:
            if fila[2] == str(cuil):
                nombre = fila[0]
                return nombre
        Anses.close()
        raise NoExiste("No se encontro el cuil solicitado")
    @classmethod
    def TelefonoANombre(cls, telefono):
        Anses = open("Anses.csv", "r")
        reader = csv.reader(Anses, delimiter="|")
        for fila in reader:
            if fila[1] == str(telefono):
                nombre = fila[0]
                return nombre
        raise NoExiste("No se encontro el telefono solicitado")
    @classmethod
    def TelefonoACuil(cls, telefono):
        Anses = open("Anses.csv", "r")
        reader = csv.reader(Anses, delimiter="|")
        for fila in reader:
            if fila[1] == str(telefono):
                cuil = int(fila[2])
                return cuil
        raise NoExiste("No se encontro el telefono solicitado")
    @classmethod
    def CuilATelefono(cls, cuil):
        Anses = open("Anses.csv", "r")
        reader = csv.reader(Anses, delimiter="|")
        for fila in reader:
            if fila[2] == str(cuil):
                telefono = int(fila[1])
                return telefono
        Anses.close()
        raise NoExiste("No se encontro el cuil solicitado")

class NoExiste(Exception):
    def __init__(self, msg):
        self.msg = msg
    def mensaje(self):
        return self.msg
