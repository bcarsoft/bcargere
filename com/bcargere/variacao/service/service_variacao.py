from tools.instance_check.instance import Instan
from tools.variacao_check.variacao_check import VariacaoCheck
from com.bcargere.variacao.model.variacao import Variacao


class ServiceVariacao:
    """
    Regra de negócio para testar as informações sobre variacao.
    bcarsoft
    """

    def __init__(self):
        self._var_check = VariacaoCheck()

    # create variacao

    def create_variacao(self, variacao):
        """
        Esse metodo registra uma nova variação.
        :param variacao: object
        :return: bool
        """
        if not self._get_var_check().validar_variacao(variacao):
            return False
        else:
            return True

    # update variacao

    def update_variacao(self, variacao):
        """
        Esse metodo atualiza uma variação.
        :param variacao: object
        :return: bool
        """
        if not self._get_var_check().validar_variacao(variacao):
            return False
        elif not variacao.get_id() > 0:
            return False
        else:
            return True

    # buscando variacao

    def find_variacao(self, **kwargs):
        """
        Esse metodo serve para encontrar
        variação,
        retorna a chave do registro.
        :param kwargs: dict
        :return: int
        """
        if not kwargs or kwargs.__len__() < 1:
            return 0
        else:
            return 1

    # delete variacao

    def delete_variacao(self, variacao):
        """
        Deletando variacão pelo id.
        :param variacao: object
        :return: bool
        """
        if not Instan.get_instance(variacao, Variacao):
            return False
        elif not variacao.get_id() > 0:
            return False
        else:
            return True

    # getter method

    def _get_var_check(self):
        return self._var_check
