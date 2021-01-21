from com.bcargere.pix.model.pix import Pix
from tools.instance_check.instance import Instan
from tools.name_check.name_check import NameCheck
from tools.strs_check.str_control import StrControl


class ServicePix:
    """
    Regra de negócio para pix
    - create;
    - update;
    - delete;
    - find;
    bcarsoft
    """

    def __init__(self):
        self._name = NameCheck()

    # create pix

    def create_pix(self, pix: Pix):
        """
        Criar novo pix.
        :param pix: object
        :return: bool
        """
        if not Instan.get_instance(pix, Pix):
            return False
        elif not pix.get_fk() > 0:
            return False
        return True if self._create_update_delete(pix) else False

    # update pix

    def update_pix(self, pix: Pix):
        """
        Atualizar pix.
        :param pix: object
        :return: bool
        """
        if not Instan.get_instance(pix, Pix):
            return False
        elif not pix.get_id() > 0:
            return False
        elif not pix.get_fk() > 0:
            return False
        return True if self._create_update_delete(pix) else False

    # delete pix

    def delete_pix(self, pix: Pix):
        """
        Esse metodo deleta pix pela chave.
        :param pix: object
        :return: bool
        """
        if not Instan.get_instance(pix, Pix):
            return False
        return True if self._create_update_delete(
            pix, delete=True) else False

    # select pix

    def find_pix(self, **kwargs):
        """
        Busca por pixs
        :param kwargs: dict
        :return: int
        """
        if not kwargs or not kwargs.__len__() > 0:
            return 0
        else:
            return 1

    # update and create

    def _create_update_delete(self, pix: Pix, delete=False):
        """
        Esse metodo serve para update, delete, e create.
        :param pix: object
        :param delete: bool (optional)
        :return: bool
        """
        if delete:
            return pix.get_id() > 0
        elif not self._get_name().validar_palavra(pix.get_nome()):
            return False
        return False if StrControl.is_none_or_empty(pix.get_chave()) else True

    # getter

    def _get_name(self):
        return self._name