from tools.strs_check.str_control import StrControl


class NameCheck:
    """
    Esse metódo é um verificador de palavras
    configurado para o português.
    bcarsoft
    """

    def __init__(self):
        pass

    def validar_palavra(self, palavra=''):
        """
        Esse metódo pode validar uma palavra, ou seja,
        seus caracteres são válidos no português.
        :param palavra: str
        :return: bool
        """
        palavra = StrControl.make_str_list_each(palavra)
        palavra = tuple(palavra, )
        special = self._tupla_special_char()
        upcase = self._tupla_upcase()
        lowcase = self._tupla_lowcase()
        charact = special + upcase + lowcase
        tem = True
        for p in palavra:
            if not tem:
                return False
            tem = False
            for ch in charact:
                if p == ch:
                    tem = True
                    break
        else:
            return True

    def _tupla_special_char(self):
        """
        Retorna tupla com inteiros para caracteres especiais.
        :return: tuple
        """
        special = (
            32, 46, 192, 193, 194, 199, 201, 202, 205,
            211, 212, 218, 224, 225, 226, 231, 233,
            234, 237, 243, 244, 250,
        )
        return special

    def _tupla_lowcase(self):
        """
        Retorna uma tupla de inteiros
        para representar valores na tabela
        ascii de letras em caixa baixa.
        :return: tuple
        """
        lowcase = [num for num in range(97, 123)]
        return tuple(lowcase)

    def _tupla_upcase(self):
        """
        Retorna uma tupla de inteiros
        para representar valores na tabela
        ascii de letras em caixa baixa.
        :return: tuple
        """
        upcase = [num for num in range(65, 91)]
        return tuple(upcase)
