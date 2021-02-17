from abc import ABCMeta


class IServiceBanco(metaclass=ABCMeta):
    """Classe abstrata que simula interface.
    bcarsoft
    """

    def create_banco(self, banco):
        pass

    def update_banco(self, banco):
        pass

    def delete_banco(self, banco):
        pass

    def find_banco(self, **kwargs):
        pass
