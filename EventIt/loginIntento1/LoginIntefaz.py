import csv

from EventIt.diccionario import ciudadanoList
from EventIt.usuarios.Administrador import Administrador
from EventIt.usuarios.Ciudadano import Ciudadano
from EventIt.Estadistica.Estadistica1 import Tablero
from EventIt.mapa1.Mapa import Mapa
from EventIt.mapa1.Evento import Evento
from EventIt.Sensores.Sensor import Sensor
from EventIt.Sensores.AdministracionSensores import AdministracionSensores
from EventIt.exceptions import e

# Instancie administrador debido a que se trata siempre del mismo

admin = Administrador()


class Function:
    def Choice(self):
        while True:
            try:
                accion = int(input(
                    "Ingrese: \n\t|1 para Ciudadano\n\t|2 Para Admin \n\t|3 Para ver el Mapa \n\t|4 Para ver el tablero \n\t|5 Para crear un evento: "))
                if accion != 1 and accion != 2 and accion != 3 and accion != 4 and accion != 5:
                    raise e.Error()
                break
            except ValueError:
                print("Coloque uno de los valores solicitados ;)")
            except:
                print("Coloque uno de los valores solicitados")

        if accion == 1:
            return self.CitizenLoop()
        elif accion == 2:
            return self.AdminLoop()
        elif accion == 3:
            return self.MapLoop()
        elif accion == 4:
            return self.StatisticsLoop()
        elif accion == 5:
            return self.EventosLoop()
        else:
            print("Hay un error obteniendo usuario ;)")

    def StatisticsLoop(self):
        while True:
            try:
                accion = int(input("|Ingrese 1 para ver el tablero \n|2 para "))
                if accion != 1 and accion != 2:
                    raise e.Error()
                break
            except ValueError:
                print("Coloque el digito soliciatado")
            except e.Error:
                print("Debe ingresar 1 o 2")
        if accion == 1:
            # recibe la lista de eventos
            eventos = []
            Tablero.ranking(eventos)
        elif accion == 2:
            return self.Choice()
        return self.StatisticsLoop()

    def MapLoop(self):
        while True:
            try:
                accion = int(input('Ingrese: \n\t|1 para ver el mapa\n\t|2 para volver al LogIn'))
                if accion != 1 and accion != 2:
                    raise e.Error()
                break
            except ValueError:
                print(e.Error.ErrorMsg("Ingrese uno de los valores solicitados"))
            except e.Error:
                print(e.Error.ErrorMsg("Los valores no son correctos"))
        if int(accion) == 1:
            mi = Mapa()
            mi.VerMapa()
        elif int(accion) == 2:
            return self.Choice()
        return self.MapLoop()

    def CitizenLoop(self):
        while True:
            try:
                accion = int(input("Si esta registrado presione 1, si quiere registrarse presione 2: "))
                break
            except ValueError:
                print("Ingrese el numero solicitado")
        if accion == 1:
            self.CitizenLogIn()
        elif accion == 2:
            while True:
                try:
                    nombre = input("Ingrese su nombre: ")
                    if self.verificarDatosNoExistentes(nombre=nombre):
                        raise e.CiudadanoExisteMismoTelefonooNombre()
                    telefono = int(input("Ingrese su numero de telefono: +54 9 "))
                    if self.verificarDatosNoExistentes(telefono=telefono):
                        raise e.CiudadanoExisteMismoTelefonooNombre()
                    if not Checker.CheckTelefono(str(telefono)):
                        raise e.ErrorTelefono()
                    cuil = int(input("Ingrese su Cuil: "))
                    if self.verificarDatosNoExistentes(cuil=cuil):
                        raise e.CiudadanoExisteMismoCuil()
                    if not Checker.CheckCuil(str(cuil)):
                        raise e.ErrorCuil()
                except ValueError:
                    print("Coloque solo numeros enteros para el telefono y el cuil")
                except Exception:
                    print("Un Cuil posee 11 digitos y un telefono 10")
                else:
                    self.registrarCiudadanoAnses(nombre.title(), int(telefono), int(cuil))
                    ciudadano = Ciudadano(nombre, int(telefono), int(cuil))
                    ciudadanoList.agregar(int(cuil), ciudadano)
                    self.CitizenLoop()
                    break

    def verificar(self, nombre, telefono, cuil):
        Anses = open("Anses.csv", "r")
        reader = csv.reader(Anses, delimiter="|")
        datos = [nombre, str(telefono), str(cuil)]
        for fila in reader:
            if fila[0] == datos[0] and fila[1] == datos[1] and fila[2] == datos[2]:
                return True
        Anses.close()
        return False

    def verificarDatosNoExistentes(self, nombre="", telefono=0, cuil=0):
        Anses = open("Anses.csv", "r")
        reader = csv.reader(Anses, delimiter="|")
        datos = [nombre, str(telefono), str(cuil)]
        for fila in reader:
            if fila[0] == datos[0] or fila[1] == datos[1] or fila[2] == datos[2]:
                return True
        Anses.close()
        return False

    def registrarCiudadanoAnses(self, nombre, telefono, cuil):
        verificacion = self.verificar(nombre, telefono, cuil)
        if verificacion:
            return "Ya existe una cuenta con estos datos"
        elif not verificacion:
            Anses = open("Anses.csv", "a", newline="")
            writer = csv.writer(Anses, delimiter="|")
            datos = [nombre, telefono, cuil]
            writer.writerow(datos)
            Anses.close()
            return "Registrado"

    def CitizenLogIn(self):
        while True:
            try:
                cuil = input("Ingrese su Cuil: ")
                if not Checker.CheckCuil(str(cuil)):
                    raise e.ErrorCuil()
                break
            except ValueError:
                return e.Error.ErrorMsg("Ingrese valores numéricos")
            except Exception:
                return e.Error.ErrorMsg("Ingrese su Cuil de 11 digitos")
        print("Se ha iniciado sesion")
        ciudadano = ciudadanoList.buscar(cuil)
        return self.CitizenChoices(ciudadano)

    def CitizenChoices(self, ciudadano):
        while True:
            try:
                accion = int(input(
                    "Ingrese:\n\t|1 para mandar solicitud\n\t|2 para ver las solicitudes pendientes\n\t|3 para reportar un evento a los administradores" +
                    "\n\t|4 para enviar información de un evento a tus contactos"))
                if accion != 1 != 2 != 3 != 4:
                    raise e.Error()
                break
            except e.Error:
                print(e.Error.ErrorMsg('Ingrese valores validos.'))
            except ValueError:
                print('Ingrese únicamente valores numéricos entre 1 y 4')

    # if accion == 1

    def EventosLoop(self):
        while True:
            try:
                x = int(input("Ingrese la longitud: "))
                y = int(input("Ingrese la latitud: "))
                tipo = input("Ingrese el tipo de evento: ")
                nombre = input("Ingrese el nombre la localidad: ")
                cantidadPersonas = int(input("Ingrese la cantidad de participantes: "))
                fecha = input("Ingrese el Dia de hoy separando el dia y el mes con un espacio de barra: ")
                if len(str(fecha)) != 5:
                    raise e.FechaError()
                break
            except ValueError:
                print("En latitud, longitud y cantidad de participantes ingrese valores numericos")
            except e.FechaError:
                print("No esta colocando correctamente la fecha, recuerde el espacios ;)")
        Sensor.ReprotarAdministracion(x, y, nombre, tipo, cantidadPersonas, fecha)
        AdministracionSensores.ReportarEventoAAdmin()
        mi = Mapa()
        mi.ReiniciarBotones()
        mi.AgregarBoton(Evento(x, y, nombre, tipo, cantidadPersonas))
        print(f"Su evento de {tipo} ha sido creado")
        return self.Choice()

    def AdminLoop(self):
        counter = 0
        while counter < 3:
            try:
                contrasena = input("Ingrese la contraseña de Administrador: ")
                if contrasena == "Sumbudrule":
                    print("Creaste un Admin!!!!!!!!!")
                    return -1  # llamo a AdminChoices(admin)
                elif contrasena != "Sumbudrule":
                    raise e.NonAdminError()
                break
            except:
                print("Si sos admin, poné bien la contra ;)")
                counter += 1
        print("Vos no sos Admin, comunicate con un psicologo")
        print("...Volviendo al inicio...")
        return self.Choice()

    def AdminChoices(self, admin):
        while True:
            try:
                accion = int(input("Si esta registrado presione 1, si quiere registrarse presione 2: "))
                break
            except ValueError:
                print("Ingrese el numero solicitado")
        return self.Choice()


functions = Function()


prueba = Function()
prueba.CitizenLoop()


class Checker:
    @classmethod
    def CheckCuil(self, cuil):
        if len(cuil) == 11:
            return True
        else:
            print("raro")
            return False

    @classmethod
    def CheckDni(self, dni):
        """Si es un dni retorna True"""
        if len(dni) == 8:
            return True
        else:
            return False

    @classmethod
    def CheckTelefono(self, telefono):
        if len(telefono) == 10:
            return True
        else:
            return False
