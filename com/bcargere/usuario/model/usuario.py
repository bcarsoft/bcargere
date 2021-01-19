from com.bcargere.core.model.absmodel import AbsModel
from com.bcargere.data.model.data import Data


class User(AbsModel):
    """
        Classe para usuário do aplicativo.
        bcarsoft
    """

    def __init__(self):
        """Construtor"""
        super().__init__()
        self._nome = ''
        self._data_nas = Data()
        self._genero = ''
        self._email = ''
        self._usuario = ''
        self._senha = ''
        self._telefone = ''

    # getters and setters

    def set_nome(self, nome: str):
        """
        Esse metodo insere o nome
        :param nome: str
        """
        self._nome = nome

    def get_nome(self):
        """
        Esse metodo retorna o nome
        :return: str
        """
        return self._nome

    def get_data_nasc(self):
        """
        Esse metodo retorna a instancia para registro
        de data de nascimento
        :return: Data instance
        """
        return self._data_nas

    def set_genero(self, genero: str):
        """
        Esse metodo insere o genero
        :param genero: str
        """
        self._genero = genero

    def get_genero(self):
        """
        Esse metodo retorna o genero
        :return: str
        """
        return self._genero

    def set_email(self, email: str):
        """
        Esse metodo insere o email
        :param email: str
        """
        self._email = email

    def get_email(self):
        """
        Esse metodo retorna o email
        :return: str
        """
        return self._email

    def set_usuario(self, usuario: str):
        """
        Esse metodo insere o nome de usuário
        :param usuario: str
        """
        self._usuario = usuario

    def get_usuario(self):
        """
        Esse metodo retorna o nome de usuário
        :return: str
        """
        return self._usuario

    def set_senha(self, senha: str):
        """
        Esse metodo insere a senha de usuário do app
        :param senha: str
        """
        self._senha = senha

    def get_senha(self):
        """
        Esse metodo retorna a senha de usuario
        :return: str
        """
        return self._senha

    def set_telefone(self, telefone: str):
        """
        Esse metódo insere o telefone
        :param telefone: str
        """
        self._telefone = telefone

    def get_telefone(self):
        """
        Esse metodo retorna o telefone
        :return: str
        """
        return self._telefone
