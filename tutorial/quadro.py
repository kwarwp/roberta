# roberta.tutorial.quadro.py
# SPDX-License-Identifier: GPL-3.0-or-later
"""     xxxxx

.. codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""
#from patricia.danae.circus import Letra, Piso, Aldeia, circus
from circus.circus import circus


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