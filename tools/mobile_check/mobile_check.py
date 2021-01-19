from tools.strs_check.str_control import StrControl


class MobileCheck:
    """
    Essa Classe trabalha com a validação de números
    de celular.
    bcarsoft
    """

    def __init__(self):
        pass

    def mobile_valid(self, mobile='', size=14):
        """
        Esse metodo valida um número de telefone quanto a
        caracteres inválido. Basta que seja enviado o numero
        de telefone em str, e se desejar, o tamanho em int.
        Por default, o valor do tamanho é 14. O número deve
        começar com '+'.
        :param mobile: str
        :param size: int
        :return: bool
        """
        if StrControl.is_none_or_empty(mobile):
            return False
        elif not StrControl.str_equals(mobile, size):
            return False
        elif not StrControl.is_str_equal(mobile[0], '+'):
            return False
        else:
            return self._is_valid_mobile\
                (tuple(StrControl.make_str_list(mobile)))

    def _is_valid_mobile(self, numeros):
        """
        Percorre a tupla e compara os elementos.
        :param lista: tuple
        :return: bool
        """
        for num in numeros[1:]:
            if not StrControl.str_can_int_float(str(num)):
                return False
            elif not StrControl.tipo_numeric_char(num):
                return False
        else:
            return True
