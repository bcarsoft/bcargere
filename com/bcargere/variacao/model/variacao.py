from decimal import Decimal
from ...core.model.absmodel import AbsModel


class Variacao(AbsModel):
    """
        Classe que cria variação ou atualiza os valores
        da mesma.
        bcarsoft
    """

    def __init__(self):
        """Construtor"""
        super().__init__()
        self._numero = 0
        self._dinheiro = Decimal('0.00')

    # getters and setters

    def set_fk(self, fk: int):
        """
        Insere chave para conta bancária
        :param fk: int
        """
        super().set_fk(fk)

    def get_fk(self):
        """
        Retorna chave para conta bancária
        :return: int
        """
        return super().get_fk()

    def set_numero(self, numero: int):
        """
        Insere numero da variação
        :param numero: int
        """
        self._numero = numero

    def get_numero(self):
        """
        Retorna numero da variacao
        :return: int
        """
        return self._numero

    def set_dinheiro(self, dinheiro=Decimal('0.00')):
        """
        Insere Valor Monetário
        :param dinheiro: Decimal instance
        """
        self._dinheiro = dinheiro

    def get_dinheiro(self):
        """
        Retorna valor da variação
        :return: Decimal instance
        """
        return self._dinheiro
