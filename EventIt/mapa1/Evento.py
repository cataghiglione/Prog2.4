class Evento:

    def __init__(self,x,y, name, type, cantidadPersonas):
        self.__type = type
        self.__x = x
        self.__y = y
        self.__name = name
        self.__cantidadPersonas = cantidadPersonas

    def __repr__(self):
        return f"soy {self.__name}"

    def getType(self):
        return self.__type

    def getName(self):
        return self.__name

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getCantidad(self):
        return self.__cantidadPersonas
