from tp.mapa1.Mapa import Mapa, root, Evento

<<<<<<< HEAD
from tp.mapa1.Mapa import Mapa, Evento, a


b = Mapa()
=======
b = Mapa(root)
b.ReiniciarBotones()
>>>>>>> 9561f11a4353a7ed907c3b0a3d914bd1e88afabd
b.AgregarBoton(Evento(50,30, 'Pilar', 'Educación'))
print(b.getEventos())
b.ReiniciarBotones()
b.VerMapa()