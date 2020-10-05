# roberta.kwarwp.kwarwppart.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Jogo para ensino de programação Python.

    .. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

    Classes neste módulo:
        - :py:class:`Vazio`     Espaço vago na arena do desafio.
        - :py:class:`Oca`       Destino final da aventura.
        - :py:class:`Piche`     Uma armadilha para prender o índio.
        - :py:class:`Tora`      Uma tora que o índio pode pegar.
        - :py:class:`Nulo`      Objeto Nulo para default em argumentos.

    Changelog
    ---------
    .. versionchanged::    20.08.b1
        modifica :meth:`Vazio.ocupou` para receber também a posição.
        - :py:class:`Nulo`      Objeto nulo passivo a todas as requisições.

    .. versionchanged::    20.08.b0
        Moveu constantes de classe VITOLLINO, LADO para Vazio.
        
    .. versionadded::    20.08.b0
        Moveu :class:`Vazio`, :class:`Oca`, :class:`Piche` para cá.
        Adicionou :class:`Tora` e classe :class:`Nulo`

"""


class Nulo:
    """Objeto nulo que responde passivamente a todas as requisições."""
    def __init__(self):
        self.pegar = self.ocupa = self.ocupou = self.elt = self.corrente = self.nulo
        
    def nulo(self, *_, **__):
        """Método nulo, responde passivamente a todas as chamadas.
        
        :param _: aceita todos os argumentos posicionais.
        :param __: aceita todos os argumentos nomeados.
        :return: retorna o próprio objeto nulo.
        """
        return self 

NULO = Nulo()


class Vazio():
    """ Cria um espaço vazio na taba, para alojar os elementos do desafio.

        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Cinha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :param taba: Referência onde ele pode encontrar a taba.
        :param ocupante: Objeto que ocupa inicialmente a vaga.
    """
    VITOLLINO, LADO = None, None
    
    def __init__(self, imagem, x, y, cena, taba, ocupante=None):
        self.lado = lado = self.LADO # or 100
        self.taba = taba
        self.posicao = (x//lado,y//lado-1)
        self.vazio = self.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self._nada = self.VITOLLINO.a()
        self.acessa = self._acessa
        """O **acessa ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_acessa ()** que é o estado vago, aceitando ocupantes"""
        self.ocupante = ocupante or NULO
        """O ocupante se não for fornecido é encenado pelo próprio vazio, agindo como nulo"""
        self.acessa(ocupante)
        self.sair = self._sair
        """O **sair ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_sair ()** que é o estado leniente, aceitando saidas"""

    def sai(self):
        """ Pedido por um ocupante para que desocupe a posição nela.
        """
        self.ocupante = NULO
        self.acessa = self._acessa
        self.sair = self._sair

    def limpa(self):
        """ Pedido por um ocupante para ele seja eliminado do jogo.
        """
        self._nada.ocupa(self.ocupante)
        """a figura do ocupante vai ser anexada ao elemento nada, que não é apresentado"""
        self.ocupante = self
        self.acessa = self._acessa
        self.sair = self._sair

    def pegar(self, requisitante):
        """ Consulta o ocupante atual se há permissão para pegar e entregar ao requistante.

            :param requistante: O ator querendo pegar o objeto.
        """
        self.ocupante.pegar(requisitante)
        
    def empurrar(self, requisitante, azimute):
        """ Consulta o ocupante atual se há permissão para pegar e entregar ao requistante.

            :param requistante: O ator querendo pegar o objeto.
        """
        if type(self.ocupante) is Tora:
            self.ocupante.empurrar(requisitante, azimute)

    def _valida_acessa(self, ocupante):
        """ Consulta o ocupante atual se há permissão para substituí-lo pelo novo ocupante.

            :param ocupante: O canditato a ocupar a posição corrente.
        """
        self.ocupante.acessa(ocupante)
        
    def _acessa(self, ocupante):
        """ Atualmente a posição está vaga e pode ser acessada pelo novo ocupante.
        
        A responsabilidade de ocupar definitivamente a vaga é do candidato a ocupante
        Caso ele esteja realmente apto a ocupar a vaga e deve cahamar de volta ao vazio
        com uma chamada ocupou.

            :param ocupante: O canditato a ocupar a posição corrente.
        """
        ocupante.ocupa(self)


    def acessar(self, ocupante, azimute):
        """ Faz o índio caminhar na direção em que está olhando.
        """
        destino = (self.posicao[0]+azimute.x, self.posicao[1]+azimute.y)
        """A posição para onde o índio vai depende do vetor de azimute corrente"""
        taba = self.taba.taba
        if destino in taba:
            vaga = taba[destino]
            """Recupera na taba a vaga para a qual o índio irá se transferir"""
            vaga.acessa(ocupante)


    def _sair(self):
        """Objeto tenta sair e recebe autorização para seguir"""
        self.ocupante.siga()      
    
    def _pede_sair(self):
        """Objeto tenta sair e consulta o ocupante para seguir"""
        self.ocupante.sair()      

    def ocupou(self, ocupante, pos=(0, 0)):
        """ O candidato à vaga decidiu ocupá-la e efetivamente entra neste espaço.
        
        :param ocupante: O canditato a ocupar a posição corrente.
        :param pos: A posição (atitude) do sprite do ocupante.

        Este ocupante vai entrar no elemento do Vitollino e definitivamente se tornar
        o ocupante da vaga. Com isso ele troca o estado do método acessa para primeiro
        consultar a si mesmo, o ocupante corrente usando o protocolo definido em
        **_valida_acessa ()**

        """
        self.vazio.ocupa(ocupante, pos)
        self.ocupante = ocupante
        self.acessa = self._valida_acessa
        self.sair = self._pede_sair

    @property        
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .

        No caso do espaço vazio, vai retornar um elemento que não contém nada.
        """
        return self._nada.elt
        
    def ocupa(self, vaga, *_):
        """ Pedido por uma vaga para que ocupe a posição nela.

        No caso do espaço vazio, não faz nada.
        """
        pass
        
    def sai(self):
        """ Pedido por um ocupante para que desocupe a posição nela.
        """
        self.ocupante = self
        self.acessa = self._acessa
        self.sair = self._sair


