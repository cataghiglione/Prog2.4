class Administrador:
    def __init__(self):
        self.ciudadanos = []
        self.eventos = []
    def bloquear(self, usuario):
        pass

    def desbloquear(self, usuario):
        pass

    def darAlta(self, evento):
        pass

    def auditar(self, usuario):
        pass
    def agregarCiudadano(self, ciudadano):
        self.ciudadanos.append(ciudadano)

    def buscarTelefono(self, cuil):
        for ciudadano in self.ciudadanos:
            if cuil == ciudadano.cuil :
                return ciudadano.telefono

    def buscarCuil(self, telefono):
        for ciudadano in self.ciudadanos:
            if telefono == ciudadano.telefono :
                return ciudadano.cuil



from tp.solicitudes.solicitud import Solicitud
from tp.solicitudes.contacto import Contacto

from tp.anses.efimeros import efimero
class Ciudadano:
    def __init__(self, telefono, cuil):
        self.telefono = telefono
        self.cuil = cuil
        self.contactos = []
        self.solicitudes = []
        self.bloqueado = False


    def mandarSolicitud(self, info):
        if self.bloqueado == False:
            if len(str(info)) == 13:
                celular_r = info
                cuil_r = efimero.TelefonoACuil(celular_r)
            elif len(str(info)) == 11:
                cuil_r = info
                telefono_r = efimero.CuilATelefono(cuil_r)
            else:
                pass #metele una excepcion ahi

            contacto_r = Contacto(cuil_r, telefono_r)
            contacto_e = Contacto(self.cuil, self.telefono)

            solicitud1 = Solicitud(contacto_e, contacto_r)
            ciudadano_r = efimero.ContactoACiudadano(contacto_r)
            ciudadano_r.solicitudes.append(solicitud1)

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
