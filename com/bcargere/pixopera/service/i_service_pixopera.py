from abc import ABCMeta


class IServicePixOpera(metaclass=ABCMeta):
    """Classe abstrata que simula interface.
    bcarsoft
    """

    def create_pixopera(self, pixopera):
        pass

    def delete_pixopera(self, pixopera):
        pass

    def find_pixopera(self, **kwargs):
        pass
