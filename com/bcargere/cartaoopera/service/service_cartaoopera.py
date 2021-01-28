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
        elif not self._get_name_check() \
                .validar_palavra(cartaoopera.get_nome()):
            return False
        elif not self._get_name_check() \
                .validar_palavra(cartaoopera.get_descricao()):
            return False
        elif not self._get_data_check() \
                .is_data_valida(cartaoopera.get_data()):
            return False
        cartaoopera.set_valor(
            Decimal(
                self._get_money_check().str_converter_money(
                    self._get_money_check().decimal_to_str(
                        cartaoopera.get_valor()
                    )
                )
            )
        )
        if not cartaoopera.get_valor():
            return False
        elif not self._check_cartao(cartaoopera.get_cartao()):
            return False
        elif self._get_money_check()\
                .decimal_greater(dec_1=cartaoopera.get_valor(),
                                 dec_2=self._limite_atual()):
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
        elif not cartaoopera.get_id() > 0 or not cartaoopera.get_fk() > 0:
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
        elif not self._get_cartao_check()\
                .bandeira_checker(cartao.get_bandeira()):
            return False
        elif not self._get_cartao_check().tipo_check(cartao.get_tipo()):
            return False
        elif not self._get_cartao_check().nome_checker(cartao.get_nome_cartao()):
            return False
        elif not self._get_cartao_check()\
                .str_to_number_cartao(cartao.get_numero()):
            return False
        elif not self._get_cartao_check().data_checker(cartao.get_data_venc()):
            return False
        elif not self._get_cartao_check()\
                .verifica_monetario(cartao.get_limite()):
            return False
        elif not self._get_cartao_check()\
                .verifica_monetario(cartao.get_excedente()):
            return False
        elif not self._get_cartao_check().verifica_monetario(cartao.get_fatura()):
            return False
        elif not self._get_cartao_check().code_checker(cartao.get_codigo()):
            return False
        else:
            cartao.set_numero(
                self._get_cartao_check().str_to_number_cartao(
                    cartao.get_numero()
                )
            )
            return True

    def _limite_atual(self):
        """
        Esse metodo retorna apenas o limite valido
        para efeitos de comparação.
        :return: Decimal isntance
        """
        dec = cartaoopera.get_cartao().get_limite()
        dec = self._get_money_check().soma_dinheiro(
            dec_1=dec,
            dec_2=cartaoopera.get_cartao().get_excedente()
        )
        dec = self._get_money_check().subtrai_dinheiro(
            dec_1=dec,
            dec_2=cartaoopera.get_cartao().get_fatura()
        )
        dec = Decimal(
            self._get_money_check().str_converter_money(
                self._get_money_check().decimal_to_str(dec)
            )
        )
        return dec

    # getters

    def _get_name_check(self):
        return self._name_check

    def _get_data_check(self):
        return self._data_check

    def _get_money_check(self):
        return self._money_check

    def _get_cartao_check(self):
        return self._cartao_check
