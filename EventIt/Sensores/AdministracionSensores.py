
from EventIt.usuarios.Administrador import Administrador

class AdministracionSensores:
    eventosReportados = []
    @classmethod
    def ReportarEventoAAdmin(cls):
        for reporte in cls.eventosReportados:
            Administrador.reportesAdministracionSensores.append(reporte)
        cls.eventosReportados = []
