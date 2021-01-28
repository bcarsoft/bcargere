class AbsModel:
    """
        Classe abstratra com chave primaria e extrangeira
        - deve ser herdada pelos modelos de base de dados.
        bcarsoft
    """

    def __init__(self):
        """Construtor"""
        self._id = 0
        self._fk = self._id

    # getters and setters

    @property
    def id(self):
        """
        Retorna Chave Primária
        :return: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """
        Insere Chave Primária
        :param id: int
        """
        self._id = id

    @property
    def fk(self):
        """
        Retorna Chave Estrangeira
        :return: int
        """
        return self._fk

    @fk.setter
    def fk(self, fk: int):
        """
        Insere Chave Estrangeira
        :param fk: int
        """
        self._fk = fk
