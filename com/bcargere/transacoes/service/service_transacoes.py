from decimal import Decimal
from com.bcargere.transacoes.model.transacoes import Transacoes
from tools.banco_check.banco_check import BancoCheck
from tools.data_check.data_check import DataCheck
from tools.instance_check.instance import Instan
from tools.money_check.money_check import MoneyCheck
from tools.name_check.name_check import NameCheck
from com.bcargere.transacoes.service.i_service_transacoes import IServiceTransacoes


class ServiceTransacoes(IServiceTransacoes):
    """
    Regra de negócio para transacoes.
    bcarsoft
    """

    def __init__(self):
        """Novo service de transações"""
        self._ban_check = BancoCheck()
        self._name_check = NameCheck()
        self._data_check = DataCheck()
        self._money_check = MoneyCheck()

    # create part

    def create_transacoes(self, transacao):
        """
        Esse metodo registra uma nova transação
        bancária.
        :param transacao: Transacoes instance
        :return: bool
        """
        if not Instan.get_instance(transacao, Transacoes):
            SingMessage.message().message = 'Error: Instancia Inválida.'
            return False
        elif not self._check_b.validar_banco(transacao.banco_1):
            SingMessage.message().message = 'Error: Banco Inválido'
            return False
        elif not self._check_b.validar_banco(transacao.banco_2):
            SingMessage.message().message = 'Error: Banco Inválido.'
            return False
        elif not self._check_n.validar_palavra(transacao.descricao):
            SingMessage.message().message = 'Error: Descrição Inválida.'
            return False
        elif not self._check_d.is_data_valida(transacao.data):
            SingMessage.message().message = 'Error: Data Inválida.'
            return False
        transacao.dinheiro = Decimal(
            self._check_m.str_converter_money(
                self._check_m.decimal_to_str(
                    transacao.dinheiro
                )
            )
        )
        if not transacao.dinheiro:
            SingMessage.message().message = 'Error: Valor Monetário Inválido.'
        return False if not transacao.dinheiro else True

    # delete part

    def delete_transacoes(self, transacao):
        """
        Esse metodo deleta uma transacao
        bancária.
        :param transacao: Transacoes instance
        :return: bool
        """
        if not Instan.get_instance(transacao, Transacoes):
            SingMessage.message().message = 'Error: Instancia Inválida.'
            return False
        elif not transacao.id > 0 or not transacao.fk > 0:
            SingMessage.message().message = 'Error: Chaves Inválidas.'
            return False
        else:
            return True

    # find part

    def find_transacoes(self, **kwargs):
        """
        Esse metodo serve para
        encontrar transacao bancária.
        Retorna a chave do registro.
        :param kwargs: dict
        :return: int
        """
        if not kwargs or kwargs.__len__() < 1:
            SingMessage.message().message = 'Error: Parametro de Pesquisa Inválido.'
            return 0
        else:
            return 1

    # getters

    @property
    def _check_b(self):
        return self._ban_check

    @property
    def _check_n(self):
        return self._name_check

    @property
    def _check_d(self):
        return self._data_check

    @property
    def _check_m(self):
        return self._money_check
