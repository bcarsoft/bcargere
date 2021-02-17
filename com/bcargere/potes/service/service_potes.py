from decimal import Decimal
from com.bcargere.potes.model.potes import Potes
from com.bcargere.potes.service.i_service_potes import IServicePotes
from tools.instance_check.instance import Instan
from tools.name_check.name_check import NameCheck
from tools.money_check.money_check import MoneyCheck


class ServicePotes(IServicePotes):
    """
    Regra de de negócio para registro de potes.
    bcarsoft
    """

    def __init__(self):
        """novo service potes."""
        self._name = NameCheck()
        self._money = MoneyCheck()

    # create potes

    def create_potes(self, potes):
        """
        Criando novo pote.
        :param potes: object
        :return: bool
        """
        if not Instan.get_instance(potes, Potes):
            SingMessage.message().message = 'Error: Instancia Inválida.'
            return False
        if not potes.fk > 0:
            SingMessage.message().message = 'Error: ID Usuário Inválido.'
            return False
        return True if self._create_and_update(potes) else False

    # update potes

    def update_potes(self, potes):
        """
        Atualizando pote.
        :param potes: object
        :return: bool
        """
        if not Instan.get_instance(potes, Potes):
            SingMessage.message().message = 'Error: Instancia Inválida.'
            return False
        elif not potes.id > 0:
            SingMessage.message().message = 'Error: ID Potes Inválido.'
            return False
        elif not potes.fk > 0:
            SingMessage.message().message = 'Error: ID Usuário Inválido.'
            return False
        return True if self._create_and_update(potes) else False

    # delete potes

    def delete_potes(self, potes):
        """
        Esse metodo deleta um pote.
        :param potes: object.
        :return: bool
        """
        if not Instan.get_instance(potes, Potes):
            SingMessage.message().message = 'Error: Instancia Inválida.'
            return False
        if not potes.id > 0:
            SingMessage.message().message = 'Error: ID Potes Inválido.'
        return False if not potes.id > 0 else True

    # find potes

    def find_potes(self, **kwargs):
        """
        Faz a busca pelos potes do usuário.
        :param kwargs: dict
        :return: int
        """
        if not kwargs or not kwargs.__len__() > 0:
            SingMessage.message().message = 'Error: Pesquisa Inválida.'
            return 0
        else:
            return 1

    # checker create and update

    def _create_and_update(self, potes):
        """
        Faz a checagem para aprovar os dados válidas no
        - create, - update.
        :param potes: object
        :return: bool
        """
        if not self._check_n.validar_palavra(potes.nome):
            SingMessage.message().message = 'Error: Nome Inválido.'
            return False
        elif self._check_n.validar_palavra(potes.descricao):
            SingMessage.message().message = 'Error: Descrição Inválida.'
            return False
        potes.dinheiro = Decimal(
            self._check_m.str_converter_money(
                self._check_m.decimal_to_str(potes.dinheiro)
            )
        )
        if not potes.dinheiro:
            SingMessage.message().message = 'Error: Valor Monetário Inválido.'
        return True

    # getters

    @property
    def _check_n(self):
        return self._name

    @property
    def _check_m(self):
        return self._money
