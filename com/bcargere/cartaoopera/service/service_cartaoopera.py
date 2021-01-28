from decimal import Decimal
from com.bcargere.cartao.model.cartao import Cartao
from com.bcargere.cartaoopera.model.cartaoopera import CartaoOpera
from tools.cartao_check.cartao_check import CartaoCheck
from tools.data_check.data_check import DataCheck
from tools.instance_check.instance import Instan
from tools.money_check.money_check import MoneyCheck
from tools.name_check.name_check import NameCheck


class ServiceCartaoOpera:
    """
    Regra de negócio para operação de
    cartão.
    bcarsoft
    """

    def __init__(self):
        self._name_check = NameCheck()
        self._data_check = DataCheck()
        self._money_check = MoneyCheck()
        self._cartao_check = CartaoCheck()

    # create part

    def create_cartaoopera(self, cartaoopera):
        """
        Esse metódo registra uma compra de cartão de crédito.
        :param cartaoopera: CartaoOpera instance
        :return: bool
        """
        if not Instan.get_instance(cartaoopera, CartaoOpera):
            return False
        elif not self._check_n.validar_palavra(cartaoopera.nome):
            return False
        elif not self._check_n.validar_palavra(cartaoopera.descricao):
            return False
        elif not self._check_d.is_data_valida(cartaoopera.data):
            return False
        cartaoopera.valor = Decimal(
            self._check_m.str_converter_money(
                self._check_m.decimal_to_str(cartaoopera.valor)
            )
        )
        if not cartaoopera.valor:
            return False
        elif not self._check_cartao(cartaoopera.cartao):
            return False
        elif self._check_m.decimal_greater(
                dec_1=cartaoopera.valor, dec_2=self._limite_atual()):
            return False
        else:
            return True

    # delete part

    def delete_cartaoopera(self, cartaoopera):
        """
        Esse metodo deleta uma operação de cartão.
        :param cartaoopera: CartaoOpera instance
        :return: bool
        """
        if not Instan.get_instance(cartaoopera, CartaoOpera):
            return False
        elif not cartaoopera.id > 0 or not cartaoopera.fk > 0:
            return False
        else:
            return True

    # find part

    def find_cartaoopera(self, **kwargs):
        """
        Esse metodo serve para
        encontrar operação de cartão.
        Retorna a chave do registro.
        :param kwargs: dict
        :return: int
        """
        if not kwargs or kwargs.__len__() < 1:
            return 0
        else:
            return 1

    # special

    def _check_cartao(self, cartao):
        """
        Esse metodo verifica se o cartão é válido.
        :param cartao: Cartao instance
        :return: bool
        """
        if not Instan.get_instance(cartao, Cartao):
            return False
        elif not self._check_c.bandeira_checker(cartao.bandeira):
            return False
        elif not self._check_c.tipo_check(cartao.tipo):
            return False
        elif not self._check_c.nome_checker(cartao.nome_cartao):
            return False
        elif not self._check_c.str_to_number_cartao(cartao.numero):
            return False
        elif not self._check_c.data_checker(cartao.data_venc):
            return False
        elif not self._check_c.verifica_monetario(cartao.limite):
            return False
        elif not self._check_c.verifica_monetario(cartao.excedente):
            return False
        elif not self._check_c.verifica_monetario(cartao.fatura):
            return False
        elif not self._check_c.code_checker(cartao.codigo):
            return False
        else:
            cartao.numero = self._check_c.str_to_number_cartao(cartao.numero)
            return True

    def _limite_atual(self):
        """
        Esse metodo retorna apenas o limite valido
        para efeitos de comparação.
        :return: Decimal isntance
        """
        dec = cartaoopera.cartao.limite
        dec = self._check_m.soma_dinheiro(
            dec_1=dec,
            dec_2=cartaoopera.cartao.excedente
        )
        dec = self._check_m.subtrai_dinheiro(
            dec_1=dec,
            dec_2=cartaoopera.cartao.fatura
        )
        dec = Decimal(
            self._check_m.str_converter_money(
                self._check_m.decimal_to_str(dec)
            )
        )
        return dec

    # getters

    @property
    def _check_n(self):
        return self._name_check

    @property
    def _check_d(self):
        return self._data_check

    @property
    def _check_m(self):
        return self._money_check

    @property
    def _check_c(self):
        return self._cartao_check
