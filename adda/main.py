# roberta.adda.main.py
"""xxxx
..codeauthor: Isabel Hortencia Garnica <hortencia.garnica@gmail.com>

Changelog
---------
..versionadded::
    - xxx
    

from _spy.vitollino.main import Cena, STYLE, Elemento
STYLE["width"] = 1100
STYLE["height"] = "600px"
FLORESTA = "https://i.imgur.com/4lB1eyQ.jpg"
MUNDO = "https://i.imgur.com/LpWmClc.png"
ARCO = "https://i.imgur.com/PdAD7GC.jpg"
LAPIS = "https://i.imgur.com/U7w5CPr.png"
FIM = "https://i.imgur.com/EJpEunb.gif"
LINUX = "https://i.imgur.com/ym0HMHC.png"

def flora():
    cenaFloresta = Cena(img = FLORESTA)
    
    cenaMundo = Cena(img = MUNDO)
    cenaFloresta.direita = cenaMundo
    cenaMundo.vai()
    
    cenaMundo.esquerda = cenaFloresta
    
    cenaArco = Cena(img = ARCO)
    cenaFloresta.esquerda = cenaArco
    cenaArco.vai()    
    cenaArco.direita = cenaFloresta
    
    
    cenaLapis = Cena(img = LAPIS) 
    cenaFloresta.meio = cenaLapis   
    cenaLapis.vai()    
    cenaLapis.esquerda = cenaFloresta
        
    cenaFloresta.vai()
flora()
"""
x = "ola"

def mostra_x():
    x = "eeee"
    j = "oooo"
    print(x)
print(x)









