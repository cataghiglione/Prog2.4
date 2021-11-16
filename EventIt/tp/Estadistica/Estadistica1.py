from matplotlib import pyplot as plt

class Tablero:

    @classmethod
    def ranking(cls, eventos):
        posibles_maximos = MaximoPersonas.getMaximos3(eventos)
        maximoA = MaximoPersonas.getMaximo(posibles_maximos)
        plt.stem(maximoA.getName(), maximoA.getCantidad())
        posibles_maximos.remove(maximoA)
        maximoB= MaximoPersonas.getMaximo(posibles_maximos)
        plt.stem(maximoB.getName(), maximoB.getCantidad())
        posibles_maximos.remove(maximoB)
        maximoC=MaximoPersonas.getMaximo(posibles_maximos)
        plt.stem(maximoC.getName(), maximoC.getCantidad())
        plt.show()

class MaximoPersonas:

    @classmethod
    def getMaximo(cls, eventos):
        maxevento = None
        for evento in eventos:
            if maxevento == None:
                maxevento = evento
            elif maxevento != None:
                if maxevento.getCantidad() < evento.getCantidad():
                    maxevento = evento
        if maxevento != None:
            return maxevento
        elif maxevento == None:
            print("Hay error")

    @classmethod
    def getMaximos3(self, eventos):
        maximoA = MaximoPersonas.getMaximo(eventos)
        eventos.remove(maximoA)
        maximoB = MaximoPersonas.getMaximo(eventos)
        eventos.remove(maximoB)
        maximoC = MaximoPersonas.getMaximo(eventos)
        posibles_maximos = [maximoA, maximoB, maximoC]
        return posibles_maximos

#class FakeEvento:
 #   def __init__(self, nombre, cantidad):
  #      self.cantidad = cantidad
   #     self.nombre = nombre
  #  def __repr__(self):
  #      return f"{self.cantidad}"
   # def getCantidad(self):
   #     return self.cantidad
   # def getName(self):
   #     return self.nombre

#mievento = FakeEvento("Palermo", 20)
#tuevento = FakeEvento("Himalaya", 2)
#nuestroevento = FakeEvento("NuevaZelanda", 40)

