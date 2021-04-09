# roberta.tutorial.teste_game.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto de TCC: COORDENAÇÕES LÓGICAS

.. codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

Changelog
---------
.. versionadded::    21.04
       Teste de tamanho das peças

"""
BACKGROUND = "https://i.imgur.com/15vsHKm.jpg"

TRONCO_BASE = "https://imgur.com/MvuKMHs.png"
BRACH_UM = "https://imgur.com/9HEwnOX.png"
BRANCH_TRES_CRITERIO = "https://imgur.com/Sl5USH5.png"
BRANCH_TRES_CRITERIADO = "https://imgur.com/RNrW0L9.png"

CRITERIO_AZUL= "https://imgur.com/bSutiDv.png"
CRITERIO_CIRCULO = "https://imgur.com/lWXEv57.png"
CRITERIO_GRANDE = "https://imgur.com/yBD04Wg"
GEOMETRICO_CIRCULO_AZUL = "https://imgur.com/JKHhspj.png"

from browser import document
pdiv = document["pydiv"]
pdiv.style.minHeight = "1100px"
pdiv.style.marginLeft = "-120px"
pdiv.style.marginTop = "-40px"

from _spy.vitollino.main import Cena, Elemento, STYLE

STYLE.update(width = 1920, height = '1080px') # width = 300 (default)
#STYLE["heigth"] = "300px" # min-height = "300px"



fundo_estatico = Cena(BACKGROUND)
criteriado = Elemento(GEOMETRICO_CIRCULO, tit="Este é o tronco da árvore",x=370, y=245, w = 30, h=30, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = fundo_estatico)

criterio_vermelho = Elemento(CRITERIO_VERMELHO, tit="Este é o tronco da árvore", x=450, y=350, w=20, h=20, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = fundo_estatico)
                           
#ramo_criterio_tres = Elemento(BRANCH_TRES_CRITERIO, tit="Este é o tronco da árvore", x =375, y=197, w=170, h=170, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
#                           cena = fundo_estatico)
                           
ramo_criteriado_tres = Elemento(BRANCH_TRES_CRITERIADO, tit="Este é o tronco da árvore", x =379, y=193, w=175, h=175, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = fundo_estatico)

tronco_base = Elemento(TRONCO_BASE, tit="Este é o tronco da árvore", x =300, y= 365, w = 300, h = 300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = fundo_estatico)
                           
                   
                           
fundo_estatico.vai()