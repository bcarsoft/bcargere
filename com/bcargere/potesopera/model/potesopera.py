from ...core.model.absmodel import AbsModel
from ...potes.model.potes import Potes


class PotesOpera(AbsModel):
    """
    Classe para registro de operações em Potes
    de dinheiro
    bcarsoft
    """

    def __init__(self):
        """Construtor"""
        super().__init__()
        self._descricao = ''
        self._pote_1 = Potes()
        self._pote_2 = Potes()

    # getters and setters

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

    def get_pote_1(self):
        """
        Remetentente
        :return: Potes Instance
        """
        return self._pote_1

    def get_pote_2(self):
        """
        Beneficiado
        :return: Potes Instance
        """
        return self._pote_2
