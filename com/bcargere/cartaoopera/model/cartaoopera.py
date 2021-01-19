from decimal import Decimal, getcontext
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

    def get_cartao(self):
        """
        Retorna o cartão.
        :return: Cartao instance
        """
        return self._cartao

    def set_nome(self, nome: str):
        """
        Esse metodo insere o nome
        :param nome: str
        """
        self._nome = nome

    def get_nome(self):
        """
        Esse metodo retorna o nome
        :return: str
        """
        return self._nome

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

    def set_valor(self, valor=Decimal('0.00')):
        """
        Insere valor da compra.
        :param valor: Decimal instance
        """
        getcontext().prec = 2
        self._valor = valor

    def get_valor(self):
        """
        Retorna valor da compra.
        :return: Decimal instance
        """
        return self._valor

    def get_data(self):
        """
        Inserir data.
        :return: Data instance
        """
        return self._data

    def set_done(self, done=False):
        """
        Aprova ou não a compra.
        :param done: bool
        """
        self._done = done

    def is_done(self):
        """
        Retorna se a compra foi ou não aprovada.
        :return: bool
        """
        return self._done
