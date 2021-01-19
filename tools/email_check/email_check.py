from tools.strs_check.str_control import StrControl
from tools.instance_check.instance import Instan


class EmailCheck:
    """
    Classe para validação de endereço de e-mail.
    bcarsoft
    """

    def __init__(self):
        pass

    # metodo principal

    def email_is_valid(self, email=''):
        """
        Metodo que trabalha na validação de um email.
        :param email: str
        :return: bool
        """
        if StrControl.is_none_or_empty(email):
            return False
        elif not Instan.get_instance(email, str):
            return False
        # tirando espaços
        email = StrControl.take_space(email)
        if not StrControl.str_small_equal(email, 256):
            return False
        elif not self._only_one_at(StrControl.make_str_list_each(email)):
            return False
        elif StrControl.first_char_equal(email, '@') or \
                StrControl.last_char_equal(email, '@'):
            return False
        elif not StrControl.tipo_alpha_char(email) or \
                not StrControl.tipo_alpha_char(email, -1):
            return False
        elif not self._near_at_alpha_numeric(email):
            return False
        elif not self._char_valid(email):
            return False
        else:
            return True

    # caracteres válidos teste

    def _only_one_at(self, lista):
        """
        :param lista: list
        :return: bool
        """
        return lista.count('@') == 1

    def _near_at_alpha_numeric(self, email=''):
        """
        Metodo que verifica se imediato antes ou depois de um '@'
        o caractere é alfanumérico.
        :param email: str
        :return: bool
        """
        index = StrControl.return_index(email, '@')
        if not StrControl.tipo_alpha_char(email, index-1) and \
                not StrControl.tipo_numeric_char(email, index-1):
            return False
        elif not StrControl.tipo_alpha_char(email, index+1) and \
                not StrControl.tipo_numeric_char(email, index+1):
            return False
        return True

    def _char_valid(self, email=''):
        """
        Metodo que verifica se os caracteres de um
        email são validos.
        :param email: str
        :return: bool
        """
        validos = ('@', '.', '_',)
        numeros = (chr(a) for a in range(48, 58))
        letras = (chr(a) for a in range(97, 123))
        for a in numeros:
            validos += tuple(a, )
        for a in letras:
            validos += tuple(a, )
        numeros = None
        index = StrControl.return_index(email, '@')
        letras = [a for a in email[index+1:]]
        if letras.__len__() < 1:
            return False
        letras = None
        aux = StrControl.make_str_list_each(email)
        return self._email_char_valids(chaves=validos, valores=tuple(aux))

    def _email_char_valids(self, chaves=(), valores=()):
        """
        Essa classe verifica se o email tem caracteres válidos.
        (depende de _char_valid())
        :param chaves: tuple
        :param valores: tuple
        :return: bool
        """
        tem = True
        for val in valores:
            if not tem:
                return False
            tem = False
            for cha in chaves:
                if val == cha:
                    tem = True
                    break
        return True
