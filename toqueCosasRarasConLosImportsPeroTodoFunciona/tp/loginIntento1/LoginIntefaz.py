import csv
from tp.usuarios.usuario import Administrador

#Instancie administrador debido a que se trata siempre del mismo
admin = Administrador()

#cambiar nombre
class Error(Exception):
    msg1 = "Coloque uno de los valores solicitados"

miErro = Error()
def Choice():
    while True:
        try:
            usuario = int(input("Ingrese 1 para Ciudadano, 2 para Admin o 3 para ver el Mapa: "))
            if usuario != 1 and usuario != 2 and usuario != 3:
                raise Error()
            break
        except ValueError:
            print("Coloque uno de los valores solicitados ;)")
        except:
            print("Coloque uno de los valores solicitados")

    if usuario == 1:
        CitizenLoop()
    elif usuario == 2:
        AdminLoop()
    elif usuario == 3:
        MapLoop()
    else:
        print("Hay un error obteniendo usuario ;)")


class ErrorCuil(Exception):
    pass


class ErrorTelefono(Exception):
    pass

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


class CiudadanoExisteMismoTelefonooNombre(Exception):
    pass


class CiudadanoExisteMismoCuil(Exception):
    pass

class MapChoices:
    pass

from tp.mapa1.Mapa import Mapa

def MapLoop():
    while True:
        try:
            accion = int(input("Ingrese 1 para abrir el mapa o 2 para volver a Login: "))
            if accion != 1 and accion !=2:
                raise Error()
            break
        except ValueError:
            print("Ingrese uno de los valores solicitados")
        except Error:
            print("Los valores no son correctos")
    if int(accion) == 1:
        mi = Mapa()
        mi.VerMapa()
    elif int(accion) == 2:
        Choice()
    Choice()

def CitizenLoop():
    while True:
        try:
            accion = int(input("Si esta registrado presione 1, si quiere registrarse presione 2: "))
            break
        except ValueError:
            print("Ingrese el numero solicitado")
    if accion == 1:
        CitizenLogIn()
    elif accion == 2:
        while True:
            try:
                nombre = input("Ingrese su nombre: ")
                telefono = int(input("Ingrese su numero de telefono: +54 9 "))
                if verificarDatosNoExistentes(telefono = telefono) or verificar(nombre= nombre):
                    raise CiudadanoExisteMismoTelefonooNombre()
                if Checker.CheckTelefono(str(telefono)) == False:
                    raise ErrorTelefono()
                cuil = int(input("Ingrese su Cuil: "))
                if verificarDatosNoExistentes(cuil=cuil):
                    raise CiudadanoExisteMismoCuil()
                if Checker.CheckCuil(str(cuil)) == False:
                    raise ErrorCuil()
            except ValueError:
                print("Coloque solo numeros enteros para el telefono y el cuil")
            except Exception:
                print("Un Cuil posee 11 digitos y un telefono 8 digitos ;)")
            else:
                registrarCiudadanoAnses(nombre.title(), int(telefono), int(cuil))
                CitizenLoop()
                break

def verificar(nombre, telefono, cuil):
    Anses = open("Anses.csv", "r")
    reader = csv.reader(Anses, delimiter="|")
    datos = [nombre, str(telefono), str(cuil)]
    for fila in reader:
        if fila[0] == datos[0] and fila[1] == datos[1] and fila[2] == datos[2]:
            return True
    Anses.close()
    return False
def verificarDatosNoExistentes(nombre = "", telefono = 0, cuil = 0):
    Anses = open("Anses.csv", "r")
    reader = csv.reader(Anses, delimiter="|")
    datos = [nombre, str(telefono), str(cuil)]
    for fila in reader:
        if fila[0] == datos[0] or fila[1] == datos[1] or fila[2] == datos[2]:
            return True
    Anses.close()
    return False

def registrarCiudadanoAnses(nombre, telefono, cuil):
    verificacion = verificar(nombre, telefono, cuil)
    if verificacion == True:
        print("Ya existis ;)")
    elif verificacion == False:
        Anses = open("Anses.csv", "a", newline="")
        writer = csv.writer(Anses, delimiter="|")
        datos = [nombre, telefono, cuil]
        writer.writerow(datos)
        Anses.close()
        print("Registrado")

def CitizenLogIn():
    while True:
        try:
            dato = input("Ingrese su Cuil: ")
            if Checker.CheckCuil(str(dato)) == False:
                raise ErrorCuil()
            break
        except ValueError:
            print("Ingrese el valor solicitado")
        except Exception:
            print("Ingrese su Cuil de 11 digitos ;)")
    print("Se ha iniciado sesion")
    #Instanciar Ciudadano??!


def CitizenChoices(ciudadano):
    pass


class NonAdminError(Exception):
    msg = "None pa ;)"

def AdminLoop():
    counter = 0
    while counter < 3:
        try:
            contrasena = input("Ingrese la contraseña de Administrador: ")
            if contrasena == "Sumbudrule":
                print("Creaste un Admin!!!!!!!!!")
                return -1   #llamo a AdminChoices(admin)
            elif contrasena != "Sumbudrule":
                raise NonAdminError()
            break
        except:
            print("Si sos admin, poné bien la contra ;)")
            counter += 1
    print("Vos no sos Admin, comunicate con un psicologo")
    print("...Volviendo al inicio...")
    Choice()


def AdminChoices(admin):
    while True:
        try:
            accion = int(input("Si esta registrado presione 1, si quiere registrarse presione 2: "))
            break
        except ValueError:
            print("Ingrese el numero solicitado")
Choice()


#Como hacer para que no existan dos personas con el mismo cuil, mismo telefono, mismo nombre --> LISTO
# Ciudadano choices y admin choices
    # guarda con los loops y los breaks
#holz
#PREGUNTA: Como hacer con los errorCuil y errorTelefono
#ingles --> interfaz
#español --> internas

# valen --> hace un archivo con todas las funciones internas


