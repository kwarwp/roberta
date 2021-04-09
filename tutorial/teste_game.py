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

BRANCH_TRES_CRITERIO_NIVEL_UM = "https://imgur.com/RNrW0L9.png"
BRANCH_TRES_CRITERIADO_NIVEL_2 = "https://imgur.com/Sl5USH5.png"
BRANCH_UM_CRITERIADO = "https://imgur.com/9HEwnOX.png"

CRITERIO_AZUL = "https://imgur.com/bSutiDv.png"
CRITERIO_CIRCULO = "https://imgur.com/lWXEv57.png"
CRITERIO_GRANDE = "https://imgur.com/yBD04Wg.png"
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

criteriado = Elemento(GEOMETRICO_CIRCULO_AZUL, x=370, y=245, w = 30, h=30, cena = fundo_estatico)

criterio_azul = Elemento(CRITERIO_AZUL, x=450, y=350, w=20, h=20,  cena = fundo_estatico)
criterio_circulo = Elemento(CRITERIO_CIRCULO, x=450, y=350, w=20, h=20,  cena = fundo_estatico)
criterio_grande = Elemento(CRITERIO_GRANDE, x=450, y=350, w=20, h=20,  cena = fundo_estatico)

       
ramo_criteriado_tres = Elemento(BRANCH_TRES_CRITERIADO,  x =379, y=193, w=175, h=175,cena = fundo_estatico)

ramo_criterio_tres = Elemento(BRANCH_TRES_CRITERIO,  x =379, y=193, w=175, h=175,cena = fundo_estatico)

ramo_criterio_um = Elemento(BRANCH_UM_CRITERIADO,  x =379, y=193, w=175, h=175,cena = fundo_estatico)


tronco_base = Elemento(TRONCO_BASE, x =300, y= 365, w = 300, h = 300,  cena = fundo_estatico)
                           
                   
                           
fundo_estatico.vai()