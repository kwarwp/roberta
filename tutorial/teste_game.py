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

TRONCO_BASE = "https://imgur.com/PMAoGcd.png"

BRANCH_TRES_NIVEL_ = "https://imgur.com/Eumtp6h.png"
BRANCH_TRES_UM_UM ="https://imgur.com/7tz9P1X.png"
BRANCH_TRES_UM_DOIS = "https://imgur.com/F6yRq5f.png"
BRANCH_TRES_UM_TRES = "https://imgur.com/MRgb5pH.png"

CRITERIO_VERMELHO = "https://imgur.com/ggv9wva.png"
CRITERIO_CIRCULO = "https://imgur.com/E5GTyil.png"
#CRITERIO_GRANDE = "https://imgur.com/yBD04Wg.png"
GEOMETRICO_CIRCULO_VERMELHO = "https://imgur.com/CZJ0xTb.png"

from browser import document
pdiv = document["pydiv"]
pdiv.style.minHeight = "1100px"
pdiv.style.marginLeft = "-120px"
pdiv.style.marginTop = "-40px"

from _spy.vitollino.main import Cena, Elemento, STYLE

STYLE.update(width = 1920, height = '1080px') # width = 300 (default)
#STYLE["heigth"] = "300px" # min-height = "300px"

fundo_estatico = Cena(BACKGROUND)

tronco_base = Elemento(TRONCO_BASE, x =550, y= 675, w = 416, h = 523,  cena = fundo_estatico)
ramo_nivel_tres = Elemento(BRANCH_TRES_NIVEL_,  x =67, y=50, w=160, h=98,cena = fundo_estatico)
ramo_nivel_tres_um = Elemento(BRANCH_TRES_UM_UM,  x =640, y=410, w=81, h=100,cena = fundo_estatico)
ramo_nivel_tres_dois = Elemento(BRANCH_TRES_UM_DOIS,  x =640, y=410, w=52, h=93,cena = fundo_estatico)
ramo_nivel_tres_dois = Elemento(BRANCH_TRES_UM_TRES,  x =640, y=410, w=98, h=85,cena = fundo_estatico)


                           
fundo_estatico.vai()