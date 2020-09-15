# roberta.adda.main.py
"""xxxx
..codeauthor: Isabel Hortencia Garnica <hortencia.garnica@gmail.com>

Changelog
---------
..versionadded::
    - xxx
    
"""
from _spy.vitollino.main import Cena, STYLE
STYLE["width"] = 1100
STYLE["height"] = "600px"
FLORESTA = "https://i.imgur.com/4lB1eyQ.jpg"
MUNDO = "https://i.imgur.com/KYGCskB.gifv"
ARCO = "https://i.imgur.com/PdAD7GC.jpg"
LAPIS = "https://i.imgur.com/U7w5CPr.png"

def flora():
    cenaFloresta = Cena(img = FLORESTA)
    
    cenaFloresta.vai()
flora()
