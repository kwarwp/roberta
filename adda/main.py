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


from _spy.vitollino.main import Cena
#Variavel global
VARIAVEL = "https://i.imgur.com/4lB1eyQ.jpg"

def ambiente():
    #variavel local
    VARIAVEL = "https://i.imgur.com/LpWmClc.png"
    floresta = Cena(VARIAVEL)
    floresta.vai()
    
ambiente()

numero = 3

def verifica():
    if numero > 5:
        print("três é maior que cinco")
    elif numero == 5:
        print("opa! Igualdade")
    else:
        print("numero não é maior que cinco")

#verifica()
animais = ["macaco", "aguia", "leao"]

for x in animais:
    print(x)
    if x == "leao":
        break
    #print(x)
"""

for x in range(9):
    print(x)






