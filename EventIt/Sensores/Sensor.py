from EventIt.Sensores.Reporte import Reporte
from EventIt.mapa1.Evento import Evento
from EventIt.Sensores.AdministracionSensores import AdministracionSensores


class Sensor:

    @classmethod
    def ReportarAdministracion(cls, x, y, nombre, tipo, cantidadPersonas, fecha):
        evento = Evento(x, y, nombre, tipo, cantidadPersonas)
        reporte = Reporte(evento, fecha)
        AdministracionSensores.eventosReportados.append(reporte)
