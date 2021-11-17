class Error(Exception):
    @classmethod
    def ErrorMsg(cls, msg):
        return msg


class NoExiste(Exception):
    pass


class DatosIncorrectos(Exception):
    pass


class ErrorCuil(Exception):
    pass


class ErrorTelefono(Exception):
    pass


class CiudadanoExisteMismoTelefonooNombre(Exception):
    pass


class CiudadanoExisteMismoCuil(Exception):
    pass


class FechaError(Exception):
    pass


class NonAdminError(Exception):
    @classmethod
    def NonAdminErrorMsg(cls, msg):
        return msg


class Bloqueado(Exception):

    def __init__(self, msg):
        self.msg = msg

    def mensaje(self):
        return self.msg
