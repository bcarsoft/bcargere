class Criptonow:
    """
    This class has the tools to encrypt and
    decrypt data information.
    bcarsoft
    """

    def __init__(self):
        """
        Encrypt/Decryp Criptonow new instance.
        """
        pass

    def encrypt(self, dado, senha):
        """
        This method cans encrypt data with a
        password and the result is only one.
        :param dado: str or list - data to encrypt
        :param senha: str or list - password
        :return: str if valid else None
        """
        dado = self._transform_str_list(dado)
        senha = self._transform_str_list(senha)
        if not dado or not senha:
            return None
        mix = self._mix_two_lists(senha, dado)
        mix = self._reverse(mix)
        mix = self._transform_ascii(mix)
        mix = self._sum_grown_up(mix)
        mix = self._transform_ascii_str_list(mix)
        return self._transform_list_str(mix)

    def decrypt(self, dado, senha):
        """
        This method cans decrypt data with a
        password and the result is only one.
        :param dado: str or list - data to decrypt
        :param senha: str or list - password
        :return: str if valid else None
        """
        dado = self._transform_str_list(dado)
        senha = self._transform_str_list(senha)
        if not dado or not senha:
            return None
        mix = self._transform_ascii(dado)
        mix = self._sub_grown_down(mix)
        mix = self._transform_ascii_str_list(mix)
        mix = self._reverse(mix)
        id_i = senha.index(senha[-1])
        passw = mix[:id_i]
        passw.append(mix[-1])
        return self._transform_list_str(mix[id_i:-1]) \
            if passw == senha else None

    def _reverse(self, lista):
        """
        This method can invert a list.
        :param lista: list
        :return: list if valid else None
        """
        if not self._verify_instan_size(objeto=lista, classe=list):
            return None
        return [lista[i] for i in range(len(lista) - 1, -1, -1)]

    def _mix_two_lists(self, lista1, lista2):
        """
        This method can mix two lists in one.
        :param lista1: list
        :param lista2: list
        :return: list if valid else None
        """
        if not self._verify_instan_size(objeto=lista1, classe=list):
            return None
        elif not self._verify_instan_size(objeto=lista2, classe=list):
            return None
        nova = lista1[:-1] + lista2
        nova.append(lista1[-1])
        return nova

    def _transform_ascii(self, lista):
        """
        This method converts a str list in a int list with
        the ascii table values.
        :param lista: list
        :return: list if valid else None
        """
        if not self._verify_instan_size(objeto=lista, classe=list):
            return None
        return [ord(str(i)) for i in lista]

    def _sum_grown_up(self, lista):
        """
        This method cans sum values to each element from a list.
        :param lista: list
        :return: list if valid else None
        """
        if not self._verify_instan_size(objeto=lista, classe=list):
            return None
        nova = []
        dif = 1
        for i in lista:
            nova.append(i + dif)
            dif += 1
        return nova

    def _transform_ascii_str_list(self, lista):
        """
        This method takes each int from a int list, (ascii table values)
        and change them to a str list.
        :param lista: list
        :return: list if valid else None
        """
        if not self._verify_instan_size(objeto=lista, classe=list):
            return None
        return [chr(i) for i in lista]

    def _sub_grown_down(self, lista):
        """
        This method cans sub values to each element from a list.
        :param lista: list
        :return: list if valid else None
        """
        if not self._verify_instan_size(objeto=lista, classe=list):
            return None
        nova = []
        dif = 1
        for i in lista:
            nova.append(i - dif)
            dif += 1
        return nova

    def _verify_instance(self, objeto, classe):
        """
        This method is for test the object's class.
        :param objeto: object
        :param classe: class
        :return: bool
        """
        return isinstance(objeto, classe)

    def _none_or_empty(self, objeto):
        """
        This method verifies if an object value (str) isn't None or
        Empty.
        :param objeto: object (str)
        :return: bool
        """
        return True if not objeto or objeto.__len__() < 1 else False

    def _verify_instan_size(self, objeto, classe=object):
        """
        This method can verifies the object's class and if it's not
        none or empty.
        :param objeto: object
        :param classe: class
        :return: bool
        """
        return self._verify_instance(objeto=objeto, classe=classe) and not \
            self._none_or_empty(objeto)

    def _transform_str_list(self, str_list):
        """
        This method is for transform a str object into a list with
        str.split() values from previous str.
        :param str_list: str
        :return: list if valid else None
        """
        if self._verify_instance(objeto=str_list, classe=list):
            stl = [str(i) for i in str_list if str(i).__len__() == 1]
            if not stl.__len__() == str_list.__len__():
                return None
            else:
                return [str(i) for i in str_list]
        elif self._verify_instance(objeto=str_list, classe=str):
            return [i for i in str_list]
        else:
            return None

    def _transform_list_str(self, list_str):
        """
        This method is for transform a list object into valid str.
        :param list_str: list
        :return: str if valid else None
        """
        if self._verify_instance(objeto=list_str, classe=str):
            return list_str
        elif self._verify_instance(objeto=list_str, classe=list):
            strl = ''
            for i in list_str:
                strl += i
            else:
                list_str = strl
            return list_str
        else:
            return None
