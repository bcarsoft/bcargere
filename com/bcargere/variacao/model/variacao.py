from decimal import Decimal
from com.bcargere.core.model.absmodel import AbsModel


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

    @property
    def numero(self):
        """
        Retorna numero da variacao
        :return: int
        """
        return self._numero

    @numero.setter
    def numero(self, numero: int):
        """
        Insere numero da variação
        :param numero: int
        """
        self._numero = numero

    @property
    def dinheiro(self):
        """
        Retorna valor da variação
        :return: Decimal instance
        """
        return self._dinheiro

    @dinheiro.setter
    def dinheiro(self, dinheiro=Decimal('0.00')):
        """
        Insere Valor Monetário
        :param dinheiro: Decimal instance
        """
        self._dinheiro = dinheiro
