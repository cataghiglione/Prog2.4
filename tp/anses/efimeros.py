from usuarios.usuario import Administrador
import csv
from solicitudes.contacto import Contacto
from solicitudes.solicitud import Solicitud
class efimero:
    @classmethod
    def TelefonoACuil(cls, telefono):
        Anses = open("Anses.csv", "r")
        reader = csv.reader(Anses, delimiter="|")
        for fila in reader:
            if fila [1] == telefono:
                cuil = fila [2]
                return cuil
        Anses.close()
        raise NoExiste("No se encontro el telefono solicitado")
    @classmethod
    def CuilATelefono(cls, cuil):
        buenas = Lista()
        caquita = buenas.ciudadanos
        for ciuda in caquita:
            if ciuda.cuil == cuil:
                return ciuda.telefono
        return "Kpo el chabon no esta registrado"
    @classmethod
    def ContactoACiudadano(cls, contacto):
        buenas = Administrador()
        caquita = buenas.ciudadanos
        for ciuda in caquita:
            if ciuda.cuil == contacto.cuil:
                return ciuda
            if ciuda.telefono == contacto.numero:
                return ciuda
    @classmethod
    def EnviarSolicitud(cls, cuil, telefono, info):
        if len(str(info)) == 13:
            celular_r = info
            try:
                cuil_r = efimero.TelefonoACuil(celular_r)
            except NoExiste:
                return "Ese telefono no esta registrado, por favor verifique los datos"
            except Exception:
                return "Ha ocurrido un error"
            else:
                contacto_r = Contacto(cuil_r, celular_r)
                contacto_e = Contacto(cuil, telefono)
                solicitud1 = Solicitud(contacto_e, contacto_r)


        elif len(str(info)) == 11:
            cuil_r = info
            telefono_r = efimero.CuilATelefono(cuil_r)
        else:
            raise DatosIncorrectos("Un cuil tiene 11 numeros, y un telefono 13, por favor verifique los datos ingresados")


class DatosIncorrectos(Exception):
    def __init__(self, msg):
        self.msg = msg
    def mensaje(self):
        return self.msg

class NoExiste(Exception):
    def __init__(self, msg):
        self.msg = msg
    def mensaje(self):
        return self.msg