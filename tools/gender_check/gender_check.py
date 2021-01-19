from tools.instance_check.instance import Instan
from tools.strs_check.str_control import StrControl


class GenderCheck:
    """
    Verifica se um sexo é valido.
    bcarsoft
    """

    def __init__(self):
        pass

    def gender_valid(self, gender=''):
        """
        Verifica se o sexo é válido.
        :param gender: str
        :return: bool
        """
        if not Instan.get_instance(gender, str):
            return False
        elif StrControl.is_none_or_empty(gender):
            return False
        elif not StrControl.str_small_equal(gender, 10):
            return False
        # deixando minusculo
        gender = StrControl.make_lowcase(gender)
        # comparando
        if StrControl.is_str_equal(gender, 'masculino'):
            return True
        elif StrControl.is_str_equal(gender, 'feminino'):
            return True
        elif StrControl.is_str_equal(gender, 'indefinido'):
            return True
        else:
            return False
