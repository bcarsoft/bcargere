from abc import ABCMeta


class IServiceCartaoOpera(metaclass=ABCMeta):
    """Classe abstrata que simula interface.
    bcarsoft
    """

    def create_cartaoopera(self, cartaoopera):
        pass

    def delete_cartaoopera(self, cartaoopera):
        pass

    def find_cartaoopera(self, **kwargs):
        pass
