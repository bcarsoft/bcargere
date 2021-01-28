from com.bcargere.core.model.absmodel import AbsModel
from com.bcargere.data.model.data import Data


class Banco(AbsModel):
    """
        Para registro de contas bancárias
        bcarsoft
    """

    def __init__(self):
        """Construtor"""
        super().__init__()
        self._nome = ''
        self._codigo = ''
        self._num_agencia = ''
        self._num_conta = ''
        self._tipo = ''
        self._titular = ''
        self._genero = ''
        self._data_nas = Data()
        self._senha1 = ''
        self._senha2 = ''

    # getters and setters

    @property
    def nome(self):
        """
        Retorna Nome do Banco
        :return: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        """
        Insere Nome do Banco
        :param name: str
        """
        self._nome = nome

    @property
    def codigo(self):
        """
        Retorna Codigo do Banco
        :return: str
        """
        return self._codigo

    @codigo.setter
    def codigo(self, codigo: str):
        """
        Insere Código do Banco
        :param codigo: str
        """
        self._codigo = codigo

    @property
    def num_agencia(self):
        """
        Retorna Número de Agência
        :return: str
        """
        return self._num_agencia

    @num_agencia.setter
    def num_agencia(self, num_agencia: str):
        """
        Insere Número de Agência
        :param num_agencia: str
        """
        self._num_agencia = num_agencia

    @property
    def num_conta(self):
        """
        Retorna Número de Conta
        :return: str
        """
        return self._num_conta

    @num_conta.setter
    def num_conta(self, num_conta: str):
        """
        Insere Número de Conta
        :param num_conta: str
        """
        self._num_conta = num_conta

    @property
    def tipo(self):
        """
        Retorna Tipo de conta
        :return: str
        """
        return self._tipo

    @tipo.setter
    def tipo(self, tipo: str):
        """
        Insere Tipo de conta
        :param tipo: str
        """
        self._tipo = tipo

    @property
    def titular(self):
        """
        Retorna Nome do titular da conta
        :return: str
        """
        return self._titular

    @titular.setter
    def titular(self, titular: str):
        """
        Insere Nome do titular da conta
        :param titular: str
        """
        self._titular = titular

    @property
    def genero(self):
        """
        Retorna Genero do titular da conta
        :return: str
        """
        return self._genero

    @genero.setter
    def genero(self, genero: str):
        """
        Insere Genero do titular da conta
        :param genero: str
        """
        self._genero = genero

    @property
    def data_nas(self):
        """
        Retorna objeto para registro de data
        :return: Data instance
        """
        return self._data_nas

    @property
    def senha_1(self):
        """
        Retorna Senha 1 (mais curta)
        :return: str
        """
        return self._senha1

    @senha_1.setter
    def senha_1(self, senha_1: str):
        """
        Insere Senha 1 (mais curta)
        :param senha_1: str
        """
        self._senha1 = senha_1

    @property
    def senha_2(self):
        """
        Retorna Senha 2 (mais longa)
        :return: str
        """
        return self._senha2

    @senha_2.setter
    def senha_2(self, senha_2: str):
        """
        Insere Senha 2 (mais longa)
        :param senha_2: str
        """
        self._senha2 = senha_2
