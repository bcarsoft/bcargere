from com.bcargere.pix.model.pix import Pix
from tools.instance_check.instance import Instan
from tools.name_check.name_check import NameCheck
from tools.strs_check.str_control import StrControl
from com.bcargere.pix.service.i_service_pix import IServicePix


class ServicePix(IServicePix):
    """
    Regra de negócio para pix
    - create;
    - update;
    - delete;
    - find;
    bcarsoft
    """

    def __init__(self):
        """novo service pix."""
        self._name_ = NameCheck()

    # create pix

    def create_pix(self, pix):
        """
        Criar novo pix.
        :param pix: object
        :return: bool
        """
        if not Instan.get_instance(pix, Pix):
            SingMessage.message().message = 'Error: Instancia Inválida.'
            return False
        elif not pix.fk > 0:
            SingMessage.message().message = 'Error: ID Banco Inválido.'
            return False
        return True if self._create_update_delete(pix) else False

    # update pix

    def update_pix(self, pix):
        """
        Atualizar pix.
        :param pix: object
        :return: bool
        """
        if not Instan.get_instance(pix, Pix):
            SingMessage.message().message = 'Error: Instancia Inválida.'
            return False
        elif not pix.id > 0:
            SingMessage.message().message = 'Error: ID Pix Inválido.'
            return False
        elif not pix.fk > 0:
            SingMessage.message().message = 'Error: ID Banco Inválido.'
            return False
        return True if self._create_update_delete(pix) else False

    # delete pix

    def delete_pix(self, pix):
        """
        Esse metodo deleta pix pela chave.
        :param pix: object
        :return: bool
        """
        if not Instan.get_instance(pix, Pix):
            SingMessage.message().message = 'Error: Instancia Inválida.'
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
            SingMessage.message().message = 'Error: Pesquisa Inválida.'
            return 0
        else:
            return 1

    # update and create

    def _create_update_delete(self, pix, delete=False):
        """
        Esse metodo serve para update, delete, e create.
        :param pix: object
        :param delete: bool (optional)
        :return: bool
        """
        if delete:
            if pix.id < 1:
                SingMessage.message().message = 'Error: ID Pix Inválido.'
            return pix.id > 0
        elif not self._name.validar_palavra(pix.nome):
            SingMessage.message().message = 'Error: Nome Invalido'
            return False
        if StrControl.is_none_or_empty(pix.chave):
            SingMessage.message().message = 'Error: Chave Pix Inválida.'
            return False
        return True

    # getter

    @property
    def _name(self):
        """
        Validador de palavra.
        :return: NameCheck instance
        """
        return self._name_
