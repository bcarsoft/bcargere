from com.bcargere.cartao.model.cartao import Cartao
from tools.cartao_check.cartao_check import CartaoCheck
from tools.instance_check.instance import Instan


class ServiceCartao:
    """
    Regra de negócio para Cartão
    - create, - update, - delete, - select
    bcarsoft
    """

    def __init__(self):
        self._card = CartaoCheck()

    # cria cartão

    def create_cartao(self, cartao):
        """
        Cria um novo cartão.
        :param cartao: object
        :return: bool
        """
        if not Instan.get_instance(cartao, Cartao):
            return False
        elif not cartao.fk > 0:
            return False
        return False if not self._check_create_update(cartao) else True

    # atualiza cartao

    def update_cartao(self, cartao):
        """
        Atualiza um cartão.
        :param cartao: object
        :return: bool
        """
        if not Instan.get_instance(cartao, Cartao):
            return False
        elif not cartao.id > 0:
            return False
        elif not cartao.fk > 0:
            return False
        return False if not self._check_create_update(cartao) else True

    # deleta cartao

    def delete_cartao(self, cartao):
        """
        Esse metodo pode deletar um cartão.
        :param cartao: object
        :return: bool
        """
        if not Instan.get_instance(cartao, Cartao):
            return False
        return False if not cartao.id > 0 else True

    # busca cartao

    def find_cartao(self, **kwargs):
        """
        Esse metodo busca cartão.
        :param kwargs: dict
        :return: int
        """
        if not kwargs or not kwargs.__len__() > 0:
            return 0
        else:
            return 1

    # fazendo aprovação create / update

    def _check_create_update(self, cartao):
        """
        Esse metodo faz a checagem de dados para criar e atualizar.
        :param cartao: object
        :return: bool
        """
        if not self._card_.bandeira_checker(cartao.bandeira):
            return False
        elif not self._card_.tipo_check(cartao.tipo):
            return False
        elif not self._card_.nome_checker(cartao.nome_cartao):
            return False
        elif not self._card_.str_to_number_cartao(cartao.numero):
            return False
        elif not self._card_.data_checker(cartao.data_venc):
            return False
        elif not self._card_.code_checker(cartao.codigo):
            return False
        elif not self._card_.verifica_monetario(cartao.limite):
            return False
        elif not self._card_.verifica_monetario(cartao.excedente):
            return False
        elif not self._card_.verifica_monetario(cartao.fatura):
            return False
        else:
            return True

    # metodo getter

    @property
    def _card_(self):
        return self._card
