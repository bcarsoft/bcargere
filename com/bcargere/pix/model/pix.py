from com.bcargere.core.model.absmodel import AbsModel


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

    @property
    def chave(self):
        """
        Retorna Chave Pix
        :return: str
        """
        return self._chave

    @chave.setter
    def chave(self, chave: str):
        """
        Insere Chave Pix.
        :param chave: str
        """
        self._chave = chave

    @property
    def nome(self):
        """
        Retorna nome da Chave.
        :return: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        """
        Insere nome da Chave.
        :param nome: str
        """
        self._nome = nome
