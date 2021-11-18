from EventIt.anses.Exceptions1 import NoExiste, DatosIncorrectos
from EventIt.diccionario import ciudadanoList
from EventIt.solicitudes.contacto import Contacto
from EventIt.solicitudes.solicitud import Solicitud
from EventIt.usuarios.Administrador import Administrador
from EventIt.usuarios.Ciudadano import Ciudadano
from EventIt.exceptions import e
import csv


class CrearCiudadano:
    @classmethod
    def crear_ciudadano(cls, cuil, telefono):
        Anses = open("Anses.csv", "r")
        reader = csv.reader(Anses, delimiter="|")
        for fila in reader:
            if fila[1] == telefono and fila[2] == cuil:
                nombre = fila[0]
                return Ciudadano(nombre, telefono, cuil)
        Anses.close()


class Efimero:

    @classmethod
    def TelefonoACuil(cls, telefono):
        """Dado un Telefono obtengo un Cuil"""
        Anses = open("Anses.csv", "r")
        reader = csv.reader(Anses, delimiter="|")
        for fila in reader:
            if fila[1] == str(telefono):
                cuil = int(fila[2])
                Anses.close()
                return cuil
        raise NoExiste("No se encontro el telefono solicitado")

    @classmethod
    def CuilANombre(cls, cuil):
        """Dado un cuil obtengo un nombre"""
        Anses = open("Anses.csv", "r")
        reader = csv.reader(Anses, delimiter="|")
        try:
            for fila in reader:
                if fila[2] == str(cuil):
                    nombre = fila[0]
                    Anses.close()
                    return nombre
            raise e.NoExiste()
        except NoExiste:
            print(e.NoExiste.getMsg('No se encontro el cuil solicitado.'))

    @classmethod
    def CuilANombreEventIt(cls, cuil):
        """Dado un cuil obtengo un nombre"""
        EventIt = open("EventIt.csv", "r")
        reader = csv.reader(EventIt, delimiter="|")
        try:
            for fila in reader:
                if fila[2] == str(cuil):
                    nombre = fila[0]
                    EventIt.close()
                    return nombre
            raise e.NoExiste()
        except NoExiste:
            print(e.NoExiste.getMsg('No se encontro el cuil solicitado.'))

    @classmethod
    def CuilATelefonoEventIt(cls, cuil):
        """Dado un cuil obtengo un nombre"""
        EventIt = open("EventIt.csv", "r")
        reader = csv.reader(EventIt, delimiter="|")
        try:
            for fila in reader:
                if fila[2] == str(cuil):
                    telefono = int(fila[1])
                    EventIt.close()
                    return telefono
            raise e.NoExiste()
        except NoExiste:
            print(e.NoExiste.getMsg('No se encontro el cuil solicitado.'))

    @classmethod
    def CuilATelefono(cls, cuil):
        Anses = open("Anses.csv", "r")
        reader = csv.reader(Anses, delimiter="|")
        for fila in reader:
            if fila[2] == str(cuil):
                telefono = int(fila[1])
                Anses.close()
                return telefono
        raise NoExiste("No se encontro el cuil solicitado")

    @classmethod
    def EnviarSolicitud(cls, cuil, telefono, nombre, info):  # info: celular del receptor de la solicitud
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
            raise DatosIncorrectos()

    def rechazar(self, solicitud):
        contacto = solicitud.contacto
        ciudadano = CrearCiudadano.crear_ciudadano(contacto.cuil, contacto.numero)
        ciudadano.intentos += 1
        if ciudadano.intentos == 5:
            ciudadano.bloqueado = True
            Administrador.bloqueados.append(ciudadano)
