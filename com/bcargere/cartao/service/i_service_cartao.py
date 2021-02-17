from abc import ABCMeta


class IServiceCartao(metaclass=ABCMeta):
    """Classe abstrata que simula interface.
    bcarsoft
    """

    def create_cartao(self, cartao):
        pass

    def update_cartao(self, cartao):
        pass

    def delete_cartao(self, cartao):
        pass

    def find_cartao(self, **kwargs):
        pass