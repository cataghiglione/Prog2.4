import unittest
from EventIt.diccionario import ciudadanoList
from EventIt.usuarios.Ciudadano import Ciudadano


# class ProbarTelefonoACuil(unittest.TestCase):
#     def test1(self):
#         c = Efimero.TelefonoACuil(1135655745)
#         self.assertEqual(c, 27439744184)
#
#     def test2(self):
#         c = Efimero.CuilANombre(27439744184)
#         self.assertEqual(c, "Catalina Ghiglione")
#
#     def test3(self):
#         c = Efimero.CuilATelefono(27439744184)
#         self.assertEqual(c, 1135655745)


class ProbarEnviarSolicitud(unittest.TestCase):
    def test1(self):
        cata = Ciudadano("Catalina Ghiglione", 1135655745, 27439744184)
        valen = Ciudadano("Valentina Valenzi", 1137929799, 27447884522)
        ciudadanoList.agregar(27447884522, valen)
        ciudadanoList.agregar(cata.cuil, cata)
        a = cata.mandarSolicitud(27447884522)
        self.assertEqual(a, True)

