from tkinter import Tk

from tp.mapa1.Mapa import Mapa, Evento, a


b = Mapa()
b.AgregarBoton(Evento(50,30, 'Pilar', 'Educación'))
print(b.getEventos())
b.ReiniciarBotones()
b.VerMapa()