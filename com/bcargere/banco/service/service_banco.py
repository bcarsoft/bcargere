from tools.banco_check.banco_check import BancoCheck
from com.bcargere.banco.model.banco import Banco
from tools.instance_check.instance import Instan


class ServiceBanco:
    """
    Regra de negócio para criação de contas bancárias.
    bcarsoft
    """

    def __init__(self):
        self._ban_check = BancoCheck()

    # criar conta bancaria

    def create_banco(self, banco):
        """
        Registrar nova conta bancaria.
        :param banco: object
        :return: bool
        """
        if not Instan.get_instance(banco, Banco):
            return False
        elif not banco.fk > 0:
            return False
        return False if not \
            self._check_b.validar_banco(banco) else True

    # atualizar conta bancaria

    def update_banco(self, banco):
        """
        Atualizar conta bancaria.
        :param banco: object
        :return: bool
        """
        if not Instan.get_instance(banco, Banco):
            return False
        if not banco.id > 0:
            return False
        elif not banco.fk > 0:
            return False
        return False if not \
            self._check_b.validar_banco(banco) else True

    # deletar conta bancaria

    def delete_banco(self, banco):
        """
        Deletar conta bancária.
        :param banco: oject
        :return: bool
        """
        if not banco.id > 0 or not banco.fk > 0:
            return False
        else:
            return True

    # buscar conta bancaria

    def find_banco(self, **kwargs):
        """
        Esse metodo serve para
        encontrar conta bancaria.
        Retorna a chave do registro.
        :param kwargs: dict
        :return: int
        """
        if not kwargs or kwargs.__len__() < 1:
            return 0
        else:
            return 1

    # metodo getter

    @property
    def _check_b(self):
        return self._ban_check
