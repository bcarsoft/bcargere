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

    def set_id(self, id: int):
        """
        Insere Chave Primária
        :param id: int
        """
        self._id = id

    def get_id(self):
        """
        Retorna Chave Primária
        :return: int
        """
        return self._id

    def set_fk(self, fk: int):
        """
        Insere Chave Estrangeira
        :param fk: int
        """
        self._fk = fk

    def get_fk(self):
        """
        Retorna Chave Estrangeira
        :return: int
        """
        return self._fk
