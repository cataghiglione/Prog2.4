class Error(Exception):
    @classmethod
    def ErrorMsg(cls, msg):
        return msg


class CiudadanoYaRegistrado(Exception):
    @classmethod
    def getMsg(cls, msg):
        return msg


class NoExiste(Exception):
    @classmethod
    def getMsg(cls, msg):
        return msg


class DatosIncorrectos(Exception):
    @classmethod
    def getMsg(cls, msg):
        return msg


class SolicitudNoEncontrada(Exception):
    @classmethod
    def getMsg(cls):
        return 'La solicitud no fue encontrada, escriba el nombre nuevamente.'


class ErrorCuil(Exception):
    @classmethod
    def getMsg(cls, msg):
        return msg


class ErrorTelefono(Exception):
    @classmethod
    def getMsg(cls, msg):
        return msg


class CiudadanoExisteMismoTelefonooNombre(Exception):
    @classmethod
    def getMsg(cls, msg):
        return msg


class CiudadanoExisteMismoCuil(Exception):
    @classmethod
    def getMsg(cls, msg):
        return msg


class FechaError(Exception):
    @classmethod
    def getMsg(cls, msg):
        return msg


class NonAdminError(Exception):
    @classmethod
    def NonAdminErrorMsg(cls, msg):
        return msg


class Bloqueado(Exception):

    def __init__(self, msg):
        self.msg = msg

    def mensaje(self):
        return self.msg
