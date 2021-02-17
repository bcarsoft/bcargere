from com.bcargere.banco.service.service_banco import ServiceBanco
from com.bcargere.cartao.service.service_cartao import ServiceCartao
from com.bcargere.cartaoopera.service.service_cartaoopera import ServiceCartaoOpera
from com.bcargere.core.service.i_facade import IFacade
from com.bcargere.pix.service.service_pix import ServicePix
from com.bcargere.pixopera.service.service_pixopera import ServicePixOpera
from com.bcargere.potes.service.service_potes import ServicePotes
from com.bcargere.potesopera.service.service_postesopera import ServicePosteOpera
from com.bcargere.transacoes.service.service_transacoes import ServiceTransacoes
from com.bcargere.usuario.service.service_usuario import ServiceUsuario
from com.bcargere.variacao.service.service_variacao import ServiceVariacao


class Facade(IFacade):
    """Essa é a fachada do projeto,
    nela se encontram os caminhos para
    testes e banco de dados.
    bcarsoft
    """

    # variaveis
    _serv_banco = ServiceBanco()
    _serv_cartao = ServiceCartao()
    _serv_cartao_opera = ServiceCartaoOpera()
    _serv_pix = ServicePix()
    _serv_pix_opera = ServicePixOpera()
    _serv_potes = ServicePotes()
    _serv_potes_opera = ServicePosteOpera()
    _serv_transacoes = ServiceTransacoes()
    _serv_usuario = ServiceUsuario()
    _serv_variacao = ServiceVariacao()
    # variaveis

    def __init__(self):
        """Nova Fachada
        """
        pass

    # banco

    def create_banco(self, banco):
        """
        novo banco.
        :param banco: Banco instance
        :return: bool
        """
        return self._serv_banco.create_banco(banco=banco)

    def update_banco(self, banco):
        """
        atualiza banco.
        :param banco: Banco instance
        :return: bool
        """
        return self._serv_banco.update_banco(banco=banco)

    def delete_banco(self, banco):
        """
        delete banco.
        :param banco: Banco isntance
        :return: bool
        """
        return self._serv_banco.delete_banco(banco=banco)

    def find_banco(self, **kwargs):
        """
        pesquisa banco.
        :param kwargs: dict
        :return: Banco
        """
        return self._serv_banco.find_banco(**kwargs)

    # cartão

    def create_cartao(self, cartao):
        """
        novo cartao.
        :param cartao: Cartao instance
        :return: bool
        """
        return self._serv_cartao.create_cartao(cartao=cartao)

    def update_cartao(self, cartao):
        """
        atualiza cartao.
        :param cartao: Cartao instance
        :return: bool
        """
        return self._serv_cartao.update_cartao(cartao=cartao)

    def delete_cartao(self, cartao):
        """
        deleta cartao.
        :param cartao: Cartao instance
        :return: bool
        """
        return self._serv_cartao.delete_cartao(cartao=cartao)

    def find_cartao(self, **kwargs):
        """
        pesquisa cartao.
        :param kwargs: dict
        :return: Cartao
        """
        return self._serv_cartao.find_cartao(**kwargs)

    # cartao opera

    def create_cartaoopera(self, cartaoopera):
        """
        novo cartao opera.
        :param cartaoopera: CartaoOpera instance
        :return: bool
        """
        return self._serv_cartao_opera.create_cartaoopera(cartaoopera=cartaoopera)

    def delete_cartaoopera(self, cartaoopera):
        """
        delete cartao opera.
        :param cartaoopera: CartaoOpera instance
        :return: bool
        """
        return self._serv_cartao_opera.delete_cartaoopera(cartaoopera=cartaoopera)

    def find_cartaoopera(self, **kwargs):
        """
        pesquisa cartao opera.
        :param kwargs: dict
        :return: CartaoOpera
        """
        return self._serv_cartao_opera.find_cartaoopera(**kwargs)

    # pix

    def create_pix(self, pix):
        """
        novo pix.
        :param pix: Pix instance
        :return: bool
        """
        return self._serv_pix.create_pix(pix=pix)

    def update_pix(self, pix):
        """
        atualiza pix.
        :param pix: Pix instance
        :return: bool
        """
        return self._serv_pix.update_pix(pix=pix)

    def delete_pix(self, pix):
        """
        deleta pix.
        :param pix: Pix instance
        :return: bool
        """
        return self._serv_pix.delete_pix(pix=pix)

    def find_pix(self, **kwargs):
        """
        pesquisa pix.
        :param kwargs: dict
        :return: Pix
        """
        return self._serv_pix.find_pix(**kwargs)

    # pix opera

    def create_pixopera(self, pixopera):
        """
        novo pix opera.
        :param pixopera: PixOpera instance
        :return: bool
        """
        return self._serv_pix_opera.create_pixopera(pixopera=pixopera)

    def delete_pixopera(self, pixopera):
        """
        deleta pix opera.
        :param pixopera: PixOpera instance
        :return: bool
        """
        return self._serv_pix_opera.delete_pixopera(pixopera=pixopera)

    def find_pixopera(self, **kwargs):
        """
        pesquisa pix opera.
        :param kwargs: dict
        :return: PixOpera
        """
        return self._serv_pix_opera.find_pixopera(**kwargs)

    # potes

    def create_potes(self, potes):
        """
        novo pote.
        :param potes: Potes instance
        :return: bool
        """
        return self._serv_potes.create_potes(potes=potes)

    def update_potes(self, potes):
        """
        atualiza pote.
        :param potes: Potes instance
        :return: bool
        """
        return self._serv_potes.update_potes(potes=potes)

    def delete_potes(self, potes):
        """
        delete pote.
        :param potes: Potes instance
        :return: bool
        """
        return self._serv_potes.delete_potes(potes=potes)

    def find_potes(self, **kwargs):
        """
        pesquisa potes.
        :param kwargs: dict
        :return: Potes
        """
        return self._serv_potes.find_potes(**kwargs)

    # potes opera

    def create_potesopera(self, potesopera):
        """
        novo potesopera.
        :param potesopera: PotesOpera instance
        :return: bool
        """
        return self._serv_potes_opera.create_potesopera(potesopera=potesopera)

    def delete_potesopera(self, potesopera):
        """
        delete potesopera.
        :param potesopera: PotesOpera instance
        :return: bool
        """
        return self._serv_potes_opera.delete_potesopera(potesopera=potesopera)

    def find_potesopera(self, **kwargs):
        """
        pesquisa potes opera.
        :param kwargs: dict
        :return: PotesOpera
        """
        return self._serv_potes_opera.find_potesopera(**kwargs)

    # transacoes

    def create_transacoes(self, transacao):
        """
        nova transacao.
        :param transacao: Transacao instance
        :return: bool
        """
        return self._serv_transacoes.create_transacoes(transacao=transacao)

    def delete_transacoes(self, transacao):
        """
        delete transacao.
        :param transacao: Transacao instance
        :return: bool
        """
        return self._serv_transacoes.delete_transacoes(transacao=transacao)

    def find_transacoes(self, **kwargs):
        """
        pesquisa transacao.
        :param kwargs: dict
        :return: Transacao
        """
        return self._serv_transacoes.find_transacoes(**kwargs)

    # usuario

    def create_usuario(self, user):
        """
        novo usuario.
        :param user: Usuario instance
        :return: bool
        """
        return self._serv_usuario.create_usuario(user=user)

    def update_usuario(self, user):
        """
        atualiza usuario.
        :param user: Usuario instance
        :return: bool
        """
        return self._serv_usuario.update_usuario(user=user)

    def delete_usuario(self, user):
        """
        deleta usuario.
        :param user: Usuario instance
        :return: bool
        """
        return self._serv_usuario.delete_usuario(user=user)

    def find_usuario(self, **kwargs):
        """
        pesquisa usuario (login).
        :param kwargs: dict
        :return: Usuario
        """
        return self._serv_usuario.find_usuario(**kwargs)

    # variacao

    def create_variacao(self, variacao):
        """
        nova variacao.
        :param variacao: Variacao instance
        :return: bool
        """
        return self._serv_variacao.create_variacao(variacao=variacao)

    def update_variacao(self, variacao):
        """
        atualiza variacao.
        :param variacao: Variacao instance
        :return: bool
        """
        return self._serv_variacao.update_variacao(variacao=variacao)

    def find_variacao(self, **kwargs):
        """
        pesquisa variacao.
        :param kwargs: dict
        :return: Variacao
        """
        return self._serv_variacao.find_variacao(**kwargs)

    def delete_variacao(self, variacao):
        """
        deleta variaco.
        :param variacao: Variacao instance
        :return: bool
        """
        return self._serv_variacao.delete_variacao(variacao=variacao)

    # end
