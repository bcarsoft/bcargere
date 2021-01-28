from com.bcargere.core.model.absmodel import AbsModel
from decimal import Decimal


class Potes(AbsModel):
    """
        Classe que Registra uma forma de guardar dinheiro
        fisico.
        bcarsoft
    """

    def __init__(self):
        """Construtor"""
        super().__init__()
        self._nome = ''
        self._descricao = ''
        self._dinheiro = Decimal('0.00')

    # getters and setters

    @property
    def nome(self):
        """
        Retorna o nome do pote.
        :return: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Insira um nome ao pote.
        :param nome: str
        """
        self._nome = nome

    @property
    def descricao(self):
        """
        Retorna a Descricao
        :return: str
        """
        return self._descricao

    @descricao.setter
    def descricao(self, descricao='Ponte de Dinheiro'):
        """
        Insira uma descrição para o pote
        :param descricao: str
        """
        self._descricao = descricao

    @property
    def dinheiro(self):
        """
        Retornar o valor monetário no pote.
        :return: Decimal instance
        """
        return self._dinheiro

    @dinheiro.setter
    def dinheiro(self, dinheiro=Decimal('0.00')):
        """
        Colocar dinheiro no pote
        :param dinheiro: Decimal instance
        """
        self._dinheiro = dinheiro
