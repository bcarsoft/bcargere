from com.bcargere.core.service.facade import Facade


class SingFacade:
    """
    Facade Singleton Pattern.
    bcarsoft
    """

    _instance = Facade()

    def __init__(self):
        """
        Facade Singleton.
        """
        pass

    @classmethod
    def facade(cls):
        """
        Retorna Facade encontrado.
        :return: Facade instance
        """
        if not cls._instance:
            cls._instance = Facade()
        return cls._instance
