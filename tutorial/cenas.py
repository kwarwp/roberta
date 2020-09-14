# janese.cenas.imix.py
# SPDX-License-Identifier: GPL-3.0-or-later
"""     Vitollino na UNESP 2020

.. codeauthor:: Equipe Supygirls <supygirls@gmail.com>

Changelog
---------
.. versionadded::    20.08
       - Cenas;
       - Texto de abertura;
       - Elemento;
       - Texto ao clicar no elemento;
       - Importação de classes de MESMO MÓDULO

"""
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
#from samantha.main import turmaDireita
#from kristen.main import inicialesquerda
#from danae.main import Lago

MUNDO = "http://www.pngall.com/wp-content/uploads/1/World-Map.png"
ARCO = "https://i.ytimg.com/vi/ynxZPR27gi4/maxresdefault.jpg"
LAPIS = "https://i.ytimg.com/vi/5igYewGEoFo/maxresdefault.jpg"



STYLE["width"] = 900
STYLE["heigth"] = 900

cena_direita = Cena(ARCO)
cena_esquerda =Cena(LAPIS)

cena_fundo = Cena(FUNDO, esquerda=cena_esquerda, direita=cena_direita)
cena_fundo.vai()

#def cria_fundo():
    #cena_fundo = Cena(FUNDO)
    #cena_fundo.vai()
    
    
#cria_fundo()
