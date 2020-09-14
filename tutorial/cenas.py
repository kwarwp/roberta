# janese.cenas.imix.py
# SPDX-License-Identifier: GPL-3.0-or-later
"""     


"""
from _spy.vitollino.main import Cena, STYLE

MUNDO = "http://www.pngall.com/wp-content/uploads/1/World-Map.png"
ARCO = "https://i.ytimg.com/vi/ynxZPR27gi4/maxresdefault.jpg"
LAPIS = "https://i.ytimg.com/vi/5igYewGEoFo/maxresdefault.jpg"


STYLE["width"] = 900
STYLE["heigth"] = "900px"

#cena_direita = Cena(ARCO)
#cena_esquerda =Cena(LAPIS)
#cena_fundo = Cena(MUNDO, esquerda=cena_esquerda, direita=cena_direita)

#cena_fundo = Cena(FUNDO)
#cena_fundo.vai()

def cria_fundo(*_):
    cena_direita = Cena(ARCO)
    cena_esquerda =Cena(LAPIS)
    cena_fundo = Cena(MUNDO, direita=cena_direita, esquerda=cena_esquerda)
    cena_fundo.vai()
    
    
cria_fundo()
