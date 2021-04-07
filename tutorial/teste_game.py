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
CRITERIO_VERMELHO = "https://i.imgur.com/KU344jS.png"
GEOMETRICO_CIRCULO = "https://i.imgur.com/Ch4uiED.png"

from _spy.vitollino.main import Cena, Elemento, STYLE

STYLE["width"] = 900 # width = 300 (default)
STYLE["heigth"] = "900px" # min-height = "300px"



fundo_estatico = Cena(BACKGROUND)
tronco_base = Elemento(TRONCO_BASE, tit="Este é o tronco da árvore",
                           style=dict(left=60, top=500), # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = fundo_estatico)
                           
fundo_estatico.vai()