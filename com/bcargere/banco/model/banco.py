from ...core.model.absmodel import AbsModel
from ...data.model.data import Data


class Banco(AbsModel):
    """
        Para registro de contas bancárias
        bcarsoft
    """

    def __init__(self):
        """Construtor"""
        super().__init__()
        self._nome = ''
        self._codigo = 0
        self._num_agencia = ''
        self._num_conta = ''
        self._tipo = ''
        self._titular = ''
        self._genero = ''
        self._data_nas = Data()
        self._senha1 = ''
        self._senha2 = ''

    # getters and setters

    def set_nome(self, nome: str):
        """
        Insere Nome do Banco
        :param nome: str
        """
        self._nome = nome

    def get_nome(self):
        """
        Retorna Nome do Banco
        :return: str
        """
        return self._nome

    def set_codigo(self, codigo: int):
        """
        Insere Código do Banco
        :param codigo: int
        """
        self._codigo = codigo

    def get_codigo(self):
        """
        Retorna Codigo do Banco
        :return: str
        """
        return self._codigo

    def set_num_agencia(self, num_agencia: str):
        """
        Insere Número de Agência
        :param num_agencia: str
        """
        self._num_agencia = num_agencia

    def get_num_agencia(self):
        """
        Retorna Número de Agência
        :return: str
        """
        return self._num_agencia

    def set_num_conta(self, num_conta: str):
        """
        Insere Número de Conta
        :param num_conta: str
        """
        self._num_conta = num_conta

    def get_num_conta(self):
        """
        Retorna Número de Conta
        :return: str
        """
        return self._num_conta

    def set_tipo(self, tipo: str):
        """
        Insere Tipo de conta
        :param tipo: str
        """
        self._tipo = tipo

    def get_tipo(self):
        """
        Retorna Tipo de conta
        :return: str
        """
        return self._tipo

    def set_titular(self, titular: str):
        """
        Insere Nome do titular da conta
        :param titular: str
        """
        self._titular = titular

    def get_titular(self):
        """
        Retorna Nome do titular da conta
        :return: str
        """
        return self._titular

    def set_genero(self, genero: str):
        """
        Insere Genero do titular da conta
        :param genero: str
        """
        self._genero = genero

    def get_genero(self):
        """
        Retorna Genero do titular da conta
        :return: str
        """
        return self._genero

    def get_data_nas(self):
        """
        Retorna objeto para registro de data
        :return: Data instance
        """
        return self._data_nas

    def set_senha_1(self, senha1: str):
        """
        Insere Senha 1 (mais curta)
        :param senha1: str
        """
        self._senha1 = senha1

    def get_senha_1(self):
        """
        Retorna Senha 1 (mais curta)
        :return: str
        """
        return self._senha1

    def set_senha_2(self, senha2: str):
        """
        Insere Senha 2 (mais longa)
        :param senha2: str
        """
        self._senha2 = senha2

    def get_senha_2(self):
        """
        Retorna Senha 2 (mais longo)
        :return: str
        """
        return self._senha2
