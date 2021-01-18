from ...core.model.absmodel import AbsModel
from ...banco.model.banco import Banco


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

    def get_banco_1(self):
        """
        Remetentente
        :return: Banco Instance
        """
        return self._banco_1

    def get_banco_2(self):
        """
        Beneficiado
        :return: Banco Instance
        """
        return self._banco_2
