import csv
from usuarios.usuario import Administrador

#Instancie administrador debido a que se trata siempre del mismo
admin = Administrador()

#cambiar nombre
class Error(Exception):
    msg = "None pa ;)"


def Choice():
    while True:
        try:
            usuario = int(input("Ingrese 1 para Ciudadano o 2 para Admin: "))
            if usuario != 1 and usuario!=2:
                raise Error()
            break
        except ValueError:
            print("Ingrese alguno de los valores solicitados")
        except:
            print("Ingrese uno de los valores especificados")
    if usuario == 1:
        CitizenLoop()
    elif usuario == 2:
        AdminLoop()
    else:
        print("Hay un error obteniendo usuario ;)")


class ErrorCuil(Exception):
    pass

class ErrorTelefono(Exception):
    pass

class Checker():
    @classmethod
    def CheckCuil(self, cuil):
        if len(cuil) == 11:
            return True
        else:
            print("raro")
            return False

    @classmethod
    def CheckTelefono(self, telefono):
        if len(telefono) == 10:
            return True
        else:
            return False


class CiudadanoExisteMismoTelefono(Exception):
    pass


class CiudadanoExisteMismoCuil(Exception):
    pass


class CiudadanoExisteMismoNombre(Exception):
    pass


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
                if verificarDatosNoExistentes(nombre=nombre.title()):
                    raise CiudadanoExisteMismoNombre()
                telefono = int(input("Ingrese su numero de telefono: +54 9 "))
                if verificarDatosNoExistentes(telefono=telefono):
                    raise CiudadanoExisteMismoTelefono()
                if Checker.CheckTelefono(str(telefono)) == False:
                    raise ErrorTelefono()
                cuil = int(input("Ingrese su Cuil: "))
                if verificarDatosNoExistentes(cuil=cuil):
                    raise CiudadanoExisteMismoCuil()
                if Checker.CheckCuil(str(cuil)) == False:
                    raise ErrorCuil()
            except ValueError:
                print("Coloque solo numeros enteros para el telefono y el cuil")
            except ErrorCuil:
                print("Un Cuil posee 11 digitos ;)")
            except ErrorTelefono:
                print("Un Telefono posee 10 digitos ;)")
            except CiudadanoExisteMismoTelefono:
                print("Este telefono ya existe")
            except CiudadanoExisteMismoCuil:
                print("Este Cuil ya existe")
            except CiudadanoExisteMismoNombre:
                print("Este nombre ya existe")
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
        if fila[0] == datos[0]:
            return True
        elif fila[1] == datos[1]:
            return True
        elif fila[2] == datos[2]:
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

