from decimal import Decimal
from com.bcargere.pix.model.pix import Pix
from com.bcargere.pixopera.model.pixopera import PixOpera
from com.bcargere.pixopera.service.i_service_pixopera import IServicePixOpera
from tools.data_check.data_check import DataCheck
from tools.money_check.money_check import MoneyCheck
from tools.name_check.name_check import NameCheck
from tools.instance_check.instance import Instan
from tools.strs_check.str_control import StrControl


class ServicePixOpera(IServicePixOpera):
    """
    Regra de negócio para operações pix.
    bcarsoft
    """

    def __init__(self):
        """novo service pix opera"""
        self._data_check = DataCheck()
        self._money_check = MoneyCheck()
        self._name_check = NameCheck()

    # create part

    def create_pixopera(self, pixopera: PixOpera):
        """
        Esse metodo verifica dados para registro de
        nova operação pix.
        :param pixopera: PixOpera instance
        :return: bool
        """
        if not Instan.get_instance(pixopera, PixOpera):
            SingMessage.message().message = 'Error: Instancia Inválida.'
            return False
        elif not self._verifica_pix(pixopera.pix_1):
            SingMessage.message().message = 'Error: Pix Inválido.'
            return False
        elif not self._verifica_pix(pixopera.pix_2):
            SingMessage.message().message = 'Error: Pix Inválido.'
            return False
        pixopera.dinheiro = Decimal(
            self._check_m.str_converter_money(
                self._check_m.decimal_to_str(pixopera.dinheiro)
            )
        )
        if not pixopera.dinheiro:
            SingMessage.message().message = 'Error: Valor Monetário Inválido.'
            return False
        if not self._check_d.is_data_valida(pixopera.data):
            SingMessage.message().message = 'Error: Data Inválida.'
        return False if not self._check_d.is_data_valida(pixopera.data) else True

    # delete part

    def delete_pixopera(self, pixopera):
        """
        Esse metodo deleta uma operação de pix.
        :param pixopera: PixOpera instance
        :return: bool
        """
        if not Instan.get_instance(pixopera, PixOpera):
            SingMessage.message().message = 'Error: Instancia Inválida.'
            return False
        elif not pixopera.id > 0 or not pixopera.fk > 0:
            SingMessage.message().message = 'Error: Chave de Acesso Inválida.'
            return False
        else:
            return True

    # find part

    def find_pixopera(self, **kwargs):
        """
        Esse metodo serve para
        encontrar operação pix.
        Retorna a chave do registro.
        :param kwargs: dict
        :return: int
        """
        if not kwargs or kwargs.__len__() < 1:
            SingMessage.message().message = 'Error: Pesquisa Inválida.'
            return 0
        else:
            return 1

    # special

    def _verifica_pix(self, pix):
        """
        Verifica se as informações de pix
        estão corretas.
        :param pix: Pix intance
        :return: bool
        """
        if not Instan.get_instance(pix, Pix):
            SingMessage.message().message = 'Error: Instancia Inválida.'
            return False
        elif not self._check_n.validar_palavra(pix.nome):
            SingMessage.message().message = 'Error: Nome Inválido.'
            return False
        elif StrControl.is_none_or_empty(pix.chave):
            SingMessage.message().message = 'Error: Chave Pix Inválida.'
            return False
        else:
            return True

    # getters

    @property
    def _check_d(self):
        return self._data_check

    @property
    def _check_m(self):
        return self._money_check

    @property
    def _check_n(self):
        return self._name_check
