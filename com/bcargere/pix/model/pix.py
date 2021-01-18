from ...core.model.absmodel import AbsModel


class Pix(AbsModel):
    """
        Classe para registro de Chaves Pix's
        bcarsoft
    """

    def __init__(self):
        super().__init__()
        self._chave = ''
        self._nome = ''

    # getters and setters

    def set_fk(self, fk: int):
        """
        Insere a chave da conta de banco vinculada
        :param fk: int
        """
        super().set_fk(fk)

    def get_fk(self):
        """
        Retorna a chave da conta de banco vinculada
        :return: int
        """
        return super().get_fk()

    def set_chave(self, chave: str):
        """
        Insere Chave Pix.
        :param chave: str
        """
        self._chave = chave

    def get_chave(self):
        """
        Retorna Chave Pix
        :return: str
        """
        return self._chave

    def set_nome(self, nome: str):
        """
        Insere nome da Chave.
        :param nome: str
        """
        self._nome = nome

    def get_nome(self):
        """
        Retorna nome da Chave.
        :return: str
        """
        return self._nome
