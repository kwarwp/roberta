# roberta.sarah.main.py
"""     xxxxx

.. codeauthor:: Mariana Bittencourt <cmarianab3@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""

from_spy.vitollino.main import Cena, STYLE

FLORESTA = "https://viajarverde.com.br/wp-content/uploads/2016/07/amazon-rainforest-wallpaper-4-810x506.jpg"
MUNDO = "https://exame.com/wp-content/uploads/2016/09/size_960_16_9_terral9.jpg"
ARCO = "https://static.todamateria.com.br/upload/56/e1/56e1a50b15b88-arco-iris.jpg"
LAPIS = "https://http2.mlstatic.com/adesivo-parede-quarto-infantil-lapis-cor-onda-colorida-480-D_NQ_NP_765610-MLB31210291228_062019-F.jpg"

STYLE["width"] = 900
STYLE["height"] = "900px"

cena_direita = Cena(ARCO)
cena_esquerda = Cena (LAPIS)
cena_fundo = Cena(MUNDO, esquerda=cena_esquerda, direita=cena_cireita)

cena_esquera.direita = cena_fundo
cena_direita.esquerda = cena_fundo
cena_fundo.vai()

