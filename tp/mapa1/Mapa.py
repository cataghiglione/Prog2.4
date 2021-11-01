from tkinter import *
from tkinter import messagebox

class Mapa:
    __eventos = []
    __botones = []

    def __init__(self, master):
        self.master = master

        self.frame = Frame(master)
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
        Mapa.__eventos.append(evento)
        self.__botones.append(boton)

    def ReiniciarBotones(self):
        for evento in Mapa.__eventos:
            self.__botones = []
            boton = MiBoton(self.frame, evento)
            boton.place(x=str(evento.getX()), y=str(evento.getY()))
            boton.config(width="12", height="1")
            self.__botones.append(boton)

    def BorrarBoton(self, evento):
        newListEvent = Mapa.__eventos
        newListBoton = self.__botones
        for i in Mapa.__eventos:
            if i == evento:
                newListEvent.remove(i)
                for boton in self.__botones:
                    if boton.getEvento() == evento:
                        boton.destroy()
                        newListBoton.remove(boton)
        self.__botones = newListBoton
        Mapa.__eventos = newListEvent

    def VerMapa(self):
        self.master.mainloop()

    def getEventos(self):
        return Mapa.__eventos

    def getBotones(self):
        return self.__botones

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


root = Tk()
a= Mapa(root)
mievento = Evento(200, 100, "Palermo", "Seguridad")
tuevento = Evento(400,200, "San Isidro", "Medicina")
a.AgregarBoton(mievento)
a.AgregarBoton(tuevento)
a.BorrarBoton(mievento)
a.ReiniciarBotones()

a.VerMapa()




