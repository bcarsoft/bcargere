from com.bcargere.banco.model.banco import Banco
from tools.instance_check.instance import Instan
from tools.passw_check.passw import Passw
from tools.name_check.name_check import NameCheck
from tools.data_check.data_check import DataCheck
from tools.strs_check.str_control import StrControl
from tools.gender_check.gender_check import GenderCheck


class BancoCheck:
    """
    Essa classe é para a verificação de informações referentes a
    criação de conta bancária.
    bcarsoft
    """

    def __init__(self):
        self._passw = Passw()
        self._name = NameCheck()
        self._data = DataCheck()
        self._gender = GenderCheck()

    def validar_banco(self, banco):
        """
        Validar conta bancaria para registro.
        :param banco: Banco instance
        :return: bool
        """
        if not Instan.get_instance(banco, Banco):
            # se a instancia está incorreta
            return False
        elif not self._get_name_check().validar_palavra(banco.get_nome()):
            # nome do banco invalido
            return False
        elif not self._get_passw().verifica_senha_numerica(str(banco.get_codigo()), 3):
            # codigo do banco invalido
            return False
        elif not self._get_passw().verifica_senha_numerica(banco.get_num_agencia(), 5) and \
                not self._get_passw().verifica_senha_numerica(banco.get_num_agencia(), 6):
            # número de agência inválido
            return False
        elif not self._get_passw().verifica_senha_numerica(banco.get_num_conta(), 9, exact=False):
            # numero da conta invalido
            return False
        elif not self._is_tipo_valido(banco.get_tipo()):
            # tipo de conta inválido
            return False
        elif not self._get_name_check().validar_palavra(banco.get_titular()):
            # titular de conta invalido
            return False
        elif not self._get_gender_check().gender_valid(banco.get_genero()):
            # sexo invalido
            return False
        elif not self._get_data_check().is_data_valida(banco.get_data_nas()):
            # data de nascimento inválido
            return False
        elif not self._get_passw().verifica_senha_numerica(banco.get_senha_1(),
                                                           size=8, exact=False):
            # senha principal invalido
            return False
        elif not self._get_passw().verifica_senha_app(banco.get_senha_2(), size=12):
            # senha secundária inválida
            return False
        pass

    def _get_passw(self):
        """
        Retorna checagem de senha e numeros de
        agência e conta.
        :return: Passw instance
        """
        return self._passw

    def _get_name_check(self):
        """
        Retorna objeto para checar nome.
        :return: NameCheck instance
        """
        return self._name

    def _get_data_check(self):
        """
        Retorna objeto para checar data.
        :return: DataCheck instance
        """
        return self._data

    def _get_gender_check(self):
        """
        Retona objeto para checar sexo.
        :return: GenderCheck intance.
        """
        return self._gender

    def _is_tipo_valido(self, tipo=''):
        """
        Verifica se o tipo da conta atende aos paramentros:
        - deve ser:
            - Conta Poupança;
            - Conta Pagamento;
            - Conta Corrente;
        :param tipo: str
        :return: bool
        """
        tipo = StrControl.make_lowcase(tipo)
        contas = ('conta pagamento', 'conta corrente', 'conta poupança', )
        return tipo in contas
