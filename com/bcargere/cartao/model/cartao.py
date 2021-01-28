from com.bcargere.core.model.absmodel import AbsModel
from com.bcargere.data.model.data import DataCartao
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
        self._tipo = ''
        self._nome_cartao = ''
        self._numero = ''
        self._data_venc = DataCartao()
        self._codigo = ''
        self._limite = Decimal('0.00')
        self._excedente = Decimal('0.00')
        self._fatura = Decimal('0.00')

    # getters and setters

    @property
    def bandeira(self):
        """
        Retorna a bandeira do cartão
        :return: str
        """
        return self._bandeira

    @bandeira.setter
    def bandeira(self, bandeira: str):
        """
        Empresa que opera o cartão
        :param bandeira: str
        """
        self._bandeira = bandeira

    @property
    def fk(self):
        """
        Retorna a chave da conta bancária vinculada
        :return: int
        """
        return super().fk

    @fk.setter
    def fk(self, fk: int):
        """
        É uma chave para a conta bancária vinculada
        :param fk: int
        """
        super().fk = fk

    @property
    def tipo(self):
        """
        Retorna o tipo de operação do cartão
        :return: str
        """
        return self._tipo

    @tipo.setter
    def tipo(self, tipo: str):
        """
        Insere o tipo de operação do cartão
        :param tipo: str
        """
        self._tipo = tipo

    @property
    def nome_cartao(self):
        """
        Retona nome do proprietário do cartão
        :return: str
        """
        return self._nome_cartao

    @nome_cartao.setter
    def nome_cartao(self, nome_cartao: str):
        """
        Insere nome do proprietário do cartão
        :param nome_cartao: str
        """
        self._nome_cartao = nome_cartao

    @property
    def numero(self):
        """
        Retorna numero do cartão
        :return: str
        """
        return self._numero

    @numero.setter
    def numero(self, numero: str):
        """
        Insere numero do cartão
        :param numero: str
        """
        self._numero = numero

    @property
    def data_venc(self):
        """
        Retorna o objeto com a data de vencimento
        :return: DataCartao instance
        """
        return self._data_venc

    @property
    def codigo(self):
        """
        Retorna número do cartão
        :return: str
        """
        return self._codigo

    @codigo.setter
    def codigo(self, codigo: str):
        """
        Insere codigo do cartão
        :param codigo: str
        """
        self._codigo = codigo

    @property
    def limite(self):
        """
        Retorna o limite do cartão
        :return: Decimal instance
        """
        return self._limite

    @limite.setter
    def limite(self, limite=Decimal('0.00')):
        """
        Insere valor de limite ao cartão
        :param limite: Decimal instance
        """
        self._limite = limite

    @property
    def excedente(self):
        """
        Retorna valor a mais (deve ser combinado ao limite)
        :return: Decimal instance
        """
        return self._excedente

    @excedente.setter
    def excedente(self, excedente=Decimal('0.00')):
        """
        Insere valor a mais (deve ser combinado ao limite).
        :param excendente: Decimal instance
        """
        self._excedente = excedente

    @property
    def fatura(self):
        """
        Retorna valor da fatura.
        :return: Decimal instance.
        """
        return self._fatura

    @fatura.setter
    def fatura(self, fatura=Decimal('0.00')):
        """
        Insere valor a fatura.
        :param fatura: Decimal instance
        """
        self._fatura = fatura
