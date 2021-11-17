# from matplotlib import pyplot as plt

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

    @classmethod
    def Picos(cls, eventos):
        lista = []
        while True:
            maximo = MaximoPersonas.getMaximo(eventos)
            lista.append(maximo)
            eventos.remove(maximo)
            if len(eventos) == 0:
                break
        for evento in lista:
            plt.stem(evento.getName(), evento.getCantidad())
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
