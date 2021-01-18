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

    def set_dia(self, dia=1):
        """
        Esse metodo insere o dia do mês
        :param dia: int
        """
        self._dia = dia

    def get_dia(self):
        """
        Esse metodo retorna o dia
        :return: int
        """
        return self._dia

    def set_mes(self, mes=1):
        """
        Esse metodo insere o mês
        :param mes: int
        """
        self._mes = mes

    def get_mes(self):
        """
        Esse metodo retorna o mes
        :return: int
        """
        return self._mes

    def set_ano(self, ano=1970):
        """
        Esse metodo insere o ano
        :param ano: int
        """
        self._ano = ano

    def get_ano(self):
        """
        Esse metodo retorna o ano
        :return: int
        """
        return self._ano


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

    def set_mes(self, mes=1):
        """
        Esse metodo insere o mês
        :param mes: int
        """
        self._mes = mes

    def get_mes(self):
        """
        Esse metodo retorna o mes
        :return: int
        """
        return self._mes

    def set_ano(self, ano=1970):
        """
        Esse metodo insere o ano
        :param ano: int
        """
        self._ano = ano

    def get_ano(self):
        """
        Esse metodo retorna o ano
        :return: int
        """
        return self._ano
