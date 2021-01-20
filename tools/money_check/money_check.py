from decimal import Decimal
from tools.instance_check.instance import Instan
from tools.strs_check.str_control import StrControl


class MoneyCheck:
    """
    Classe para checagem de valores monetários.
    bcarsoft
    """

    def __init__(self):
        pass

    def str_converter_money(self, money=''):
        """
        Analisa se uma string pode ser dinheiro.
        Assim como deixa a string no formato correto.
        :param money: str
        :return: str or None
        """
        if not Instan.get_instance(money, str):
            # não string
            return None
        money = StrControl.take_space(money)
        if not self._float_except(money):
            # não pode ser float
            return None
        money = tuple(StrControl.make_str_list_each(money))
        if money.count('.') > 1:
            # mais de um .
            return None
        money = StrControl.make_list_str(list(money))
        if StrControl.is_str_equal(money[0], '.'):
            money = '0' + money
        elif money.isnumeric():
            money += '.00'
        else:
            idx = money.index('.')
            idx = money[idx + 1:]
            if idx.__len__() < 2:
                money += '0'
            if idx.__len__() > 2:
                idx = money.index('.')
                money = money[:idx + 3]
        return money

    def get_signal_changed(self, dec=Decimal('0.00')):
        """
        Muda o sinal do decimal.
        - Se n > 0 se torna n < 0
        - Se n < 0 se torna n > 0
        :param dec: Decimal instance
        :return: Decimal instance
        """
        return dec.__mul__(Decimal('-1'))

    def soma_dinheiro(self, dec_1, dec_2):
        """
        Metodo para realizar soma de dinheiro.
        :param dec_1: Decimal instance
        :param dec_2: Decimal instance
        :return: Decimal instance
        """
        if not self._veriry_decimal_or_false(dec_1, dec_2):
            return Decimal('0.00')
        return dec_1.__add__(dec_2)

    def subtrai_dinheiro(self, dec_1, dec_2):
        """
        Metodo para realizar subtração de dinheiro.
        :param dec_1: Decimal instance
        :param dec_2: Decimal instance
        :return: Decimal instance
        """
        if not self._veriry_decimal_or_false(dec_1, dec_2):
            return Decimal('0.00')
        return dec_1.__sub__(dec_2)

    def multiplica_dinheiro(self, dec_1, dec_2):
        """
        Metodo para realizar multiplicação de dinheiro.
        :param dec_1: Decimal instance
        :param dec_2: Decimal instance
        :return: Decimal instance
        """
        if not self._veriry_decimal_or_false(dec_1, dec_2):
            return Decimal('0.00')
        return dec_1.__mul__(dec_2)

    def divide_dinheiro(self, dec_1, dec_2):
        """
        Metodo para realizar divisão de dinheiro.
        :param dec_1: Decimal instance
        :param dec_2: Decimal instance
        :return: Decimal instance
        """
        if not self._veriry_decimal_or_false(dec_1, dec_2):
            return Decimal('0.00')
        return self.str_converter_money(self.decimal_to_str(dec_1/dec_2))

    def decimal_to_str(self, dec):
        """
        Converte um Decimal em Str
        :param dec: object
        :return: None or Str
        """
        return None if not Instan.get_instance(dec, Decimal) \
            else dec.__str__()

    def decimal_greater(self, dec_1, dec_2):
        """
        Metodo que verifica se um decimal é maior do que outro.
        :param dec_1: Decimal instance
        :param dec_2: Decimal instance
        :return: bool
        """
        if not self._veriry_decimal_or_false(dec_1, dec_2):
            return False
        return dec_1 > dec_2

    def decimal_small(self, dec_1, dec_2):
        """
        Metodo que verifica se um decimal é menor do que outro.
        :param dec_1: Decimal instance
        :param dec_2: Decimal instance
        :return: bool
        """
        if not self._veriry_decimal_or_false(dec_1, dec_2):
            return False
        return dec_1 < dec_2

    def decimal_equals(self, dec_1, dec_2):
        """
        Metodo que verifica se um decimal é a outro.
        :param dec_1: Decimal instance
        :param dec_2: Decimal instance
        :return: bool
        """
        if not self._veriry_decimal_or_false(dec_1, dec_2):
            return False
        return dec_1 == dec_2

    def decimal_small_equals(self, dec_1, dec_2):
        """
        Metodo que verifica se um decimal é menor igual a outro.
        :param dec_1: Decimal instance
        :param dec_2: Decimal instance
        :return: bool
        """
        if not self._veriry_decimal_or_false(dec_1, dec_2):
            return False
        return dec_1 <= dec_2

    def decimal_greater_equals(self, dec_1, dec_2):
        """
        Metodo que verifica se um decimal é maior igual a outro.
        :param dec_1: Decimal instance
        :param dec_2: Decimal instance
        :return: bool
        """
        if not self._veriry_decimal_or_false(dec_1, dec_2):
            return False
        return dec_1 >= dec_2

    def _veriry_decimal_or_false(self, dec_1, dec_2):
        """
        Verifica se dois decimais são válidos.
        :param dec_1: object
        :param dec_2: object
        :return: bool
        """
        dec_1 = self._verify_str_or_decimal(dec_1)
        if not dec_1:
            return False
        dec_2 = self._verify_str_or_decimal(dec_2)
        if not dec_2:
            return False
        return True

    def _verify_str_or_decimal(self, dec):
        """
        Verifica Decimal ou converte str em Decimal.
        :param dec: object
        :return: Decimal or None
        """
        if not Instan.get_instance(dec, Decimal):
            if not Instan.get_instance(dec, str):
                return None
            else:
                dec = Decimal(self.str_converter_money(dec))
        return dec

    def _float_except(self, money: str):
        """
        Testa se é possível converter o valor em float
        :param money: str
        :return: bool
        """
        try:
            float(money)
            return True
        except ValueError:
            return False

    def _add_one_zero(self, money=''):
        """
        Adiciona um zero se após o ponto houver somente
        um caractere.
        :param money: str
        :return: str
        """
        idx = money.index('.')
        idx = money[idx+1:]
        if idx.__len__() < 2:
            money += '0'
        elif idx.__len__() > 2:
            pass
        return money
