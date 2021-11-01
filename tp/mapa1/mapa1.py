from tkinter import Tk

from tp.mapa1.Mapa import Mapa, Evento
print(Mapa.master)
b = Mapa()
b.ReiniciarBotones()
b.AgregarBoton(Evento(50,30, 'Pilar', 'Educación'))
print(b.getEventos())
b.VerMapa()