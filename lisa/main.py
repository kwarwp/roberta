# roberta.lisa.main.py
"""     xxxxx

.. codeauthor:: Luiza <luizaanjo2007@gmail.com>
.. codeauthor:: Rodrigo Esquinelato <resquinelato@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""
# Na linha 14 você chamou o _spy! O import é apenas from circus.circus import circus
from _spy.circus.circus import circus

def desafio0():
    TOPO_ESQUERDA = "AN"
    TOPO_DIREITA = "AN"
    TOPO_CENTRO = "AN"
    MEIO_ESQUERDA, CENTRO, MEIO_DIREITA = "AN", "AN", "AN"
    FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA =  "AN", "AN", "AN"

    # O comando abaixo voce vai entender no próximo desafio
    circus(1, [[TOPO_ESQUERDA, TOPO_CENTRO, TOPO_DIREITA], [MEIO_ESQUERDA, CENTRO,
            MEIO_DIREITA], [FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA]])
        

if __name__ == "__main__":
     desafio0()