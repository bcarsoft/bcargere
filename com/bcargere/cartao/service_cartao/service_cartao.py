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
        elif not cartao.get_fk() > 0:
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
        elif not cartao.get_id() > 0:
            return False
        elif not cartao.get_fk() > 0:
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
        return False if not cartao.get_id() > 0 else True

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

    def _check_create_update(self, cartao: Cartao):
        """
        Esse metodo faz a checagem de dados para criar e atualizar.
        :param cartao: object
        :return: bool
        """
        if not self._get_card().bandeira_checker(cartao.get_bandeira()):
            return False
        elif not self._get_card().tipo_check(cartao.get_tipo()):
            return False
        elif not self._get_card().nome_checker(cartao.get_nome_cartao()):
            return False
        elif not self._get_card().str_to_number_cartao(cartao.get_numero()):
            return False
        elif not self._get_card().data_checker(cartao.get_data_venc()):
            return False
        elif not self._get_card().code_checker(cartao.get_codigo()):
            return False
        elif not self._get_card().verifica_monetario(cartao.get_limite()):
            return False
        elif not self._get_card().verifica_monetario(cartao.get_excedente()):
            return False
        elif not self._get_card().verifica_monetario(cartao.get_fatura()):
            return False
        else:
            return True

    # metodo getter

    def _get_card(self):
        return self._card
