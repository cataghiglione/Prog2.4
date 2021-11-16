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
        if evento.getCantidad() >= 100:
            color = "red"
        elif evento.getCantidad() >= 50:
            color = "yellow"
        else:
            color = "green"
        super().__init__(master=raiz, command= self.showinfoB, text=evento.getName(), bg= color)
        self.__evento = evento

    def __repr__(self):
        return f"Soy el boton de {self.__evento.getName()}"

    def showinfoB(self):
        msg1 = self.__evento.getType()
        messagebox.showinfo(message=f"Evento de {msg1}. \nHay {self.__evento.getCantidad()} personas ")

    def getEvento(self):
        return self.__evento



