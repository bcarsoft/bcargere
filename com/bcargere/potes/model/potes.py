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

    def set_nome(self, nome):
        """
        Insira um nome ao pote.
        :param nome: str
        """
        self._nome = nome

    def get_nome(self):
        """
        Retorna o nome do pote.
        :return: str
        """
        return self._nome

    def set_descricao(self, descricao='Ponte de Dinheiro'):
        """
        Insira uma descrição para o pote
        :param descricao: str
        """
        self._descricao = descricao

    def get_descricao(self):
        """
        Retorna a Descricao
        :return: str
        """
        return self._descricao

    def set_dinheiro(self, dinheiro=Decimal('0.00')):
        """
        Colocar dinheiro no pote
        :param dinheiro: Decimal instance
        """
        self._dinheiro = dinheiro

    def get_dinheiro(self):
        """
        Retornar o valor monetário no pote.
        :return: Decimal instance
        """
        return self._dinheiro
