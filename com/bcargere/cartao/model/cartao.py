from ...core.model.absmodel import AbsModel
from ...data.model.data import DataCartao
from decimal import Decimal, getcontext


class Cartao(AbsModel):
    """
        Classe para registro de cartões de
        - crédito
        - débito
        - pré pago
        bcarsoft
    """

    def __init__(self):
        """Construtor"""
        super().__init__()
        self._bandeira = ''
        self._conta = 0
        self._tipo = ''
        self._nome_cartao = ''
        self._numero = ''
        self._data_venc = DataCartao()
        self._codigo = ''
        self._limite = Decimal('0.00')

    # getters and setters

    def set_bandeira(self, bandeira: str):
        """
        Empresa que opera o cartão
        :param bandeira: str
        """
        self._bandeira = bandeira

    def get_bandeira(self):
        """
        Retorna a bandeira do cartão
        :return: str
        """
        return self._bandeira

    def set_fk(self, fk: int):
        """
        É uma chave para a conta bancária vinculada
        :param fk: int
        """
        super().set_fk(fk)

    def get_fk(self):
        """
        Retorna a chave da conta bancária vinculada
        :return: int
        """
        return super().get_fk()

    def set_tipo(self, tipo: str):
        """
        Insere o tipo de operação do cartão
        :param tipo: str
        """
        self._tipo = tipo

    def get_tipo(self):
        """
        Retorna o tipo de operação do cartão
        :return: str
        """
        return self._tipo

    def set_nome_cartao(self, nome_cartao: str):
        """
        Insere nome do proprietário do cartão
        :param nome_cartao: str
        """
        self._nome_cartao = nome_cartao

    def get_nome_cartao(self):
        """
        Retona nome do proprietário do cartão
        :return: str
        """
        return self._nome_cartao

    def set_numero(self, numero: str):
        """
        Insere numero do cartão
        :param numero: str
        """
        self._numero = numero

    def get_numero(self):
        """
        Retorna numero do cartão
        :return: str
        """
        return self._numero

    def get_data_venc(self):
        """
        Retorna o objeto com a data de vencimento
        :return: DataCartao instance
        """
        return self._data_venc

    def set_codigo(self, codigo: str):
        """
        Insere codigo do cartão
        :param codigo: str
        """
        self._codigo = codigo

    def get_codigo(self):
        """
        Retorna número do cartão
        :return: str
        """
        return self._codigo

    def set_limite(self, limite=Decimal('0.00')):
        """
        Insere valor de limite ao cartão
        :param limite: Decimal instance
        """
        getcontext().prec = 2
        self._limite = limite

    def get_limite(self):
        """
        Retorna o limite do cartão
        :return: Decimal instance
        """
        return self._limite
