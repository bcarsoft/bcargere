from com.bcargere.core.model.absmodel import AbsModel
from com.bcargere.data.model.data import Data


class Usuario(AbsModel):
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

    @property
    def nome(self):
        """
        Esse metodo retorna o nome
        :return: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        """
        Esse metodo insere o nome
        :param nome: str
        """
        self._nome = nome

    @property
    def data_nasc(self):
        """
        Esse metodo retorna a instancia para registro
        de data de nascimento
        :return: Data instance
        """
        return self._data_nas

    @property
    def genero(self):
        """
        Esse metodo retorna o genero
        :return: str
        """
        return self._genero

    @genero.setter
    def genero(self, genero: str):
        """
        Esse metodo insere o genero
        :param genero: str
        """
        self._genero = genero

    @property
    def email(self):
        """
        Esse metodo retorna o email
        :return: str
        """
        return self._email
    @email.setter
    def email(self, email: str):
        """
        Esse metodo insere o email
        :param email: str
        """
        self._email = email

    @property
    def usuario(self):
        """
        Esse metodo retorna o nome de usuário
        :return: str
        """
        return self._usuario

    @usuario.setter
    def usuario(self, usuario: str):
        """
        Esse metodo insere o nome de usuário
        :param usuario: str
        """
        self._usuario = usuario

    @property
    def senha(self):
        """
        Esse metodo retorna a senha de usuario
        :return: str
        """
        return self._senha

    @senha.setter
    def senha(self, senha: str):
        """
        Esse metodo insere a senha de usuário do app
        :param senha: str
        """
        self._senha = senha

    @property
    def telefone(self):
        """
        Esse metodo retorna o telefone
        :return: str
        """
        return self._telefone

    @telefone.setter
    def telefone(self, telefone: str):
        """
        Esse metódo insere o telefone
        :param telefone: str
        """
        self._telefone = telefone
