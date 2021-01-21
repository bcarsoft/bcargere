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

    def crete_usuario(self, user: Usuario):
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
        elif user.get_id() < 1:
            return False
        else:
            return True

    # deletando usuário

    def delete_usuario(self, user: Usuario):
        """
        Esse metodo testa a chave para deleção de usuário.
        :param user: object
        :return: bool
        """
        if not Instan.get_instance(user, Usuario):
            return False
        elif not user.get_id() > 0:
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
        elif not self._get_name().validar_palavra(user.get_nome()):
            return False
        elif not self._get_data().is_data_valida(user.get_data_nasc()):
            return False
        elif not self._get_gender().gender_valid(user.get_genero()):
            return False
        elif not self._get_email().email_is_valid(user.get_email()):
            return False
        elif not self._get_user().validar_nome_usuario(user.get_usuario()):
            return False
        elif not self._get_pass().verifica_senha_app(user.get_senha()):
            return False
        elif not self._get_mobile().mobile_valid(user.get_telefone()):
            return False
        else:
            return True

    # getters

    def _get_name(self):
        return self._name

    def _get_data(self):
        return self._data

    def _get_gender(self):
        return self._gender

    def _get_email(self):
        return self._email

    def _get_user(self):
        return self._user

    def _get_pass(self):
        return self._pass

    def _get_mobile(self):
        return self._mobile
