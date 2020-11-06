# roberta.tutorial.quadro.py
# SPDX-License-Identifier: GPL-3.0-or-later
"""     xxxxx

.. codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""
from _spy.vitollino.main import Cena, STYLE, Texto


""" O objeto é o elementoclicável de alguma cena.
"""
FUNDO =
LIVRO = "https://comunicamack.files.wordpress.com/2016/12/livro.png"

STYLE["width"] = 900 # width = 300 (default) 
STYLE["heigth"] = "900px" # min-height = "300px


MINHA_CENA =  "https://img.elo7.com.br/product/original/1D27E33/painel-cenario-mundo-encantado-frete-gratis-cenario.jpg"
   
nome_da_cena = Cena(MINHA_CENA)
nome_da_cena.vai()
   
dicionario = dict(A=10, B=20)
texto = Texto(nome_da_cena, txt = "escolha", foi = foi, A=""10",B="20")
texto.vai()

def foi(l):
    r = Texto(nome_da_cena, txt=dicionario[l])
    r.vai()

                              
