from decimal import Decimal
from com.bcargere.core.model.absmodel import AbsModel
from com.bcargere.data.model.data import Data
from com.bcargere.pix.model.pix import Pix


class PixOpera(AbsModel):
    """
    Classe para Operações com Pix
    bcarsoft
    """

    def __init__(self):
        super().__init__()
        self._descricao = ''
        self._pix_1 = Pix()
        self._pix_2 = Pix()
        self._dinheiro = Decimal('0.00')
        self._data = Data()

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
    def pix_1(self):
        """
        Remetentente
        :return: Banco Instance
        """
        return self._pix_1

    @property
    def pix_2(self):
        """
        Beneficiado
        :return: Banco Instance
        """
        return self._pix_2

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

    @property
    def data(self):
        """
        Inserir data.
        :return: Data instance
        """
        return self._data
