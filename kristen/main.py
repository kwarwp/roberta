# roberta.kristen.main.py
"""     xxxxx

.. codeauthor:: Lilian <lilianes93@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""

from _spy.vitollino.main import Cena, STYLE

STYLE ["width"] = 600
STYLE ["height"] = 600

FLORESTA = "https://image.freepik.com/vetores-gratis/folhagem-de-floresta-tropical-paisagem_23-2148271243.jpg"
BORBOLETA = "https://store-images.s-microsoft.com/image/apps.2544.13768621950225582.167ba0c8-6eb8-47bb-96fe-278c89bf0dc9.ea440c13-fd1d-4705-b62c-9bfd9054b8b3?w=672&h=378&q=80&mode=letterbox&background=%23FFE4E4E4&format=jpg"
INDIO = "https://i.imgur.com/DUGXbFb.png"
OCA = "https://i.imgur.com/JzoV9GT.png"

cenaFloresta = Cena(img = FLORESTA)

nome_da_cena_meio = Cena(INDIO)
nome_da_cena_direita = Cena(BORBOLETA)
nome_da_cena_esquerda = Cena(OCA)
nome_da_cena = Cena(FLORESTA, esquerda=nome_da_cena_esquerda, direita=nome_da_cena_direita, meio=nome_da_cena_meio)

nome_da_cena_esquerda.direita = cenaFloresta
nome_da_cena_esquerda.esquerda = cenaFloresta
nome_da_cena_direita.direita = cenaFloresta
nome_da_cena_esquerda.esquerda = cenaFloresta
nome_da_cena_meio.esquerda = cenaFloresta
nome_da_cena_meio.direita = cenaFloresta

nome_da_cena.vai()