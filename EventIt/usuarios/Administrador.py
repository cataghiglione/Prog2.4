class Administrador:
    bloqueados = []
    reportesAdministracionSensores = []

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

