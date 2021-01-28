from decimal import Decimal
from com.bcargere.core.model.absmodel import AbsModel
from com.bcargere.cartao.model.cartao import Cartao
from com.bcargere.data.model.data import Data


class CartaoOpera(AbsModel):
    """
    Registra operações do cartão.
    bcarsoft
    """

    def __init__(self):
        """Construtor"""
        super().__init__()
        self._cartao = Cartao()
        self._nome = ''
        self._descricao = ''
        self._valor = Decimal('0.00')
        self._data = Data()
        self._done = False

    # getters and setters

    @property
    def cartao(self):
        """
        Retorna o cartão.
        :return: Cartao instance
        """
        return self._cartao

    @property
    def nome(self):
        """
        Esse metodo retorna o nome
        :return: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        """
        Esse metodo insere o nome
        :param nome: str
        """
        self._nome = nome

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
    def valor(self):
        """
        Retorna valor da compra.
        :return: Decimal instance
        """
        return self._valor

    @valor.setter
    def valor(self, valor=Decimal('0.00')):
        """
        Insere valor da compra.
        :param valor: Decimal instance
        """
        self._valor = valor

    @property
    def data(self):
        """
        Inserir data.
        :return: Data instance
        """
        return self._data

    @property
    def done(self):
        """
        Retorna se a compra foi ou não aprovada.
        :return: bool
        """
        return self._done

    @done.setter
    def done(self, done=False):
        """
        Aprova ou não a compra.
        :param done: bool
        """
        self._done = done
