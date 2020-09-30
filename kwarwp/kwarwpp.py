# roberta.kwarwp.kwarwpp.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Jogo para ensino de programação Python.

    .. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

    Classes neste módulo:
        - :py:class:`Kwarwp`    Jogo para ensino de programação.
        - :py:class:`Indio`     Personagem principal do jogo.
        - :py:class:`JogoProxy` Proxy que enfileira comandos gráficos.

    Changelog
    ---------

    .. versionadded::    20.08.b1
        Adicionou :class:`JogoProxy` para realizar o passo a passo.
        Capacidade de gerenciar mais de um índio.

    .. versionchanged::    20.08.b0
        Moveu constantes de classe VITOLLINO, LADO para Vazio.
        Moveu :class:`Vazio`, :class:`Oca`, :class:`Piche` para kwarwpart.
        
    .. versionadded::    20.08.a3
        Movimentação do índio para :py:meth:`Indio.esquerda` e 
        :py:meth:`Indio.direita`. Fala do índio: :py:meth:`Indio.fala`.
        classes Oca e Piche, double dispatch para sair.
            
    .. versionadded::    20.08.a2
        Classe Vazio que recebe cada componente do mapa.
        Movimentação do índio é feita pulando para outro vazio.
            
    .. versionadded::    20.08.a1
        Classe Indio que executa roteiro e anda.
            
    .. versionadded::    20.08.a0
        Fábrica de componentes
        classe Indio.
        Usa um mapa de caracteres para colocar os elementos.
            
    .. versionadded::    20.07
        classe Kwarwp.

