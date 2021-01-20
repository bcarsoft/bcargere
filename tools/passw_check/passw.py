from tools.strs_check.str_control import StrControl


class Passw:
    """
    Essa classe funciona como um verificador
    para validação de senhas de usuário para
    aplicação.
    bcarsoft
    """

    def __init__(self):
        pass

    # senhas gerais

    def verifica_senha_app(self, senha='', size=16):
        """
        Esse metodo verifica a senha para criação
        de conta do aplicativo.
        :param senha: str
        :param size: int
        :return: bool
        """
        if StrControl.is_none_or_empty(senha):
            return False
        elif StrControl.str_great(senha, size):
            return False
        return self._valid_characters(senha)

    def _valid_characters(self, senha=''):
        """
        Esse metodo verifica se os caracteres são válidos
        através da tabela ascii.
        [#,$,%,&,0...9,@,A...Z,a...z]
        :param senha: str
        :return: bool
        """
        aux = StrControl.make_str_list_each(senha)
        aux = [ord(c) for c in aux]
        for c in aux:
            if c < 35 or c > 122:
                return False
            if 38 < c < 48:
                return False
            if 57 < c < 64:
                return False
            if 90 < c < 97:
                return False
        else:
            return True

    # senhas numericas

    def verifica_senha_numerica(self, senha='', size=6, exact=True):
        """
        Verifica se uma senha numérica pode ser considerada
        válida com base no seu tamanho e se cada elemento
        pode ser convertido em tipo numérico.
        :param senha: str
        :param size: int
        :param exact: bool
        :return: bool
        """
        if StrControl.is_none_or_empty(senha):
            return False
        elif not StrControl.str_equals(senha, size) and exact:
            return False
        elif StrControl.str_great(senha, size):
            return False
        return self._valid_char_numeric(senha)

    def _valid_char_numeric(self, senha=''):
        """
        Verifica se cada caractere pode ser convertido em
        numero.
        :param senha: str
        :return: bool
        """
        aux = StrControl.make_str_list_each(senha)
        for c in aux:
            if not StrControl.str_can_int_float(c):
                return False
        else:
            return True
