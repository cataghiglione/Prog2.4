from tkinter import *
from tkinter import messagebox

class Mapa:
    __eventos = []
    __botones = []
    master = Tk()
    def __init__(self):

        self.frame = Frame(Mapa.master)
        self.frame.config(bg="grey")
        self.frame.pack()

        self.imagen = PhotoImage(file="coni.png")
        self.label = Label(self.frame, image=self.imagen)
        self.label.pack()
        self.master.geometry(f'{self.imagen.width()}x{self.imagen.height()}')
        self.master.resizable(0,0)



    def AgregarBoton(self, evento):
        boton= MiBoton(self.frame, evento)
        boton.place(x=str(evento.getX()), y=str(evento.getY()))
        boton.config(width="12", height="1")
        if evento not in Mapa.__eventos:
            Mapa.__eventos.append(evento)
        Mapa.__botones.append(boton)

    def ReiniciarBotones(self):
        for evento in Mapa.__eventos:
            Mapa.__botones = []
            self.AgregarBoton(evento)

    def BorrarBoton(self, evento):
        newListEvent = Mapa.__eventos
        newListBoton = Mapa.__botones
        for i in Mapa.__eventos:
            if i == evento:
                newListEvent.remove(i)
                for boton in Mapa.__botones:
                    if boton.getEvento() == evento:
                        boton.destroy()
                        newListBoton.remove(boton)
        Mapa.__botones = newListBoton
        Mapa.__eventos = newListEvent

    def VerMapa(self):
        Mapa.master.mainloop()

    def getEventos(self):
        return Mapa.__eventos

    def getBotones(self):
        return Mapa.__botones

class MiBoton(Button):
    def __init__(self,raiz, evento):
        super().__init__(master=raiz, command= self.showinfoB, text=evento.getName())
        self.__evento = evento

    def __repr__(self):
        return f"Soy el boton de {self.__evento.getName()}"

    def showinfoB(self):
        msg1 = self.__evento.getType()
        messagebox.showinfo(message=f"evento de {msg1}")

    def getEvento(self):
        return self.__evento


class Evento:

    def __init__(self,x,y, name, type):
        self.__type = type
        self.__x = x
        self.__y = y
        self.__name = name

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


a= Mapa()
mievento = Evento(200, 100, "Palermo", "Seguridad")
tuevento = Evento(400,200, "San Isidro", "Medicina")
a.AgregarBoton(mievento)
a.AgregarBoton(tuevento)
a.BorrarBoton(mievento)
a.ReiniciarBotones()
# a.AgregarBoton(Evento(50,30, 'Pilar', 'Educación'))
# a.VerMapa()
# b = Mapa()
# b.ReiniciarBotones()
# b.AgregarBoton(Evento(50,30, 'Pilar', 'Educación'))
# print(b.getEventos())
# b.VerMapa()
