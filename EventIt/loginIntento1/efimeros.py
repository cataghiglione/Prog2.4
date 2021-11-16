from EventIt.anses.Exceptions1 import NoExiste, DatosIncorrectos
from EventIt.loginIntento1.metodos import Metodo
from EventIt.solicitudes.contacto import Contacto
from EventIt.solicitudes.solicitud import Solicitud
from EventIt.usuarios.Administrador import Administrador
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


class Efimero:
    @classmethod
    def CuilANombre(cls, telefono):
        """Dado un Telefono obtengo un Cuil"""
        Anses = open("Anses.csv", "r")
        reader = csv.reader(Anses, delimiter="|")
        for fila in reader:
            if fila[1] == str(telefono):
                cuil = int(fila[2])
                return cuil
        raise NoExiste("No se encontro el telefono solicitado")

    @classmethod
    def TelefonoACuil(cls, telefono):
         """Dado un Telefono obtengo un Cuil"""
         Anses = open("Anses.csv", "r")
         reader = csv.reader(Anses, delimiter="|")
         for fila in reader:
             if fila [1] == str(telefono):
                 cuil = int(fila [2])
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
        raise NoExiste("No se encontro el cuil solicitado")

    @classmethod
    def EnviarSolicitud(cls, cuil, telefono,nombre, info):
        if len(str(info)) == 10:
            celular_r = info
            try:
                cuil_r = Efimero.TelefonoACuil(celular_r)
            except NoExiste:
                return "Ese telefono no esta registrado, por favor verifique los datos"
            except Exception:
                return "Ha ocurrido un error"
            else:
                contacto_e = Contacto(cuil, telefono, nombre)
                solicitud1 = Solicitud(contacto_e)
                ciudadano = CrearCiudadano.crear_ciudadano(cuil_r, celular_r)
                paquete = [solicitud1, ciudadano]
                return paquete

        elif len(str(info)) == 11:
            cuil_r = info
            try:
                celular_r = Efimero.CuilATelefono(cuil_r)
            except NoExiste:
                return "Ese cuil no esta registrado, por favor verifique los datos"
            except Exception:
                return "Ha ocurrido un error"
            else:
                contacto_e = Contacto(cuil, telefono, nombre)
                solicitud1 = Solicitud(contacto_e)
                ciudadano = CrearCiudadano.crear_ciudadano(cuil_r, celular_r)
                paquete = [solicitud1, ciudadano]
                return paquete
        else:
            raise DatosIncorrectos("Un cuil tiene 11 numeros, y un telefono 10, por favor verifique los datos ingresados")

    def rechazar(self,solicitud):
        contacto =solicitud.contacto
        ciudadano =CrearCiudadano.crear_ciudadano(contacto.cuil, contacto.numero)
        ciudadano.intentos += 1
        if ciudadano.intentos == 5:
            ciudadano.bloqueado = True
            admin = Administrador()
            admin.bloqueados.append(ciudadano)

