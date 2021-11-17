from collections import defaultdict
from EventIt.exceptions import e


class Diccionario:

    def __init__(self):
        self.dict = defaultdict()

    def agregar(self, cuil, ciudadano):
        self.dict[cuil] = ciudadano

    def quitar(self, cuil):
        try:
            for key, value in self.dict.items():
                if key == cuil:
                    self.dict.pop(key)
                    return True
            raise e.Error()
        except e.Error:
            return e.Error.ErrorMsg('El cuil no fue encontrado.')

    def buscar(self, cuil):
        try:
            for key, value in self.dict.items():
                if key == cuil:
                    return value
            raise e.Error()
        except e.Error:
            return e.Error.ErrorMsg('El cuil no fue encontrado.')


ciudadanoList = Diccionario()

# try:
#     ciudadanoList.agregar('Valentina', 12345678999)
# except e.Error:
#     print('algo, cualquier cosa')

