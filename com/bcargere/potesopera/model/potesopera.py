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

    def set_descricao(self, descricao: str):
        """
        Insere uma descricao para operação.
        :param descricao: str
        """
        self._descricao = descricao

    def get_descricao(self):
        """
        Retorna a descricao da operação.
        :return: str
        """
        return self._descricao

    def get_pote_1(self):
        """
        Remetentente
        :return: Potes Instance
        """
        return self._pote_1

    def get_pote_2(self):
        """
        Beneficiado
        :return: Potes Instance
        """
        return self._pote_2

    def get_data(self):
        """
        Inserir data.
        :return: Data instance
        """
        return self._data

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
