from EventIt.anses.Exceptions1 import DatosIncorrectos


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
        if not self.bloqueado:
            try:
               paquete = Efimero.EnviarSolicitud(self.cuil, self.telefono, int(info))
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
                error = Bloqueado("Estas bloqueado por bobina")
                return error.mensaje()

    def verSolicitudes(self):
        return self.solicitudes

    #def rechazarSolicitud(self, solicitud):
     #   self.solicitudes.remove(solicitud)
      #  Efimero.rechazar(solicitud)

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
