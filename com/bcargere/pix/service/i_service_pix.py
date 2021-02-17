from abc import ABCMeta


class IServicePix(metaclass=ABCMeta):
    """Classe abstrata que simula interface.
    bcarsoft
    """

    def create_pix(self, pix):
        pass

    def update_pix(self, pix):
        pass

    def delete_pix(self, pix):
        pass

    def find_pix(self, **kwargs):
        pass
