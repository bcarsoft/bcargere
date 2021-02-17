from abc import ABCMeta


class IServiceVariacao(metaclass=ABCMeta):
    """Classe abstrata que simula interface.
    bcarsoft
    """

    def create_variacao(self, variacao):
        pass

    def update_variacao(self, variacao):
        pass

    def find_variacao(self, variacao):
        pass

    def delete_variacao(self, **kwargs):
        pass
