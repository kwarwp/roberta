# roberta.adda.main.py
"""xxxx
..codeauthor: Isabel Hortencia Garnica <hortencia.garnica@gmail.com>

Changelog
---------
..versionadded::
    - xxx
    
"""
from _spy.vitollino.main import Cena, STYLE
STYLE["width"] = 900
STYLE["height"] = "900px"
FLORESTA = "https://imgur.com/a/vQzh2NP"
MUNDO = ""
ARCO = ""
LAPIS = ""

mundo = Cena(MUNDO, esquerda = floresta_verde)
arco = Cena(ARCO, direita= floresta_verde)

floresta_verde = Cena(FLORESTA, direita = mundo, esquerda = arco, meio= Cena(LAPIS))
floresta_verde.vai()
