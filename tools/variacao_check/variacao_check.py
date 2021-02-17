from com.bcargere.core.singleton.sing_message import SingMessage
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
            SingMessage.message().message = 'Erro: Inatancia Inválida.'
            return False
        elif variacao.fk < 1:
            SingMessage.message().message = 'Erro: ID Conta Bancária Inválido'
            return False
        elif variacao.numero < 1:
            SingMessage.message().message = 'Erro: Número da Variação Inválido'
            return False
        elif variacao.dinheiro < 0 and not atualiza:
            SingMessage.message().message = 'Erro: Valor Monetário Inválido'
            return False
        else:
            return True
