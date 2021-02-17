from abc import ABCMeta


class IFacade(metaclass=ABCMeta):
    """Classe abstrata que simula interface.
    bcarsoft
    """

    # banco

    def create_banco(self, banco):
        pass

    def update_banco(self, banco):
        pass

    def delete_banco(self, banco):
        pass

    def find_banco(self, **kwargs):
        pass

    # cartão

    def create_cartao(self, cartao):
        pass

    def update_cartao(self, cartao):
        pass

    def delete_cartao(self, cartao):
        pass

    def find_cartao(self, **kwargs):
        pass

    # cartao opera

    def create_cartaoopera(self, cartaoopera):
        pass

    def delete_cartaoopera(self, cartaoopera):
        pass

    def find_cartaoopera(self, **kwargs):
        pass

    # pix

    def create_pix(self, pix):
        pass

    def update_pix(self, pix):
        pass

    def delete_pix(self, pix):
        pass

    def find_pix(self, **kwargs):
        pass

    # pix opera

    def create_pixopera(self, pixopera):
        pass

    def delete_pixopera(self, pixopera):
        pass

    def find_pixopera(self, **kwargs):
        pass

    # potes

    def create_potes(self, potes):
        pass

    def update_potes(self, potes):
        pass

    def delete_potes(self, potes):
        pass

    def find_potes(self, **kwargs):
        pass

    # potes opera

    def create_potesopera(self, potesopera):
        pass

    def delete_potesopera(self, potesopera):
        pass

    def find_potesopera(self, **kwargs):
        pass

    # transacoes

    def create_transacoes(self, transacao):
        pass

    def delete_transacoes(self, transacao):
        pass

    def find_transacoes(self, **kwargs):
        pass

    # usuario

    def create_usuario(self, user):
        pass

    def update_usuario(self, user):
        pass

    def delete_usuario(self, user):
        pass

    def find_usuario(self, **kwargs):
        pass

    # variacao

    def create_variacao(self, variacao):
        pass

    def update_variacao(self, variacao):
        pass

    def find_variacao(self, **kwargs):
        pass

    def delete_variacao(self, variacao):
        pass

    # end
