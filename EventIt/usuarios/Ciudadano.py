from EventIt.anses.Exceptions1 import DatosIncorrectos
from EventIt.diccionario import ciudadanoList

from EventIt.exceptions.e import Bloqueado


class Ciudadano:
    def __init__(self, nombre,telefono, cuil):
        self.nombre = nombre
        self.telefono = telefono
        self.cuil = cuil
        self.contactos = []
        self.solicitudes = []
        self.bloqueado = False
        self.intentos = 0

    def mandarSolicitud(self, infoReceptor):
        if not self.bloqueado:
            try:
               paquete = Efimero.EnviarSolicitud(self.cuil, self.telefono, self.nombre, infoReceptor)
            except ValueError:
                return "Coloque un valor telefono o cuil del receptor"
            except DatosIncorrectos:
                error = DatosIncorrectos("Los datos son incorrectos")
                return error.mensaje()
            except Exception:
                return "Ha ocurrido un error"
            else:
                solicitud = paquete[0]
                receptor = paquete[1]
                receptor.__recibirSolicitud(solicitud)
                return True
        else:
            try:
                raise Bloqueado
            except Bloqueado:
                error = Bloqueado("El usuario se encuentra bloqueado")
                return error.mensaje()

    def verSolicitudes(self):
        return self.solicitudes

    #def rechazarSolicitud(self, solicitud):
     #   self.solicitudes.remove(solicitud)
      #  Efimero.rechazar(solicitud)

    def aceptarSolicitud(self, solicitud):
        if not self.bloqueado:
            if solicitud in self.solicitudes:
                self.contactos.append(solicitud.emisor())

    def reportarEvento(self, evento):
        pass

    def enviarInfoEvento(self, evento, contacto):
        pass

    def __recibirSolicitud(self, solicitud1):
        self.solicitudes.append(solicitud1)


from EventIt.anses.Exceptions1 import NoExiste, DatosIncorrectos
from EventIt.loginIntento1.metodos import Metodo
from EventIt.solicitudes.contacto import Contacto
from EventIt.solicitudes.solicitud import Solicitud
from EventIt.usuarios.Administrador import Administrador
import csv


class CrearCiudadano:
    @classmethod
    def crear_ciudadano(cls, cuil, telefono):
        Anses = open("Anses.csv", "r")
        reader = csv.reader(Anses, delimiter="|")
        for fila in reader:
            if fila[1] == str(telefono) and fila[2] == str(cuil):
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
            if fila[1] == str(telefono):
                cuil = int(fila[2])
                return cuil
        raise NoExiste("No se encontro el telefono solicitado")

    @classmethod
    def CuilATelefono(cls, cuil):
        Anses = open("Anses.csv")
        reader = csv.reader(Anses, delimiter="|")
        for fila in reader:
            if fila[2] == str(cuil):
                telefono = int(fila[1])
                return telefono
        raise NoExiste("No se encontro el cuil solicitado")

    @classmethod
    def EnviarSolicitud(cls, cuil, telefono, nombre, info): #info: celular del receptor de la solicitud
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
                ciudadano_r = ciudadanoList.buscar(cuil_r)
                paquete = [solicitud1, ciudadano_r]
                return paquete
        elif len(str(info)) == 11:
            cuil_r = info
            contacto_e = Contacto(cuil, telefono, nombre)
            solicitud1 = Solicitud(contacto_e)
            ciudadano_r = ciudadanoList.buscar(cuil_r)
            paquete = [solicitud1, ciudadano_r]
            return paquete
        else:
            raise DatosIncorrectos(
                "Un cuil tiene 11 numeros, y un telefono 10, por favor verifique los datos ingresados")

    def rechazar(self, solicitud):
        contacto = solicitud.contacto
        ciudadano = CrearCiudadano.crear_ciudadano(contacto.cuil, contacto.numero)
        ciudadano.intentos += 1
        if ciudadano.intentos == 5:
            ciudadano.bloqueado = True
            admin = Administrador()
            admin.bloqueados.append(ciudadano)
