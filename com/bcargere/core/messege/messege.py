from tools.strs_check.str_control import StrControl


class Message:
    """Classe responsavel pelas mensagens de
    - erro
    - sucesso
    nas operações feitas pelo software
    bcarsoft
    """

    def __str__(self):
        """String que representa a instância

        :return: str"""
        return 'Messagem ao Usuário'

    def __init__(self):
        """
        Nova Mensagem.
        """
        self._message = ''

    # getters and setters

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message: str):
        """
        Nova Mensagem.
        :param message: str
        :return: None
        """
        self._message = '' \
            if not message or StrControl.str_great(word=message, size=50) \
            else message
