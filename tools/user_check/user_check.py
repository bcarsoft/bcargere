from tools.strs_check.str_control import StrControl


class UserCheck:
    """
    Verificador de nome de usuário.
    bcarsoft
    """

    def __init__(self):
        pass

    # metodo principal

    def validar_nome_usuario(self, usuario=''):
        if StrControl.is_none_or_empty(usuario):
            return False
        elif StrControl.str_great(usuario, 32):
            return False
        usuario = StrControl.take_space(usuario)
        usuario = tuple(StrControl.make_str_list_each(usuario), )
        validos = self._generate_valid_char()
        return self._is_valid_username_text(validos, usuario)

    def _generate_valid_char(self):
        """
        Esse metodo gera uma tupla com todos os caracteres válidos.
        :return: tuple
        """
        simbolos = (chr(num) for num in range(45, 47))
        numeros = (chr(num) for num in range(48, 58))
        letras_1 = (chr(num) for num in range(97, 123))
        todos = ()
        for num in simbolos:
            todos += (num, )
        for num in numeros:
            todos += (num, )
        for num in letras_1:
            todos += (num, )
        return todos

    def _is_valid_username_text(self, validos, usuario):
        """
        Esse metodo verifica se uma tupla tem os elementos
        contidos em outra.
        :param validos: tuple
        :param usuario: tuple
        :return: bool
        """
        tem = True
        for a in usuario:
            if not tem:
                return False
            tem = False
            for b in validos:
                if a == b:
                    tem = True
                    break
        else:
            return True
