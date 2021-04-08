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
TRONCO_BASE = "https://i.imgur.com/FiV74AD.png"
BRANCH_TRES_CRITERIO = "https://i.imgur.com/E4VF4sb.png"
BRANCH_TRES_CRITERIADO = "https://i.imgur.com/AC8DivF.png"
CRITERIO_VERMELHO = "https://i.imgur.com/KU344jS.png"
GEOMETRICO_CIRCULO = "https://i.imgur.com/Ch4uiED.png"

from _spy.vitollino.main import Cena, Elemento, STYLE

STYLE["width"] = 1920 # width = 300 (default)
STYLE["heigth"] = "900px" # min-height = "300px"



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
                           
                           
                           
                           
                           
criteriado = Elemento(GEOMETRICO_CIRCULO, tit="Este é o tronco da árvore",x=100, y=245, w=100, h=100,  # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = fundo_estatico)

criterio_vermelho = Elemento(CRITERIO_VERMELHO, tit="Este é o tronco da árvore", x=100, y=350, w=100, h=100, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = fundo_estatico)
                           
#ramo_criterio_tres = Elemento(BRANCH_TRES_CRITERIO, tit="Este é o tronco da árvore", x =375, y=197, w=170, h=170, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
#                           cena = fundo_estatico)
                           
ramo_criteriado_tres = Elemento(BRANCH_TRES_CRITERIADO, tit="Este é o tronco da árvore", x =100, y=135, w=100, h=100, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = fundo_estatico)

tronco_base = Elemento(TRONCO_BASE, tit="Este é o tronco da árvore", x =100, y= 365, w=100, h=100, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = fundo_estatico)                      
                          
                           
fundo_estatico.vai()