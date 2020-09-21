

"""     xxxxx

.. codeauthor:: Angelica Zumpichiatti <angelicazumpichiatti@yahoo.com.br>

Changelog
---------
.. versionadded::    
       - xxx
"""     
numero_um=1
numero_dois=2
letras = "Oi! Tudo bom?"

operacao = numero_um + numero_dois

print(operacao)

operacao_sub = numero_um - numero_dois

print(operacao_sub)

multiplica = numero_um * numero_dois

print(multiplica)

from _spy.vitollino.main import Cena.STYLE
STYLE["width"] = 900 
STYLE["heigth"] = "900px" 

FLORESTA = "https://cdn4.ecycle.com.br/cache/images/2018-07/50-650-floresta-amazonica.jpg"
MUNDO = "https://exame.com/wp-content/uploads/2016/09/size_960_16_9_terral9.jpg"
ARCO = "https://observatoriog.bol.uol.com.br/wordpress/wp-content/uploads/2019/07/Yoast-rainbow-songs-for-kids.jpg"
LAPIS = "https://produtosassistivos.com.br/wp-content/uploads/2018/08/mcr0011-lapis-de-cor-grosso-136.jpg"

mundo = Cena (MUNDO)
arco = Cena (ARCO)

floresta_verde = Cena(FLORESTA, direita = mundo, esquerda = arco, meio = Cena (LAPIS))
floresta_verde.vai()



