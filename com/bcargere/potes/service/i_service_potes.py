from abc import ABCMeta


class IServicePotes(metaclass=ABCMeta):
    """Classe abstrata que simula interface.
    bcarsoft
    """

    def create_potes(self, potes):
        pass

    def update_potes(self, potes):
        pass

    def delete_potes(self, potes):
        pass

    def find_potes(self, **kwargs):
        pass
