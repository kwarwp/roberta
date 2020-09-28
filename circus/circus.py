# patricia.danae.circus.py
# SPDX-License-Identifier: GPL-3.0-or-later
"""  Circus: Circo Voardor da Programção Python

.. codeauthor:: Carlo E.T Oliveira <mail@local.tipo>

Changelog
---------
.. versionadded::    20.09
        Descreva o que você adicionou no código.

"""
from random import shuffle
RTAZ, SFAZ, COUNT, KEYS = "CIRCUS_RTAZ", "CIRCUS_SFAZ", "CIRCUS_COUNT", "CIRCUS_KEYS"
LADO = 80

class Letra:
    TRANSP= "https://i.imgur.com/npb9Oej.png"
    def __init__(self, cena, x, y, lt="A"):
        OFF = 0x24B6 - ord("A")
        la = Aldeia.J.a(self.TRANSP, x=x+15, y=y ,w=LADO*90//100, h=LADO*90//100, style={'font-size': f'{LADO//2}pt'}, cena=cena)
        la.elt.html = chr(OFF+ord(lt))
        
        
class Piso:
    #ALDEIA = "https://i.imgur.com/Gqoucvd.png"
    #ALDEIA = "https://i.imgur.com/UCWGCKR.png"
    ALDEIA = "https://i.imgur.com/xsjhNjh.png"
    def __init__(self, cena, x, y, ai="NA"):
        azz = {key: nk*90 for nk, key in enumerate("NLSO")}
        pos = {key: (-(nk%4)*LADO, -(nk//4)*LADO) for nk, key in enumerate("ABCDEFGHIJKL")}
        tile = LADO
        az = azz[ai[1]]
        self.elt = Aldeia.J.a(self.ALDEIA, x=x, y=y, w=tile, h=tile, cena=cena, style=dict(transform=f"rotate({az}deg)"))
        self.elt.pos = pos[ai[0]]
        self.elt.siz = (4*LADO, 3*LADO)
    def possize(self, pos, siz=None):
        self.elt.pos = pos
        self.elt.siz = siz if siz else self.elt.siz
        
class Aldeia:
    STOR = None
    ALDEIA = "https://i.imgur.com/Gqoucvd.png"
    ESPRIT = "https://i.imgur.com/XFVLtJE.png"
    MAPING = "https://i.imgur.com/MRmfpAv.png"
    YARA = "https://i.imgur.com/RfLJEhs.png"
    TRANSP= "https://i.imgur.com/npb9Oej.png"
    J = None
    OK_AZIM=list("NLSO")
    RT_AZIM="NLSO"
    SF_AZIM="NLSO"
    ORDERED_KEYS = [['Coycol', 'Cauha', 'Tetlah'],
                    ['Huatlya', 'Zitllo', 'Micpe'],
                    ['Nenea', 'Cahuitz', 'Pallotl']]
    KEYS = None
    MASMORRA = {'Cahuitz': 'AN', 'Cauha': 'BN', 'Coycol': 'CN',
     'Huatlya': 'DN', 'Micpe': 'EN', 'Nenea': 'FN',
     'Pallotl': 'GN', 'Tetlah': 'HN', 'Zitllo': 'IN'}

    @staticmethod
    def shuffle_keys():
        #keys = [key for line in Aldeia.ORDERED_KEYS for key in line]
        keys = Aldeia.STOR[KEYS].split()
        count = Aldeia.STOR[COUNT]
        count = count[:-1]
        rtazim, sfazim = Aldeia.STOR[RTAZ], list(Aldeia.STOR[SFAZ])
        if count == "":
            shuffle(keys)
            rtazim = rtazim[1:] + rtazim[0]
            shuffle(sfazim)
            count = "@@@"
            Aldeia.STOR[RTAZ] = Aldeia.RT_AZIM = rtazim
            Aldeia.STOR[SFAZ] = Aldeia.SF_AZIM = "".join(sfazim)
            Aldeia.STOR[KEYS] = " ".join(keys)
        Aldeia.STOR[COUNT] = count
        Aldeia.KEYS = [keys[n:n+3] for n in range(0,9,3)]
    #COUNT = 2
    #ALDEIA = "https://i.imgur.com/UCWGCKR.png"
    def __init__(self, j):
        Aldeia.J = j
        tile = 100
        self.shuffle_keys = self.ORDERED_KEYS[:]
        clique = j.c()
        self.cena = cena = j.c("https://i.imgur.com/sGoKfvs.jpg", direita=clique)
        clique.vai = lambda *_: self.desafio4(self.MASMORRA)
        self.logger = j.a(self.TRANSP, x=0, y=500, w=900, h=100, cena=cena)
        # self.guia()
        self.desafios = [self.guia, self.desafio0, self.desafio0, self.desafio1, self.desafio2,
                         self.desafio3, self.desafio4, self.desafio5]
        cena.vai()
    def log(self, log):
        # print(log)
        self.logger.elt.html = log
    def guia(self, tipo=0):
        cena = self.cena
        gap = (LADO*110)//100
        big = ("LS JN HN JN HN KO HO AN FN FN BN IL JO DO AO BL DO JL IO AO DS DN CL HL GS JS HS HS JS GL".split(), 6)
        small = ("AN DN DS CN IN HN HN AS IO KN KL KO GS DS DN KN".split(), 4)
        tiny = ("LS JN LO JO FN JL GS JS GL".split(), 3)
        planta = [tiny, small, big]
        layout, siz = planta[tipo]
        a = [Piso(cena, nk%2*gap, nk//2*gap, ai+"N" ) for nk, ai in enumerate("ABCDEFGHIJKL")]
        c = [Piso(cena, int(3.5 *LADO)+nk%siz*LADO, nk//siz*LADO, ai ) for nk, ai in enumerate(layout)]
        d = [Letra(cena, nk%2*gap, nk//2*gap, lt ) for nk, lt in enumerate("ABCDEFGHIJKL")]
        e = [Piso(cena, int(2.2*LADO)+nk%1*gap, 50+nk//1*gap, "A"+ai ) for nk, ai in enumerate("NLSO")]
        #Letra(cena, 0, 0, "A")
        e = [Letra(cena, int(2.2*LADO)+nk%1*gap, 50+nk//1*gap, lt ) for nk, lt in enumerate("NLSO")]
    def todos(self):
        cena = self.cena
        big = "LS JN HN JN HN KO HO AN FN FN BN IL JO DO AO BL DO JL IO AO DS DN CL HL GS JS HS HS JS GL".split()
        small = "AN DN DS CN IN HN HN AS IO KN KL KO GS DS DN KN".split()
        # a = [Piso(cena, nk%4*150, nk//4*150, ai+"N" ) for nk, ai in enumerate("ABCDEFGHIJKL")]
        b = [Piso(cena, nk%6*100, nk//6*100, ai ) for nk, ai in enumerate(big)]
        c = [Piso(cena, 600+nk%3*100, nk//3*100, ai ) for nk, ai in enumerate("LS JN LO JO FN JL GS JS GL".split())]
        #     for x in range(4) for y in range(3)]
        D = [Piso(cena, 600+nk%3*100, 300+nk//3*100, ai ) for nk, ai in enumerate("AN JN BN DO EO DO KL HS KN".split())]
        # b = [spr(a[x*3+y], x, y) for x in range(4) for y in range(3)]
        D = [Piso(cena, 900+nk%4*100, nk//4*100, ai ) for nk, ai in enumerate(small)]
        j.a(self.ESPRIT, x=220, y=220,w=60, h=60, cena=cena)
        j.a(self.MAPING, x=420, y=220,w=60, h=60, cena=cena)
        j.a(self.YARA, x=520, y=20,w=60, h=60, cena=cena)
        
    def desafio0(self, solucao):
        c = [Piso(self.cena, 10*LADO+i*LADO, j*LADO, ai ) for j, linha in enumerate(solucao) for i, ai in enumerate(linha)]
        
    def desafio1(self, solucao):
        c = [[solucao[ai] for ai in linha] for linha in self.ORDERED_KEYS]
        self.desafio0(c)
        
    def desafio2(self, solucao):
        c = [[solucao[ai] for ai in linha] for linha in Aldeia.KEYS]
        self.desafio0(c)
        return c
        
    def desafio3(self, solucao):
        self.desafio2(solucao)
        Aldeia.shuffle_keys()
        #self.log(f"COUNT{Aldeia.STOR[COUNT]} XXkeysXX {Aldeia.KEYS}")
        
    def desafio4(self, solucao):
        Aldeia.shuffle_keys()
        solucao = {key: ladrilho + Aldeia.OK_AZIM[Aldeia.RT_AZIM.index(azimute)]
                   for key, (ladrilho, azimute) in solucao.items()}
        c = self.desafio2(solucao)
        #self.log(f"COUNT: {Aldeia.STOR[COUNT]} st {Aldeia.STOR[SFAZ]} rt {Aldeia.STOR[RTAZ]} XXsolXX {c}  {Aldeia.KEYS}")
        #self.log(f"COUNT{Aldeia.STOR[COUNT]} XXkeysXX {}")
        
    def desafio5(self, solucao):
        Aldeia.shuffle_keys()
        solucao = {key: ladrilho + Aldeia.OK_AZIM[Aldeia.SF_AZIM.index(azimute)]
                   for key, (ladrilho, azimute) in solucao.items()}
        self.desafio2(solucao)
        #self.log(f"COUNT{Aldeia.STOR[COUNT]} XXkeysXX {Aldeia.KEYS} XXsolXX {solucao}")

        
    def circus(self, desafio, solucao, tipo=0):
        tipo = [0,0,2,0,0,0,0,0,0,0][tipo]
        self.guia(tipo)
        self.desafios[desafio](solucao)
        
        # b = [spr(a[x*4+y],x,y) for x in range(4) for y in range(3)]
        #a[0].siz = (400, 300)
        #a[0].entra(cena)
def circus(desafio, solucao, tipo=0):
    from _spy.vitollino.main import Jogo, STYLE
    from browser.session_storage import storage
    Aldeia.STOR = storage
    try: 
        _ = Aldeia.STOR[COUNT]
        _ = Aldeia.STOR[RTAZ]
        _ = Aldeia.STOR[SFAZ], Aldeia.STOR[KEYS]
    except:
        Aldeia.STOR[COUNT] = ""
        Aldeia.STOR[RTAZ] = Aldeia.RT_AZIM
        Aldeia.STOR[SFAZ] = Aldeia.SF_AZIM
        Aldeia.STOR[KEYS] = " ".join([key for line in Aldeia.ORDERED_KEYS for key in line])
        Aldeia.KEYS = Aldeia.STOR[KEYS]
    #Aldeia.shuffle_keys()
    STYLE.update(width=1300, height="650px")
    #Aldeia(Jogo())
    Aldeia(Jogo()).circus(desafio, solucao, desafio)
        
def desafio0():
    TOPO_ESQUERDA = "AN"
    TOPO_DIREITA = "AN"
    TOPO_CENTRO = "AN"
    MEIO_ESQUERDA, CENTRO, MEIO_DIREITA = "AN", "AN", "AN"
    FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA =  "AN", "AN", "AN"

    # O comando abaixo voce vai entender no próximo desafio
    circus(1, [[TOPO_ESQUERDA, TOPO_CENTRO, TOPO_DIREITA], [MEIO_ESQUERDA, CENTRO,
            MEIO_DIREITA], [FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA]])
        
def desafio1():
    MASMORRA = [[ "AN", "AN", "AN", "AN", "AN", "AN"],
                [ "AN", "AN", "AN", "AN", "AN", "AN"],
                [ "AN", "AN", "AN", "AN", "AN", "AN"],
                [ "AN", "AN", "AN", "AN", "AN", "AN"],
                [ "AN", "AN", "AN", "AN", "AN", "AN"]
                ]

    circus(2, MASMORRA, 2)
        
        
def desafio2(lev=3):

    MASMORRA = {'Cahuitz': 'AN', 'Cauha': 'BN', 'Coycol': 'CN',
     'Huatlya': 'DN', 'Micpe': 'EN', 'Nenea': 'FN',
     'Pallotl': 'GN', 'Tetlah': 'HN', 'Zitllo': 'IN'}

    circus(lev, MASMORRA)
    

if __name__ == "__main__":
    desafio0()
    desafio1()
    desafio2()