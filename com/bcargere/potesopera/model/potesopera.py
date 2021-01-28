from decimal import Decimal
from com.bcargere.core.model.absmodel import AbsModel
from com.bcargere.data.model.data import Data
from com.bcargere.potes.model.potes import Potes


class PotesOpera(AbsModel):
    """
    Classe para registro de operações em Potes
    de dinheiro
    bcarsoft
    """

    def __init__(self):
        """Construtor"""
        super().__init__()
        self._descricao = ''
        self._pote_1 = Potes()
        self._pote_2 = Potes()
        self._data = Data()
        self._dinheiro = Decimal('0.00')

    # getters and setters

    @property
    def descricao(self):
        """
        Retorna a descricao da operação.
        :return: str
        """
        return self._descricao

    @descricao.setter
    def descricao(self, descricao: str):
        """
        Insere uma descricao para operação.
        :param descricao: str
        """
        self._descricao = descricao

    @property
    def pote_1(self):
        """
        Remetentente
        :return: Potes Instance
        """
        return self._pote_1

    @property
    def pote_2(self):
        """
        Beneficiado
        :return: Potes Instance
        """
        return self._pote_2

    @property
    def data(self):
        """
        Inserir data.
        :return: Data instance
        """
        return self._data

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
