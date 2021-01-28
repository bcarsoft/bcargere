from decimal import Decimal
from com.bcargere.pix.model.pix import Pix
from com.bcargere.pixopera.model.pixopera import PixOpera
from tools.data_check.data_check import DataCheck
from tools.money_check.money_check import MoneyCheck
from tools.name_check.name_check import NameCheck
from tools.instance_check.instance import Instan
from tools.strs_check.str_control import StrControl


class ServicePixOpera:
    """
    Regra de negócio para operações pix.
    """

    def __init__(self):
        self._data_check = DataCheck()
        self._money_check = MoneyCheck()
        self._name_check = NameCheck()

    # create part

    def create_pixopera(self, pixopera):
        """
        Esse metodo verifica dados para registro de
        nova operação pix.
        :param pixopera: PixOpera instance
        :return: bool
        """
        if not Instan.get_instance(pixopera, PixOpera):
            return False
        elif not self._verifica_pix(pixopera.get_pix_1()):
            return False
        elif not self._verifica_pix(pixopera.get_pix_2()):
            return False
        pixopera.set_dinheiro(
            Decimal(
                self._get_money_check().str_converter_money(
                    self._get_money_check()
                        .decimal_to_str(pixopera.get_dinheiro())
                )
            )
        )
        if not pixopera.get_dinheiro():
            return False
        return False if not self._get_data_check()\
            .is_data_valida(pixopera.get_data()) else True

    # delete part

    def delete_pixoopera(self, pixopera):
        """
        Esse metodo deleta uma operação de pix.
        :param pixopera: PixOpera instance
        :return: bool
        """
        if not Instan.get_instance(pixopera, PixOpera):
            return False
        elif not pixopera.get_id() > 0 or not pixopera.get_fk() > 0:
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
            return False
        elif not self._get_name_check().validar_palavra(pix.get_nome()):
            return False
        elif StrControl.is_none_or_empty(pix.get_chave()):
            return False
        else:
            return True

    # getters

    def _get_data_check(self):
        return self._data_check

    def _get_money_check(self):
        return self._money_check

    def _get_name_check(self):
        return self._name_check
