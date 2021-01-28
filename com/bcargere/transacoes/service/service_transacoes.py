from decimal import Decimal
from com.bcargere.transacoes.model.transacoes import Transacoes
from tools.banco_check.banco_check import BancoCheck
from tools.data_check.data_check import DataCheck
from tools.instance_check.instance import Instan
from tools.money_check.money_check import MoneyCheck
from tools.name_check.name_check import NameCheck


class ServiceTransacoes:
    """
    Regra de negócio para transacoes.
    bcarsoft
    """

    def __init__(self):
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
            return False
        elif not self._get_ban_check().validar_banco(transacao.get_banco_1()):
            return False
        elif not self._get_ban_check().validar_banco(transacao.get_banco_2()):
            return False
        elif not self._get_name_check().validar_palavra(transacao.get_descricao()):
            return False
        elif not self._get_data_check().is_data_valida(transacao.get_data()):
            return False
        transacao.set_dinheiro(
            Decimal(
                self._get_money_check().str_converter_money(
                    self._get_money_check().decimal_to_str(
                        transacao.get_dinheiro()
                    )
                )
            )
        )
        return False if not transacao.get_dinheiro() else True

    # delete part

    def delete_transacoes(self, transacao):
        """
        Esse metodo deleta uma transacao
        bancária.
        :param transacao: Transacoes instance
        :return: bool
        """
        if not Instan.get_instance(transacao, Transacoes):
            return False
        elif not transacao.get_id() > 0 or not transacao.get_fk() > 0:
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
            return 0
        else:
            return 1

    # getters

    def _get_ban_check(self):
        return self._ban_check

    def _get_name_check(self):
        return self._name_check

    def _get_data_check(self):
        return self._data_check

    def _get_money_check(self):
        return self._money_check
