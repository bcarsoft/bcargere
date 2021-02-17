from abc import ABCMeta


class IServiceTransacoes(metaclass=ABCMeta):
    """Classe abstrata que simula interface.
    bcarsoft
    """

    def create_transacoes(self, transacao):
        pass

    def delete_transacoes(self, transacao):
        pass

    def find_transacoes(self, **kwargs):
        pass
