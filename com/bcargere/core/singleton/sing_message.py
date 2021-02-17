from com.bcargere.core.messege.messege import Message


class SingMessage:
    """
    Message Singleton Pattern.
    bcarsoft
    """

    _instance = Message()

    def __init__(self):
        """Novo Message"""
        pass

    @classmethod
    def message(cls):
        """
        Message Instance.
        :return: Message
        """
        if not cls._instance:
            cls._instance = Message()
        return cls._instance
