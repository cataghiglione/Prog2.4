from EventIt.usuarios.Ciudadano import Ciudadano
import csv
class CrearCiudadano:
    @classmethod
    def crear_ciudadano(cls, cuil, telefono):
        Anses = open("Anses.csv", "r")
        reader = csv.reader(Anses, delimiter="|")
        for fila in reader:
            if fila[1] == telefono and fila [2] == cuil:
                nombre = fila[0]
                return Ciudadano(nombre, telefono, cuil)
        Anses.close()
