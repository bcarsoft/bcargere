from tools.instance_check.instance import Instan
from com.bcargere.variacao.model.variacao import Variacao


class VariacaoCheck:
    """
    Essa classe verifica se as informações para variação
    podem ser consideradas válidas.
    bcarsoft
    """

    def __init__(self):
        pass

    def validar_variacao(self, variacao, atualiza=False):
        """
        Verifica se a variação não tem informação
        inválida, funciona com atualizar mudandando o
        parametro opicional.
        :param variacao: Variacao instance
        :param atualiza: bool
        :return: bool
        """
        if Instan.get_instance(variacao, Variacao):
            return False
        elif variacao.get_fk() < 1:
            return False
        elif variacao.get_numero() < 1:
            return False
        elif variacao.get_dinheiro() < 0 and not atualiza:
            return False
        else:
            return True
