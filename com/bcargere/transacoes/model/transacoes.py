from decimal import Decimal
from com.bcargere.core.model.absmodel import AbsModel
from com.bcargere.data.model.data import Data
from com.bcargere.banco.model.banco import Banco


class Transacoes(AbsModel):
    """
        Clase para registro de transações financeiras
        bcarsoft
    """

    def __init__(self):
        """Construtor"""
        super().__init__()
        self._descricao = ''
        self._banco_1 = Banco()
        self._banco_2 = Banco()
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
    def banco_1(self):
        """
        Remetentente
        :return: Banco Instance
        """
        return self._banco_1

    @property
    def banco_2(self):
        """
        Beneficiado
        :return: Banco Instance
        """
        return self._banco_2

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
