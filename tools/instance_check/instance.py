class Instan:
    """
    Classe que verifica classe de instâncias.
    bcarsoft
    """

    def __init__(self):
        pass

    @staticmethod
    def get_instance(value, instan):
        """
        Esse metodo verifica a classe de um
        objeto.
        :param value: objeto
        :param instan: objeto
        :return: bool
        """
        return isinstance(value, instan)