"""
from collections import namedtuple as nt, deque
from kwarwp.kwarwppart import Vazio, Piche, Oca, Tora, NULO

IMGUR = "https://imgur.com/"
"""Prefixo do site imgur."""
MAPA_INICIO = """
@....&
......
......
.#.^..
"""
"""Mapa com o posicionamento inicial dos elementos."""
Ponto = nt("Ponto", "x y")
"""Par de coordenadas na direção horizontal (x) e vertiacal (y)."""
Rosa = nt("Rosa", "n l s o")
"""Rosa dos ventos com as direções norte, leste, sul e oeste."""


class JogoProxy():
    """ Proxy que enfileira comandos gráficos.
    
    :param vitollino: Empacota o engenho de jogo Vitollino.
    :param elt: Elemento que vai ser encapsulado pelo proxy.
    :param proxy: Referência para o objeto proxy parente.
    :param master: Determina se este elemento vai ser mestre de comandos.
    """
    def __init__(self, vitollino=None, elt=None, proxy=None, master=False):
        class AdaptaElemento(vitollino.a):
            """ Adapta um Elemento do Vitollino para agrupar ocupa e pos.

            """
                
            def ocupa(self, ocupante=None, pos=(0, 0)):
                ocupante = ocupante or NULO
                ocupante.pos = pos
                # print(f"AdaptaElemento pos: {self.pos}")
                super().ocupa(ocupante) if ocupante else None

        self.v = vitollino
        self.proxy = proxy or self
        self.master = master
        self._corrente = self
        self.comandos = []
        self._ativa = False
        """Cria um referência para o jogo do vitollino"""
        self.ae = AdaptaElemento
        """Cria um referência o Adapador de Eelementos"""
        self.elt = elt
        
    @property    
    def siz(self):
        """Propriedade tamanho"""
        return self.elt.siz
        
    def a(self, *args, **kwargs):
        """Método fábrica - Encapsula a criação de elementos
        
        :param args: coleção de argumentos posicionais.
        :param kwargs: coleção de argumentos nominais.
        :return: Proxy para um Elemento construído com estes argumentos.
        
        """
        return JogoProxy(elt=self.ae(*args, **kwargs), vitollino=self.v, proxy=self)
        
    def e(self, *args, **kwargs):
        """Método fábrica - Encapsula a criação de elementos ativos, que executam scripts
        
        :param args: coleção de argumentos posicionais.
        :param kwargs: coleção de argumentos nominais.
        :return: Proxy para um Elemento construído com estes argumentos.
        
        """
        return JogoProxy(elt=self.ae(*args, **kwargs), vitollino=self.v, proxy=self, master=True)
        
    def cria(self):
        """Fábrica do JogoProxy"""
        return self
    
    @property    
    def corrente(self):
        """Ativa Fábrica do JogoProxy"""
        return self.proxy._corrente

    @corrente.setter
    def corrente(self, mestre):
        """Ativa Fábrica do JogoProxy"""
        self._corrente = mestre
        
    def ativa(self):
        """Ativa Fábrica do JogoProxy"""
        # JogoProxy.ATIVA = True
        self._ativa = True
        self.proxy.corrente = self
        
    def lidar(self, metodo):
        """Lida com modo de operação do JogoProxy"""
        #self.master.corrente(self)
        self.ativa() if self.master else None
        print(self._ativa, self.proxy._ativa, metodo)
        self.corrente._enfileira(metodo) if self.proxy._ativa else self._executa(metodo)
        
    def c(self, *args, **kwargs):
        """Encapsula a criação de cenas - apenas delega.
        
        :param args: coleção de argumentos posicionais.
        :param kwargs: coleção de argumentos nominais.
        :return: Uma Cena do Vitollino construída com estes argumentos.
        
        """
        return self.v.c(*args, **kwargs)
        
    @siz.setter    
    def siz(self, value):
        """Propriedade tamanho"""
        self.elt.siz = value
        
    @property    
    def pos(self):
        """Propriedade posição"""
        return self.elt.pos
        
    @property    
    def x(self):
        """Propriedade posição x"""
        return self.elt.x
        
    @property    
    def y(self):
        """Propriedade posição y"""
        return self.elt.y
        
    @pos.setter    
    def pos(self, value):
        """Propriedade posição"""
        def _pos(val=value):
            self.elt.pos = val
        self.lidar(_pos)

    def ocupa(self, ocupante=None, pos=(0, 0)):
        """Muda a posição e atitude de um elemento"""
        def _pos(val=ocupante):
            destino = val.elt if val else None
            self.elt.ocupa(destino, pos)
        self.lidar(_pos)

    def _enfileira(self, metodo):
        """Coloca um comando na fila"""
        self.comandos.append(metodo)

    def _executa(self, metodo):
        """Executa imediamente um comando, não põe na fila"""
        metodo()

    def executa(self, *_):
        """Tira e executa um comando na fila"""
        self.comandos.pop(0)() if self.comandos else None


class Indio():
    """ Cria o personagem principal na arena do Kwarwp na posição definida.

        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Cinha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :param taba: Representa a taba onde o índio faz o desafio.
    """
    AZIMUTE = Rosa(Ponto(0, -1),Ponto(1, 0),Ponto(0, 1),Ponto(-1, 0),)
    """Constante com os pares ordenados que representam os vetores unitários dos pontos cardeais."""
    
    def __init__(self, imagem, x, y, cena, taba, vitollino=None):
        self.vitollino = vitollino or Vazio.VITOLLINO
        self.lado = lado = Vazio.LADO
        self.azimute = self.AZIMUTE.n
        """índio olhando para o norte"""
        self.taba = taba
        self.vaga = self
        self.ocupante = NULO
        self.posicao = (x//lado,y//lado) 
        self.indio = self.vitollino.e(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self.x = x
        """Este x provisoriamente distingue o índio de outras coisas construídas com esta classe"""
        if x:
            self.indio.siz = (lado*3, lado*4)
            """Define as proporções da folha de sprites"""
            self.gira()
       
    def ativa(self):
        """ Ativa o proxy do índio para enfileirar comandos.
        """
        #self.vitollino.ativa()
        self.indio.ativa()
       
    def gira(self):
        """ Modifica a figura (Sprite) do índio mostrando para onde está indo.
        """
        sprite_col = sum(self.posicao) % 3
        """Faz com que três casas adjacentes tenha valores diferentes para a coluna do sprite"""
        sprite_lin = self.AZIMUTE.index(self.azimute)
        """A linha do sprite depende da direção dque índio está olhando"""
        # self.indio.ocupa(ocupante=ocupante, pos=(-self.lado*sprite_col, -self.lado*sprite_lin))
        # self.indio.pos = (-self.lado*sprite_col, -self.lado*sprite_lin)
        pos = (-self.lado*sprite_col, -self.lado*sprite_lin)
        self.indio.pos = pos
       
    def mostra(self, vaga=None):
        """ Modifica a figura (Sprite) do índio mostrando para onde está indo.
        """
        sprite_col = sum(self.posicao) % 3
        """Faz com que três casas adjacentes tenha valores diferentes para a coluna do sprite"""
        sprite_lin = self.AZIMUTE.index(self.azimute)
        """A linha do sprite depende da direção dque índio está olhando"""
        # self.indio.ocupa(ocupante=ocupante, pos=(-self.lado*sprite_col, -self.lado*sprite_lin))
        # self.indio.pos = (-self.lado*sprite_col, -self.lado*sprite_lin)
        pos = (-self.lado*sprite_col, -self.lado*sprite_lin)
        vaga.ocupou(self, pos) # if vaga else self.indio.ocupa(None,pos=pos)
       
    def esquerda(self):
        """ Faz o índio mudar da direção em que está olhando para a esquerda.
        """
        self.azimute = self.AZIMUTE[self.AZIMUTE.index(self.azimute)-1]
        self.gira()
       
    def direita(self):
        """ Faz o índio mudar da direção em que está olhando para a direita.
        """
        self.azimute = self.AZIMUTE[self.AZIMUTE.index(self.azimute)-3]
        self.gira()
       
    def fala(self, texto=""):
        """ O índio fala um texto dado.
        
        :param texto: O texto a ser falado.
        """
        self.taba.fala(texto)

    def anda(self):
        """Objeto tenta sair, tem que consultar a vaga onde está"""
        self.vaga.sair()      

    def pega(self):
        """tenta pegar o objeto que está diante dele"""
        destino = (self.posicao[0]+self.azimute.x, self.posicao[1]+self.azimute.y)
        """A posição para onde o índio vai depende do vetor de azimute corrente"""
        taba = self.taba.taba
        if destino in taba:
            vaga = taba[destino]
            """Recupera na taba a vaga para a qual o índio irá se transferir"""
            vaga.pegar(self)

    def larga(self):
        """tenta largar o objeto que está segurando"""
        destino = (self.posicao[0]+self.azimute.x, self.posicao[1]+self.azimute.y)
        """A posição para onde o índio vai depende do vetor de azimute corrente"""
        taba = self.taba.taba
        if destino in taba:
            vaga = taba[destino]
            """Recupera na taba a vaga para a qual o índio irá se transferir"""
            # self.ocupante.largar(vaga)
            vaga.acessa(self.ocupante)

    def sair(self):
        """Objeto de posse do índio tenta sair e é autorizado"""
        self.vaga.ocupante.siga()      

    def siga(self):
        """Objeto tentou sair e foi autorizado"""
        self._anda()       

    def _anda(self):
        """ Faz o índio caminhar na direção em que está olhando.
        """
        destino = (self.posicao[0]+self.azimute.x, self.posicao[1]+self.azimute.y)
        """A posição para onde o índio vai depende do vetor de azimute corrente"""
        taba = self.taba.taba
        if destino in taba:
            vaga = taba[destino]
            """Recupera na taba a vaga para a qual o índio irá se transferir"""
            vaga.acessa(self)
 
    def ocupou(self, ocupante):
        """ O candidato à vaga decidiu ocupá-la e efetivamente entra neste espaço.
        
        :param ocupante: O canditato a ocupar a posição corrente.
        
        Este ocupante vai entrar no elemento do Vitollino e definitivamente se tornar
        o ocupante da vaga. Com isso ele troca o estado do método acessa para primeiro
        consultar a si mesmo, o ocupante corrente usando o protocolo definido em
        **_valida_acessa ()**

        """
        self.indio.ocupa(ocupante)
        self.ocupante = ocupante
        
    def sai(self):
        """ Rotina de saída falsa, o objeto Indio é usado como uma vaga nula.
        """
        pass
         
    def executa(self):
        """ Roteiro do índio. Conjunto de comandos para ele executar.
        """
        pass
        
    def passo(self):
        self.indio.executa()

    @property        
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .

        No caso do índio, retorna o elt do elemento do atributo **self.indio**.
        """
        return self.indio.elt
        
    def ocupa(self, vaga, *_):
        """ Pedido por uma vaga para que ocupe a posição nela.
        
        :param vaga: A vaga que será ocupada pelo componente.

        No caso do índio, requisita que a vaga seja ocupada por ele.
        """
        self.vaga.sai()
        self.posicao = vaga.posicao
        self.mostra(vaga) if self.x else vaga.ocupou(self)
        self.vaga = vaga
        # if self.x:
        #     self.mostra()
        
    def acessa(self, ocupante):
        """ Pedido de acesso a essa posição, delegada ao ocupante pela vaga.
        
        :param ocupante: O componente candidato a ocupar a vaga já ocupada pelo índio.

        No caso do índio, ele age como um obstáculo e não prossegue com o protocolo.
        """
        pass


