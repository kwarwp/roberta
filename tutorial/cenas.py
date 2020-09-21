# janese.cenas.imix.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Nome Sobrenome <mail@local.tipo>

Changelog
---------
.. versionadded::    20.09
        Descreva o que você adicionou no código.

"""
from _spy.vitollino.main import Cena, STYLE, Elemento

MUNDO = "http://www.pngall.com/wp-content/uploads/1/World-Map.png"
ARCO = "https://i.ytimg.com/vi/ynxZPR27gi4/maxresdefault.jpg"
LAPIS = "https://i.ytimg.com/vi/5igYewGEoFo/maxresdefault.jpg"
ELEMENTO="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.redd.it%2Fxgorxiy1z4s11.png"


STYLE["width"] = 900
STYLE["heigth"] = "900px"

cena_direita = Cena(ARCO)
cena_esquerda =Cena(LAPIS)
cena_fundo = Cena(MUNDO, esquerda=cena_esquerda, direita=cena_direita)
cena_esquerda.esquerda = cena_fundo
elemento = Elemento(ELEMENTO, w=100, h=100,x=150,y=200,vai=cena_esquerda)
elemento.entra(cena_fundo)
#cena_fundo = Cena(MUNDO)
cena_fundo.vai()

#def cria_fundo(*_):
    #cena_direita = Cena(ARCO)
    #cena_esquerda =Cena(LAPIS)
    #cena_fundo = Cena(MUNDO, direita=cena_direita, esquerda=cena_esquerda)
    #cena_fundo.vai()
        
#cria_fundo()
