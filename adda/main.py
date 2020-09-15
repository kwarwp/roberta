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
MUNDO = "https://i.imgur.com/KYGCskB.gifv"
ARCO = "https://i.imgur.com/PdAD7GC.jpg"
LAPIS = "https://i.imgur.com/U7w5CPr.png"

mundo = Cena(MUNDO, esquerda = floresta_verde)
arco = Cena(ARCO, direita= floresta_verde)

floresta_verde = Cena(FLORESTA, direita = mundo, esquerda = arco, meio= Cena(LAPIS))
floresta_verde.vai()
