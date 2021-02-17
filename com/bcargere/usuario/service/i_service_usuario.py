from abc import ABCMeta


class IServiceUsuario(metaclass=ABCMeta):
    """Classe abstrata que simula interface.
    bcarsoft
    """

    def create_usuario(self, user):
        pass

    def update_usuario(self, user):
        pass

    def delete_usuario(self, user):
        pass

    def find_usuario(self, **kwargs):
        pass
