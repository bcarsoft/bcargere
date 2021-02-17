from abc import ABCMeta


class IServicePotesOpera(metaclass=ABCMeta):
    """Classe abstrata que simula interface.
    bcarsoft
    """

    def create_potesopera(self, potesopera):
        pass

    def delete_potesopera(self, potesopera):
        pass

    def find_potesopera(self, **kwargs):
        pass
