class Data:
    """
        Data de calendário, modelo de classe com três inteiros
        bcarsoft
    """

    def __init__(self):
        """Construtor"""
        self._dia = 0
        self._mes = 0
        self._ano = 0

    # getters and setters

    @property
    def dia(self):
        """
        Esse metodo retorna o dia
        :return: int
        """
        return self._dia

    @dia.setter
    def dia(self, dia=1):
        """
        Esse metodo insere o dia do mês
        :param dia: int
        """
        self._dia = dia

    @property
    def mes(self):
        """
        Esse metodo retorna o mes
        :return: int
        """
        return self._mes

    @mes.setter
    def mes(self, mes=1):
        """
        Esse metodo insere o mês
        :param mes: int
        """
        self._mes = mes

    @property
    def ano(self):
        """
        Esse metodo retorna o ano
        :return: int
        """
        return self._ano

    @ano.setter
    def ano(self, ano=1970):
        """
        Esse metodo insere o ano
        :param ano: int
        """
        self._ano = ano


class DataCartao:
    """
        Classe modelo para data especial inserida
        nos cartões de pagamentos.
        bcarsoft
    """

    def __init__(self):
        self._mes = 1
        self._ano = 2000

    # getters and setters

    @property
    def mes(self):
        """
        Esse metodo retorna o mes
        :return: int
        """
        return self._mes

    @mes.setter
    def mes(self, mes=1):
        """
        Esse metodo insere o mês
        :param mes: int
        """
        self._mes = mes

    @property
    def ano(self):
        """
        Esse metodo retorna o ano
        :return: int
        """
        return self._ano

    @ano.setter
    def ano(self, ano=1970):
        """
        Esse metodo insere o ano
        :param ano: int
        """
        self._ano = ano
