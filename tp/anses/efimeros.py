from tp.usuarios.usuario import Administrador
from parciales.final2020feb.unnitest import Lista
class efimero:
    @classmethod
    def TelefonoACuil(cls, telefono):
        hola = Lista()
        cacona = hola.ciudadanos
        for ciuda in cacona:
            if ciuda.telefono == telefono:
                return ciuda.cuil
        return "Kpo el chabon no esta registrado"
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

