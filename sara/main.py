# roberta.sara.main.py
"""     xxxxx

.. codeauthor:: marco <marcolemosss@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""

from _spy.vitollino.main  import Cena, STYLE

STYLE["width"] = 900 # width = 300 (default)
STYLE["heigth"] = "900px" # min-height = "300px"

MUNDO= "https://img.elo7.com.br/product/zoom/2464D79/quadro-poster-mapa-mundi-bandeiras-quadro.jpg"
ARCO= "http://nsrainha.com.br/content/uploads/Artigo-Arco-iris-20082018-1.jpg"
LAPIS= "https://blog.grafittiartes.com.br/wp-content/uploads/2019/03/shutterstock_318381038.jpg"
ELEMENTO= "https://www.ourolux.com.br/blog/wp-content/uploads/2019/06/acampar.jpg"

acamp_meio = Cena(ELEMENTO)
arco_direito = Cena(ARCO)
lapis_esquerda = Cena(LAPIS)
nome_cena = Cena(MUNDO, esquerda=lapis_esquerda, direita = arco_direito, meio = acamp_meio)
nome_cena.esquerda = Cena(MUNDO)

nome_cena.vai()