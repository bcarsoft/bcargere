from decimal import Decimal
from com.bcargere.potes.model.potes import Potes
from tools.instance_check.instance import Instan
from tools.name_check.name_check import NameCheck
from tools.money_check.money_check import MoneyCheck


class ServicePotes:
    """
    Regra de de negócio para registro de potes.
    bcarsoft
    """

    def __init__(self):
        self._name = NameCheck()
        self._money = MoneyCheck()

    # create potes

    def create_potes(self, potes: Potes):
        """
        Criando novo pote.
        :param potes: object
        :return: bool
        """
        if not Instan.get_instance(potes, Potes):
            return False
        if not potes.get_fk() > 0:
            return False
        return True if self._create_and_update(potes) else False

    # update potes

    def update_potes(self, potes: Potes):
        """
        Atualizando pote.
        :param potes: object
        :return: bool
        """
        if not Instan.get_instance(potes, Potes):
            return False
        elif not potes.get_id() > 0:
            return False
        elif not potes.get_fk() > 0:
            return False
        return True if self._create_and_update(potes) else False

    # delete potes

    def delete_potes(self, potes: Potes):
        """
        Esse metodo deleta um pote.
        :param potes: object.
        :return: bool
        """
        if not Instan.get_instance(potes, Potes):
            return False
        return False if not potes.get_id() > 0 else True

    # find potes

    def find_potes(self, **kwargs):
        """
        Faz a busca pelos potes do usuário.
        :param kwargs: dict
        :return: int
        """
        if not kwargs or not kwargs.__len__() > 0:
            return 0
        else:
            return 1

    # checker create and update

    def _create_and_update(self, potes: Potes):
        """
        Faz a checagem para aprovar os dados válidas no
        - create, - update.
        :param postes: object
        :return: bool
        """
        if not self._get_name().validar_palavra(potes.get_nome()):
            return False
        elif self._get_name().validar_palavra(potes.get_descricao()):
            return False
        potes.set_dinheiro(
            Decimal(
                self._get_money().str_converter_money(
                    self._get_money().decimal_to_str(
                        potes.get_dinheiro()
                    )
                )
            )
        )
        return True

    # getters

    def _get_name(self):
        return self._name

    def _get_money(self):
        return self._money
