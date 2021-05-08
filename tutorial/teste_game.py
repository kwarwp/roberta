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

BRANCH_TRES_NIVEL_UM = "https://imgur.com/pYDzqJr.png" #dimensões= 169x239      *    
BRANCH_TRES_NIVEL_DOIS = "https://imgur.com/Eumtp6h.png" #dimensoes = 160x98    *
BRACO_UM_UM ="https://imgur.com/7tz9P1X.png" #dimensoes = 81x100                *
BRACO_UM_DOIS = "https://imgur.com/F6yRq5f.png" #dimensoes = 52x93              *
BRACO_UM_TRES = "https://imgur.com/MRgb5pH.png" # dimensoes = 98x85             *

CRITERIO_COR_VERMELHO = "https://imgur.com/ggv9wva.png" #domensoes = 52x52      *
CRITERIO_CIRCULO_A = "https://imgur.com/E5GTyil.png" #domensoes = 52x52         *
#CRITERIO_GRANDE = "https://imgur.com/yBD04Wg.png"
GEOMETRICO_CIRCULO_VERMELHO = "https://imgur.com/CZJ0xTb.png" #domensoes = 33x33*

from browser import document
pdiv = document["pydiv"]
pdiv.style.minHeight = "1100px"
pdiv.style.marginLeft = "-120px"
pdiv.style.marginTop = "-40px"

from _spy.vitollino.main import Cena, Elemento, STYLE

STYLE.update(width = 1920, height = '1080px') # width = 300 (default)
#STYLE["heigth"] = "300px" # min-height = "300px"

fundo_estatico        = Cena    (BACKGROUND)

tronco_base           = Elemento(TRONCO_BASE                , x =550, y=550, w=416, h=523, cena = fundo_estatico)#
ramo_nivel_tres       = Elemento(BRANCH_TRES_NIVEL_UM       , x =402, y=593, w=169, h=239, cena = fundo_estatico)#
ramo_nivel_tres__     = Elemento(BRANCH_TRES_NIVEL_DOIS     , x =433, y=830, w=160, h=98 , cena = fundo_estatico)#
ramo_nivel_tres_um    = Elemento(BRACO_UM_UM                , x =560, y=887, w=81 , h=100, cena = fundo_estatico)
ramo_nivel_tres_dois  = Elemento(BRACO_UM_DOIS              , x =640, y=410, w=52 , h=93 , cena = fundo_estatico)
ramo_nivel_tres_dois  = Elemento(BRACO_UM_TRES              , x =640, y=410, w=98 , h=85 , cena = fundo_estatico)

criterio_cor_vermelho = Elemento(CRITERIO_COR_VERMELHO      , x =640, y=410, w=52 , h=52 , cena = fundo_estatico)
criterio_circulo_A    = Elemento(CRITERIO_CIRCULO_A         , x =535, y=672, w=52 , h=52 , cena = fundo_estatico)#
geometrico_vermelho   = Elemento(GEOMETRICO_CIRCULO_VERMELHO, x =640, y=410, w=33 , h=33 , cena = fundo_estatico)


fundo_estatico.vai()