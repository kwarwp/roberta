# roberta.adda.main.py
"""xxxx
..codeauthor: Isabel Hortencia Garnica <hortencia.garnica@gmail.com>

Changelog
---------
..versionadded::
    - xxx
    
"""
from _spy.vitollino.main import Cena, STYLE
STYLE["width"] = 600
STYLE["height"] = "900px"
FLORESTA = "https://imgur.com/a/vQzh2NP"
MUNDO = "https://i.imgur.com/KYGCskB.gifv"
ARCO = "https://i.imgur.com/PdAD7GC.jpg"
LAPIS = "https://i.imgur.com/U7w5CPr.png"

def flora():
    cenaFloresta = Cena(img = FLORESTA)
    
    cenaFloresta.vai()
flora()
