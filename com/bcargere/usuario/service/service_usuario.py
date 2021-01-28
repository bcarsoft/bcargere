from com.bcargere.usuario.model.usuario import Usuario
from tools.data_check.data_check import DataCheck
from tools.email_check.email_check import EmailCheck
from tools.gender_check.gender_check import GenderCheck
from tools.instance_check.instance import Instan
from tools.mobile_check.mobile_check import MobileCheck
from tools.name_check.name_check import NameCheck
from tools.passw_check.passw import Passw
from tools.user_check.user_check import UserCheck


class ServiceUsuario:
    """
    Regra de negócio para a criação de usuário,
    deleção, atualização e busca.
    bcarsoft
    """

    def __init__(self):
        self._name = NameCheck()
        self._data = DataCheck()
        self._gender = GenderCheck()
        self._email = EmailCheck()
        self._user = UserCheck()
        self._pass = Passw()
        self._mobile = MobileCheck()

    # criando novo usuário

    def crete_usuario(self, user):
        """
        Metodo para testar novo usuário.
        :param user: object
        :return: bool
        """
        return False if not self._get_done_create_update(user) else True

    # atualizando usuário existente

    def update_usuario(self, user):
        """
        Metodo para testar atualizar usuário.
        :param user: object
        :return: bool
        """
        if not self._get_done_create_update(user):
            return False
        elif user.id < 1:
            return False
        else:
            return True

    # deletando usuário

    def delete_usuario(self, user):
        """
        Esse metodo testa a chave para deleção de usuário.
        :param user: object
        :return: bool
        """
        if not Instan.get_instance(user, Usuario):
            return False
        elif not user.id > 0:
            return False
        else:
            return True

    # buscando usuario

    def find_usuario(self, **kwargs):
        """
        Esse metodo serve para
        - entrar no aplicativo
        retorna a chave do registro.
        :param kwargs: dict
        :return: int
        """
        if not kwargs or kwargs.__len__() < 1:
            return 0
        else:
            return 1

    # metodos especiais

    def _get_done_create_update(self, user):
        """
        Esse metodo verifica os dados para criação e atualização.
        :param user: object
        :return: bool
        """
        if not Instan.get_instance(user, Usuario):
            return False
        elif not self._check_n.validar_palavra(user.nome):
            return False
        elif not self._check_d.is_data_valida(user.data_nasc):
            return False
        elif not self._check_g.gender_valid(user.genero):
            return False
        elif not self._check_e.email_is_valid(user.email):
            return False
        elif not self._check_u.validar_nome_usuario(user.usuario):
            return False
        elif not self._check_p.verifica_senha_app(user.senha):
            return False
        elif not self._check_m.mobile_valid(user.telefone):
            return False
        else:
            return True

    # getters

    @property
    def _check_n(self):
        return self._name

    @property
    def _check_d(self):
        return self._data

    @property
    def _check_g(self):
        return self._gender

    @property
    def _check_e(self):
        return self._email

    @property
    def _check_u(self):
        return self._user

    @property
    def _check_p(self):
        return self._pass

    @property
    def _check_m(self):
        return self._mobile
