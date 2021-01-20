from decimal import Decimal
from com.bcargere.data.model.data import DataCartao
from tools.instance_check.instance import Instan
from tools.strs_check.str_control import StrControl
from tools.name_check.name_check import NameCheck
from tools.data_check.data_check import DataCheck
from tools.money_check.money_check import MoneyCheck


class CartaoCheck:
    """
    Essa classe é para testar e aperfeiçoar dados de
    cartão.
    bcarsoft
    """

    def __init__(self):
        pass

    # parte de bandeira do cartão

    def bandeira_checker(self, bandeira=''):
        """
        Metodo que valida a bandeira do cartão.
        :param bandeira: str
        :return: bool
        """
        bands = self._tuple_cartao_bandeira()
        return bandeira.lower() in bands

    def _tuple_cartao_bandeira(self):
        """
        Gera uma tupla com as bandeiras de cartão.
        :return: tuple
        """
        band = (
            'mastercard',
            'visa',
            'american express',
            'hipercard',
            'elo'
        )
        return band

    # parte de tipo do cartão

    def tipo_check(self, tipo=''):
        """
        Metodo que valida a tipo do cartão.
        :param tipo: str
        :return: bool
        """
        tipos = self._tuple_cartao_tipo()
        return tipo.lower() in tipos

    def _tuple_cartao_tipo(self):
        """
        Gera uma tupla com os tipos de cartão válidos.
        :return: tuple
        """
        tipos = (
            'crédito',
            'débito',
            'pré pago',
            'conta'
        )
        return tipos

    # parte de nome do cartão

    def nome_checker(self, nome=''):
        """
        Verifica as informações de nome no cartão.
        :param nome: str
        :return: bool
        """
        if not Instan.get_instance(nome, str):
            return False
        elif StrControl.is_none_or_empty(nome):
            return False
        elif StrControl.str_great(nome, 22):
            return False
        nome = StrControl.take_spaces_before_after(nome)
        nm_chk = NameCheck()
        return nm_chk.validar_palavra(nome)

    # parte de numero do cartão

    def str_to_number_cartao(self, number=''):
        """
        Converte uma string para um numero de cartão.
        :param number: str
        :return: object -> str or None
        """
        if not Instan.get_instance(number, str):
            # invalid instance
            return None
        number = StrControl.take_spaces_before_after(number)
        if not StrControl.str_equals(number, 19) and \
                not StrControl.str_equals(number, 16):
            # invalid size
            return None
        elif not self._is_all_char_valid(number):
            # invalid char found
            return None
        elif StrControl.str_equals(number, 19):
            # replace space to hyphen
            number.replace(' ', '-')
        else:
            temp = self._transform_str_tuple_four(number)
            number = ''
            for lt in temp:
                number += lt
        return number

    def _is_all_char_valid(self, numero=''):
        """
        Verifica caractere por caractere.
        :param numero: str
        :return: bool
        """
        temp = tuple(StrControl.make_str_list_each(numero))
        valid = self._tuple_valid_char()
        for lt in temp:
            if lt not in valid:
                return False
        else:
            return True

    def _tuple_valid_char(self):
        """
        Retorna um generator com os caracteres válidos.
        :return: tuple
        """
        num = [str(lt) for lt in range(32, 33)]
        num += [str(lt) for lt in range(45, 46)]
        num += [str(lt) for lt in range(10)]
        return tuple(num)

    def _transform_str_tuple_four(self, number=''):
        """
        Transforma uma string em tupla, dividindo-a
        em grupos de 4 caracteres.
        :param number: str
        :return: tuple
        """
        temp = []
        for lt in range(0, 17, 4):
            temp.append(number[lt-4: lt])
        else:
            temp.remove('')
        return tuple(temp)

    # parte de data de vencimento

    def data_checker(self, data: DataCartao):
        """
        Verifica a data de vencimento do cartão.
        :param data: DataCartao instance
        :return: bool
        """
        dt_chk = DataCheck()
        return dt_chk.is_data_valida(data)

    # parte de codigo de segurança

    def code_checker(self, code=''):
        """
        Verifica se um codigo de segurança pode ser
        considerado válido.
        :param code: str
        :return: bool
        """
        if not Instan.get_instance(code, str):
            return False
        elif not StrControl.str_equals(code, 3):
            return False
        return code.isnumeric()

    # parte de dinheiro verificador

    def verifica_monetario(self, dinheiro=Decimal('0.00')):
        """
        Verificar valor monetário.
        Vale para:
        - fatura;
        - limite;
        - excedente;
        :param dinheiro: Decimal instance.
        :return: bool
        """
        if not Instan.get_instance(dinheiro, Decimal):
            return False
        mn_chk = MoneyCheck()
        return Decimal(mn_chk.decimal_to_str(dinheiro))