class Piche(Vazio):
    """ Poça de Piche que gruda o índio se ele cair nela.

        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Cinha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :param taba: Representa a taba onde o índio faz o desafio.
    """
   
    def __init__(self, imagem, x, y, cena, taba):
        self.taba = taba
        self.vaga = taba
        self.lado = lado = self.LADO or 100
        self.posicao = (x//lado,y//lado-1)
        self.vazio = self.VITOLLINO.a(imagem, w=lado, h=lado, x=0, y=0, cena=cena)
        # self._nada = Kwarwp.VITOLLINO.a()
        self.ocupante = NULO
        self.empurrante = NULO

        self.acessa = self._acessa
        """O **acessa ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_acessa ()** que é o estado vago, aceitando ocupantes"""
        self.sair = self._sair
        """O **sair ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_sair ()** que é o estado vago, aceitando ocupantes"""
        
    @property        
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .

        No caso do espaço vazio, vai retornar um elemento que não contém nada.
        """
        return self.vazio.elt
    
    def ocupa(self, vaga):
        """ Pedido por uma vaga para que ocupe a posição nela.
        
        :param vaga: A vaga que será ocupada pelo componente.

        No caso do índio, requisita que a vaga seja ocupada por ele.
        """
        self.vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga
    
    def _pede_sair(self):
        """Objeto tenta sair mas não é autorizado"""
        self.taba.fala("Você ficou preso no piche")       


class Oca(Piche):
    """  A Oca é o destino final do índio, não poderá sair se ele entrar nela.
    
        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Cinha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :param taba: Representa a taba onde o índio faz o desafio.
    """
    
    def _pede_sair(self):
        """Objeto tenta sair mas não é autorizado"""
        self.taba.fala("Você chegou no seu objetivo")       
        
    def _acessa(self, ocupante):
        """ Atualmente a posição está vaga e pode ser acessada pelo novo ocupante.
        
        A responsabilidade de ocupar definitivamente a vaga é do candidato a ocupante
        Caso ele esteja realmente apto a ocupar a vaga e deve cahamar de volta ao vazio
        com uma chamada ocupou.

            :param ocupante: O canditato a ocupar a posição corrente.
        """
        self.taba.fala("Você chegou no seu objetivo")       
        ocupante.ocupa(self)


class Tora(Piche):
    """  A Tora é um pedaço de tronco cortado que o índio pode carregar ou empurrar.
    
        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Linha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :param taba: Representa a taba onde o índio faz o desafio.
    """
        
    def pegar(self, requisitante):
        """ Consulta o ocupante atual se há permissão para pegar e entregar ao requistante.

            :param requistante: O ator querendo pegar o objeto.
        """
        vaga = requisitante
        self.vaga.sai()
        # self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga

    @property        
    def posicao(self):
        """ A propriedade posição faz parte do protocolo do double dispatch com o Indio .

        No caso da tora, retorna o a posição do atributo **self.vaga**.
        """
        return self.vaga.posicao

    @posicao.setter        
    def posicao(self, _):
        """ A propriedade posição faz parte do protocolo do double dispatch com o Indio .

        No caso da tora, é uma propriedade de somente leitura, não executa nada.
        """
        pass

    @property        
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .

        No caso da tora, retorna o elt do elemento do atributo **self.vazio**.
        """
        return self.vazio.elt
        
    def _acessa(self, ocupante):
        """ Pedido de acesso a essa posição, delegada ao ocupante pela vaga.
        
        :param ocupante: O componente candidato a ocupar a vaga já ocupada pelo índio.

        No caso da tora, ela age como um obstáculo e não prossegue com o protocolo.
        """
        pass
        
    def empurrar(self, empurrante, azimute):
        """ Registra o empurrante para uso no procolo e inicia dispathc com a vaga.
            :param requistante: O ator querendo pegar o objeto.
        """
        print("Estou sendo empurrada") 
        
        self.empurrante = empurrante
        # continue aqui com o início do double dispatch para ocupar a vaga na direção do azimute
        self.vaga.acessar(self, azimute)
        self.empurrante = NULO
        
    def ocupa(self, vaga):
        """ Pedido por uma vaga para que ocupe a posição nela.
        :param vaga: A vaga que será ocupada pelo componente.
        No caso da tora, requisita que a vaga seja ocupada por ele.
        Também autoriza o empurrante a ocupar a vaga onde estava.
        """
        # o código usual do ocupa
        self.vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)

        self.empurrante.ocupa(self.vaga) if self.empurrante is not NULO else None
        self.vaga = vaga

class Pedra(Tora):
    """  A Tora é um pedaço de tronco cortado que o índio pode carregar ou empurrar.
    
        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Linha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :param taba: Representa a taba onde o índio faz o desafio.
    """
    def pegar(self, requisitante):
        """ Consulta o ocupante atual se há permissão para pegar e entregar ao requistante.

            :param requistante: O ator querendo pegar o objeto.
        """
        print("Você não pode me pegar!")