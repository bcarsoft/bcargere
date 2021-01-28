from decimal import Decimal
from com.bcargere.potes.model.potes import Potes
from com.bcargere.potesopera.model.potesopera import PotesOpera
from tools.data_check.data_check import DataCheck
from tools.instance_check.instance import Instan
from tools.money_check.money_check import MoneyCheck
from tools.name_check.name_check import NameCheck


class ServicePosteOpera:
    """
    Regra de negócio para Potes.
    bcarsoft
    """

    def __init__(self):
        self._name_check = NameCheck()
        self._money_check = MoneyCheck()
        self._data_check = DataCheck()

    # create part

    def create_potesopera(self, potesopera):
        """
        Registrar uma nova transação poteária.
        :param potesopera: PotesOpera instance
        :return: bool
        """
        if not Instan.get_instance(potesopera, PotesOpera):
            return False
        elif not self._get_name_check().validar_palavra(potesopera.get_descricao()):
            return False
        elif not self._get_data_check().is_data_valida(potesopera.get_data()):
            return False
        potesopera.set_dinheiro(
            Decimal(
                self._get_money_check().str_converter_money(
                    self._get_money_check().decimal_to_str(
                        potesopera.get_dinheiro()
                    )
                )
            )
        )
        if not potesopera.get_dinheiro():
            return False
        elif not self._valida_potes(potesopera.get_pote_1()):
            return False
        return False if self._valida_potes(potesopera.get_pote_2()) \
            else True

    # delete part

    def delete_potesopera(self, potesopera):
        """
        Esse metodo deleta uma transacao
        poteária.
        :param potesopera: PotesOpera instance
        :return: bool
        """
        if not Instan.get_instance(potesopera, PotesOpera):
            return False
        elif not potesopera.get_id() > 0 or not potesopera.get_fk() > 0:
            return False
        else:
            return True

    # find part

    def find_potesopera(self, **kwargs):
        """
        Esse metodo serve para
        encontrar transacao potesopera.
        Retorna a chave do registro.
        :param kwargs: dict
        :return: int
        """
        if not kwargs or kwargs.__len__() < 1:
            return 0
        else:
            return 1

    # private

    def _valida_potes(self, potes: Potes):
        """
        Esse metodo privado valida o potes
        ou não.
        :param potes: Potes instance.
        :return: bool
        """
        if not Instan.get_instance(potes, Potes):
            return False
        elif not self._get_name_check().validar_palavra(potes.get_nome()):
            return False
        elif not self._get_name_check().validar_palavra(potes.get_descricao()):
            return False
        potes.set_dinheiro(
            Decimal(
                self._get_money_check().str_converter_money(
                    self._get_money_check().decimal_to_str(
                        potes.get_dinheiro()
                    )
                )
            )
        )
        return False if not potes.get_dinheiro() else True

    # getters

    def _get_name_check(self):
        return self._name_check

    def _get_money_check(self):
        return self._money_check

    def _get_data_check(self):
        return self._data_check
