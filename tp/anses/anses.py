class Anses:
    cuiles= [27439744184, 27448285735, 27447884521, 20443672886]
    telefonos = [5491135655745, 5491131568250, 5491137929799, 5491162927781]

    def validar(self, cuil, numero):
        if cuil in self.cuiles:
            if numero in self.telefonos:
                return True

