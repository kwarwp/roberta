# roberta.naomi.main.py
"""     xxxxx

.. codeauthor:: Angelica <.........@gmail.com>
.. codeauthor:: Rodrigo Esquinelato <resquinelato@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""
#NSLO
from circus.circus import circus

def desafio():
    TOPO_ESQUERDA = "LS"
    TOPO_DIREITA = "LO"
    TOPO_CENTRO = "JN"
    MEIO_ESQUERDA, CENTRO, MEIO_DIREITA = "JO", "FN", "JL"
    FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA =  "GS", "JS", "GL"

    # O comando abaixo voce vai entender no próximo desafio
    circus(1, [[TOPO_ESQUERDA, TOPO_CENTRO, TOPO_DIREITA], [MEIO_ESQUERDA, CENTRO,
            MEIO_DIREITA], [FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA]])

if __name__ == "__main__":
    desafio()