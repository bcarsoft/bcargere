from datetime import datetime
from com.bcargere.data.model.data import Data
from com.bcargere.data.model.data import DataCartao
from tools.instance_check.instance import Instan


class DataCheck:
    """
    Essa classe verifica se uma data é valida.
    bcarsoft
    """

    def __init__(self):
        pass

    def is_data_valida(self, data):
        """
        Esse metodo valida uma data.
        :param data: Data/DataCartao instance
        :return: bool
        """
        if Instan.get_instance(data, Data):
            return self._checar_data_completa(data)
        elif Instan.get_instance(data, DataCartao):
            return self._checar_data_cartao(data)
        return False

    # data completa

    def _checar_data_completa(self, data: Data):
        """
        Esse metodo verifica uma data completa.
        :param data: Data instance
        :return: bool
        """
        if not self._valida_ano_atual(data.ano):
            return False
        elif not self._valida_mes(data.mes):
            return False
        elif not self._valida_dia(data.dia):
            return False
        elif self._ano_bissexto(data.ano) and data.mes == 2:
            return 0 < data.dia < 30
        elif data.mes == 2:
            return 0 < data.dia < 29
        elif mes_com_31_switch(data.mes) is None:
            return False
        return 0 < data.dia < 32 if mes_com_31_switch(data.mes) \
            else 0 < data.dia < 31

    # data cartão

    def _checar_data_cartao(self, data: DataCartao):
        """
        Esse metodo verifica uma data de cartão de credito.
        :param data: DataCartao
        :return: bool
        """
        return self._valida_mes(data.mes) and self._valida_ano(data.ano)

    # metodos auxiliares

    def _valida_dia(self, dia=0):
        """
        Esse metodo valida o dia.
        :param dia: int
        :return: bool
        """
        return 0 < dia < 32

    def _valida_mes(self, mes=0):
        """
        Esse metódo valida o mês.
        :param mes: int
        :return: bool
        """
        return 0 < mes <= 12

    def _valida_ano_atual(self, ano=0):
        """
        Esse metodo valida o ano.
        (considerando ano atual)
        :param ano: int
        :return: bool
        """
        return 1899 < ano <= datetime.now().year

    def _valida_ano(self, ano=0):
        """
        Esse metodo valida o ano.
        :param ano: int
        :return: bool
        """
        return 1899 < ano < datetime.now().year + 15

    def _ano_bissexto(self, ano=0):
        """
        Esse metodo determina se um ano é bissexto.
        (só interessa na verificação completa)
        :param ano: int
        :return: bool
        """
        if ano.__mod__(4) == 0:
            if ano.__mod__(100) == 0:
                return ano.__mod__(400) == 0
            else:
                return True
        else:
            return False

    # metodo especial para checagem 30/31

    def _mes_com_31_switch(self, mes=0):
        mes_31 = {
            (4, 6, 9, 11,): False,
            (1, 3, 5, 7, 8, 10, 12): True
        }
        mes_found = (m for meses, m in mes_31.items() if mes in meses)
        return next(mes_found, None)
