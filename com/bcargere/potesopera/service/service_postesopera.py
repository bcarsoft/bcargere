from decimal import Decimal
from com.bcargere.core.singleton.sing_message import SingMessage
from com.bcargere.potes.model.potes import Potes
from com.bcargere.potesopera.model.potesopera import PotesOpera
from com.bcargere.potesopera.service.i_service_potesopera import IServicePotesOpera
from tools.data_check.data_check import DataCheck
from tools.instance_check.instance import Instan
from tools.money_check.money_check import MoneyCheck
from tools.name_check.name_check import NameCheck


class ServicePostesOpera(IServicePotesOpera):
    """
    Regra de negócio para Potes.
    bcarsoft
    """

    def __init__(self):
        """novon service potesopera."""
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
            SingMessage.message().message = 'Error: Instancia Inválida.'
            return False
        elif not self._check_n.validar_palavra(potesopera.descricao):
            SingMessage.message().message = 'Error: Descrição Inválida.'
            return False
        elif not self._check_d.is_data_valida(potesopera.data):
            SingMessage.message().message = 'Error: Data Inválida.'
            return False
        potesopera.dinheiro = Decimal(
            self._check_m.str_converter_money(
                self._check_m.decimal_to_str(potesopera.dinheiro)
            )
        )
        if not potesopera.dinheiro:
            SingMessage.message().message = 'Error: Valor Monetário Inválida.'
            return False
        elif not self._valida_potes(potesopera.pote_1):
            SingMessage.message().message = 'Error: Pote Inválido.'
            return False
        elif not self._valida_potes(potesopera.pote_2):
            SingMessage.message().message = 'Error: Pote Inválido.'
            return False
        return False if self._valida_potes(potesopera.pote_2) else True

    # delete part

    def delete_potesopera(self, potesopera):
        """
        Esse metodo deleta uma transacao
        poteária.
        :param potesopera: PotesOpera instance
        :return: bool
        """
        if not Instan.get_instance(potesopera, PotesOpera):
            SingMessage.message().message = 'Error: Instancia Inválida.'
            return False
        elif not potesopera.id > 0 or not potesopera.fk > 0:
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
            SingMessage.message().message = 'Error: Pesquisa Inválida.'
            return 0
        else:
            return 1

    # private

    def _valida_potes(self, potes):
        """
        Esse metodo privado valida o potes
        ou não.
        :param potes: Potes instance.
        :return: bool
        """
        if not Instan.get_instance(potes, Potes):
            SingMessage.message().message = 'Error: Instancia Inválida.'
            return False
        elif not self._check_n.validar_palavra(potes.nome):
            SingMessage.message().message = 'Error: Nome Inválido.'
            return False
        elif not self._check_n.validar_palavra(potes.descricao):
            SingMessage.message().message = 'Error: Descrição Inválida.'
            return False
        potes.dinheiro = Decimal(
            self._check_m.str_converter_money(
                self._check_m.decimal_to_str(potes.dinheiro)
            )
        )
        if not potes.dinheiro:
            SingMessage.message().message = 'Error: Valor Monetário Inválido.'
        return False if not potes.dinheiro else True

    # getters

    @property
    def _check_n(self):
        return self._name_check

    @property
    def _check_m(self):
        return self._money_check

    @property
    def _check_d(self):
        return self._data_check
