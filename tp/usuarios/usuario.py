class Administrador:
    bloqueados = []
    def __init__(self):
        self.eventos = []
    def bloquear(self, usuario):
        usuario.bloqueado = True

    def desbloquear(self, usuario):
        usuario.bloqueado = False

    def darAlta(self, evento):
        pass

    def auditar(self, usuarios):
        pass


from anses.efimeros import DatosIncorrectos
from tp.solicitudes.solicitud import Solicitud
from tp.solicitudes.contacto import Contacto

from tp.anses.efimeros import efimero
class Ciudadano:
    def __init__(self, nombre,telefono, cuil):
        self.nombre = nombre
        self.telefono = telefono
        self.cuil = cuil
        self.contactos = []
        self.solicitudes = []
        self.bloqueado = False
        self.intentos = 0


    def mandarSolicitud(self, info):
        if self.bloqueado == False:
            try:
                paquete = efimero.EnviarSolicitud(self.cuil, self.telefono, int(info))
            except ValueError:
                return "Coloque un valor telefono o cuil del receptor"
            except DatosIncorrectos as error:
                error = DatosIncorrectos("Los datos son incorrectos")
                return error.mensaje()
            except Exception:
                return "Ha ocurrido un error"
            else:
                solicitud = paquete[0]
                receptor = paquete[1]
                receptor.__recibirSolicitud(solicitud)
        else:
            try:
                raise Bloqueado
            except Bloqueado as error:
                error = Bloqueado("Estas bloqueado por bobina")
                return error.mensaje()


    def verSolicitudes(self):
        return self.solicitudes

    def rechazarSolicitud(self, solicitud):
        pass

    def aceptarSolicitud(self, solicitud):
        if self.bloqueado == False:
            if solicitud in self.solicitudes:
                self.contactos.append(solicitud.emisor())
    def reportarEvento(self, evento):
        pass

    def enviarInfoEvento(self, evento, contacto):
        pass

    def __recibirSolicitud(self, solicitud1):
        self.solicitudes.append(solicitud1)

class Bloqueado(Exception):
    def __init__(self, msg):
        self.msg = msg
    def mensaje(self):
        return self.msg