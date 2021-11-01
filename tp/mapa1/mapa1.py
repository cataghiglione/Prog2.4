from tp.mapa1.Mapa import Mapa, root, Evento

b = Mapa(root)
b.ReiniciarBotones()
b.AgregarBoton(Evento(50,30, 'Pilar', 'Educación'))
print(b.getEventos())
b.VerMapa()