class Kwarwp():
    """ Jogo para ensino de programação.
    
        :param vitollino: Empacota o engenho de jogo Vitollino.
        :param mapa: Um texto representando o mapa do desafio.
        :param medidas: Um dicionário usado para redimensionar a tela.
    """
    
    def __init__(self, vitollino=None, mapa=None, medidas={}, indios=()):
        Vazio.VITOLLINO = self.v = vitollino()
        self.vitollino = vitollino
        """Referência estática para obter o engenho de jogo."""
        self.mapa = (mapa or MAPA_INICIO).split()
        """Cria um matriz com os elementos descritos em cada linha de texto"""
        self.taba = {}
        """Cria um dicionário com os elementos traduzidos a partir da interpretação do mapa"""
        self.o_indio = NULO
        self.os_indios = []
        """Instância do personagem principal, o índio, vai ser atribuído pela fábrica do índio"""
        self.lado, self.col, self.lin = 100, len(self.mapa[0]), len(self.mapa)+1
        """Largura da casa da arena dos desafios, número de colunas e linhas no mapa"""
        Vazio.LADO = self.lado
        """Referência estática para definir o lado do piso da casa."""
        w, h = self.col *self.lado, self.lin *self.lado
        medidas.update(width=w, height=f"{h}px")
        self.indios = deque(indios or [Indio])
        self.cena = self.cria(mapa=self.mapa) if vitollino else None

    def cria(self, mapa=""):
        """ Fábrica de componentes.
        
        :param mapa: Um texto representando o mapa do desafio.
        """
        Fab = nt("Fab", "objeto imagem")
        """Esta tupla nomeada serve para definir o objeto construido e sua imagem."""

        fabrica = {
        "&": Fab(self.maloc, f"{IMGUR}dZQ8liT.jpg"), # OCA
        "^": Fab(self.indio, f"{IMGUR}UCWGCKR.png"), # INDIO
        "`": Fab(self.indio, f"{IMGUR}nvrwu0r.png"), # INDIA
        "p": Fab(self.indio, f"{IMGUR}HeiupbP.png"), # PAJE
        ".": Fab(self.vazio, f"{IMGUR}npb9Oej.png"), # VAZIO
        "_": Fab(self.coisa, f"{IMGUR}sGoKfvs.jpg"), # SOLO
        "#": Fab(self.atora, f"{IMGUR}0jSB27g.png"), # TORA
        "@": Fab(self.barra, f"{IMGUR}tLLVjfN.png"), # PICHE
        "~": Fab(self.coisa, f"{IMGUR}UAETaiP.gif"), # CEU
        "*": Fab(self.coisa, f"{IMGUR}PfodQmT.gif"), # SOL
        "|": Fab(self.coisa, f"{IMGUR}uwYPNlz.png")  # CERCA       
        }
        """Dicionário que define o tipo e a imagem do objeto para cada elemento."""
        mapa = mapa if mapa != "" else self.mapa
        """Cria um cenário com imagem de terra de chão batido, céu e sol"""
        mapa = self.mapa
        lado = self.lado
        cena = self.v.c(fabrica["_"].imagem)
        self.ceu = self.v.a(fabrica["~"].imagem, w=lado*self.col, h=lado-10, x=0, y=0, cena=cena, vai=self.passo,
                       style={"padding-top": "10px", "text-align": "center"})
        """No argumento *vai*, associamos o clique no céu com o método **executa ()** desta classe.
           O *ceu* agora é um argumento de instância e por isso é referenciado como **self.ceu**.
        """
        sol = self.v.a(fabrica["*"].imagem, w=60, h=60, x=0, y=40, cena=cena, vai=self.executa)
        """No argumento *vai*, associamos o clique no sol com o método **esquerda ()** desta classe."""
        self.taba = {(i, j): fabrica[imagem].objeto(fabrica[imagem].imagem, x=i*lado, y=j*lado+lado, cena=cena)
            for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)}
        """Posiciona os elementos segundo suas posições i, j na matriz mapa"""
        cena.vai()
        return cena
        
    def fala(self, texto=""):
        """ O Kwarwp é aqui usado para falar algo que ficará escrito no céu.
        """
        self.ceu.elt.html = texto
        pass
        
    def sai(self, *_):
        """ O Kwarwp é aqui usado como uma vaga falsa, o pedido de sair é ignorado.
        """
        pass
        
    def ocupa(self, *_):
        """ O Kwarwp é aqui usado como um ocupante falso, o pedido de ocupar é ignorado.
        """
        pass
        
    def passo(self, *_):
        """ Ordena a execução do roteiro do índio.
        """
        # self.o_indio.esquerda()
        # self.v.executa()
        # self.o_indio.passo()

        [indio.passo() for indio in self.os_indios]

        
    def executa(self, *_):
        """ Ordena a execução do roteiro do índio.
        """
        # self.v.ativa()
        # JogoProxy.ATIVA = True
        # self.o_indio.ativa()
        # self.o_indio.executa()
        self.v.ativa()
        [indio.ativa() or indio.executa() for indio in self.os_indios]
        # self.os_indios[0].ativa()
        # self.os_indios[0].executa()
        
    def atora(self, imagem, x, y, cena):
        """ Cria uma tora na arena do Kwarwp na posição definida.

        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        
        Cria uma vaga vazia e coloca o componente dentro dela.
        """
        coisa = Tora(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa, taba=self)
        coisa.vazio.vai = lambda *_: self.o_indio.larga()
        return vaga
        
    def maloc(self, imagem, x, y, cena):
        """ Cria uma maloca na arena do Kwarwp na posição definida.

        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        
        Cria uma vaga vazia e coloca o componente dentro dela.
        """
        coisa = Oca(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa, taba=self)
        return vaga
        
    def barra(self, imagem, x, y, cena):
        """ Cria uma armadilha na arena do Kwarwp na posição definida.

        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        
        Cria uma vaga vazia e coloca o componente dentro dela.
        """
        coisa = Piche(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa, taba=self)
        return vaga
        
    def coisa(self, imagem, x, y, cena):
        """ Cria um elemento na arena do Kwarwp na posição definida.

        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        
        Cria uma vaga vazia e coloca o componente dentro dela.
        """
        coisa = Indio(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa, taba=self)
        return vaga
        
    def vazio(self, imagem, x, y, cena):
        """ Cria um espaço vazio na arena do Kwarwp na posição definida.

        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        """
        vaga = Vazio(imagem, x=x, y=y, cena=cena, ocupante=NULO, taba=self)
        """ O Kwarwp é aqui usado como um ocupante nulo, que não ocupa uma vaga vazia."""
        return vaga
        
    def indio(self, imagem, x, y, cena):
        """ Cria o personagem principal na arena do Kwarwp na posição definida.

        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        """
        self.o_indio = self.indios[0](imagem, x=1, y=0, cena=cena, taba=self, vitollino=self.v)
        """ O índio tem deslocamento zero, pois é relativo à vaga.
            O **x=1** serve para distinguir o indio de outros derivados.
        """
        self.o_indio.indio.vai = lambda *_: self.o_indio.pega()
        """o índio.vai é associado ao seu próprio metodo pega"""
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=self.o_indio, taba=self)
        self.os_indios.append(self.o_indio)
        self.indios.rotate()
        """recebe a definição do próximo índio"""
        return vaga


def main(vitollino, medidas={}, mapa=None, indios=()):
    """ Rotina principal que invoca a classe Kwarwp.
    
    :param vitollino: Empacota o engenho de jogo Vitollino.
    :param medidas: Um dicionário usado para redimensionar a tela.
    """
    # print(f"main(vitollino={vitollino} medidas={medidas}")
    JogoProxy.COMANDOS, JogoProxy.ATIVA = [], False
    # print(f"def main: {JogoProxy} vitollino {vitollino}")
    vitollino_proxy = JogoProxy(vitollino=vitollino()).cria
    # print(f"def main vitollino_proxy: {vitollino_proxy}, {vitollino_proxy()}")
    # mapa, indios = alternate()
    return Kwarwp(vitollino=vitollino_proxy, medidas=medidas, mapa=mapa, indios=indios)
        
    
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo, STYLE
    STYLE.update(width=600, height="500px")
    main(Jogo, STYLE)
