from tools.instance_check.instance import Instan


class StrControl:
    """
    Classe com metódos estaticos para verificação de
    strings.
    barsoft
    """

    def __init__(self):
        pass

    @staticmethod
    def is_empty(word=''):
        """
        String vazia.
        :param word: str
        :return: bool
        """
        return True if word.__len__() == 0 else False

    @staticmethod
    def is_none(word=''):
        """
        String nula.
        :param word: str
        :return: bool
        """
        return True if not word else False

    @staticmethod
    def is_none_or_empty(word=''):
        """
        String nula ou vazia.
        :param word: str
        :return: bool
        """
        return True if not word or word.__len__() == 0 else False

    @staticmethod
    def is_str_equal(word_1='', word_2=''):
        """
        Compara uma string igual a outra.
        :param word_1: str
        :param word_2: str
        :return: bool
        """
        return word_1 == word_2

    @staticmethod
    def take_spaces_before_after(word=''):
        """
        Tira os espaços finals e iniciais.
        :param word: str
        :return: str
        """
        return word.strip()

    @staticmethod
    def take_space(word=''):
        """
        tira todos os espaços
        :param word: str
        :return: str
        """
        return word.replace(' ', '')

    @staticmethod
    def take_character(word='', char=''):
        """
        Tira o caracter enviado da string.
        :param word: str
        :param char: str
        :return: str
        """
        return word.strip(char)

    @staticmethod
    def str_small_equal(word='', size=0):
        """
        String é menor ou igual a
        :param word: str
        :param size: int
        :return: bool
        """
        return word.__len__() <= size

    @staticmethod
    def str_great_equal(word='', size=0):
        """
        String é maior ou igual a.
        :param word: str
        :param size: int
        :return: bool
        """
        return word.__len__() >= size

    @staticmethod
    def str_small(word='', size=0):
        """
        String é menor que.
        :param word: str
        :param size: int
        :return: bool
        """
        return word.__len__() < size

    @staticmethod
    def str_great(word='', size=0):
        """
        String é maior que.
        :param word: str
        :param size: int
        :return: bool
        """
        return word.__len__() > size

    @staticmethod
    def str_can_int_float(word=''):
        """
        Verifica se uma string pode ser inteiro
        se sim, pode ser float também.
        :param word: str
        :return: bool
        """
        if not Instan.get_instance(word, str):
            return False
        try:
            int(word)
            float(word)
            return True
        except ValueError:
            return False

    @staticmethod
    def str_equals(word='', size=0):
        """
        Verifica se uma string tem o tamanho enviado.
        :param word: str
        :param size: int
        :return: bool
        """
        return True if word.__len__() == size else False

    @staticmethod
    def make_lowcase(word=''):
        """
        Converter string em apenas letras minusculas.
        :param word: str
        :return: str
        """
        return word.lower()

    @staticmethod
    def make_upcase(word=''):
        """
        Converter string em apenas letras maiusculas.
        :param word: str
        :return: str
        """
        return word.upper()

    @staticmethod
    def make_capitalize(word=''):
        """
        Deixar primeiras letras de cada porção
        de uma string maiusculas.
        :param word: str
        :return: str
        """
        return word.capitalize()

    @staticmethod
    def make_str_list(word=''):
        """
        Converta string em lista.
        :param word: str
        :return: list
        """
        return word.split()

    @staticmethod
    def make_str_list_each(word=''):
        """
        Converta uma string em uma lista com
        cada caractere separado.
        :param word: str
        :return: list
        """
        return [letra for letra in word]

    @staticmethod
    def make_list_str(word):
        """
        Converte uma lista em string.
        :param word: list
        :return: str
        """
        aux = ''
        for i in word:
            aux += i
        word = aux
        return word

    @staticmethod
    def first_char_equal(word='', char=''):
        """
        Compara primeiro caractere.
        :param word: str
        :param char: str
        :return: bool
        """
        return word[0] == char

    @staticmethod
    def last_char_equal(word='', char=''):
        """
        Compara último caractere.
        :param word: str
        :param char: str
        :return: bool
        """
        return word[-1] == char

    @staticmethod
    def tipo_alpha_char(word='', index=0):
        """
        Verifica se uma string é alfabetica.
        :param word: str
        :param index: int
        :return: bool
        """
        return word[index].isalpha()

    @staticmethod
    def tipo_numeric_char(word='', index=0):
        """
        Verifica se uma string é numerico.
        :param word: str
        :param index: int
        :return: bool
        """
        print(word[index].isnumeric())
        return word[index].isnumeric()

    @staticmethod
    def return_index(word='', char=''):
        """
        Retorna o index de um caractere.
        :param word: str
        :param char: str
        :return: int
        """
        return word.index(char)
