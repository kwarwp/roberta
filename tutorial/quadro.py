# roberta.tutorial.quadro.py
# SPDX-License-Identifier: GPL-3.0-or-later
"""     xxxxx

.. codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto


""" O objeto é o elementoclicável de alguma cena.
"""
FUNDO = "https://img.elo7.com.br/product/original/1D27E33/painel-cenario-mundo-encantado-frete-gratis-cenario.jpg"
LIVRO = "https://comunicamack.files.wordpress.com/2016/12/livro.png"

STYLE["width"] = 900 # width = 300 (default) 
STYLE["heigth"] = "900px" # min-height = "300px


nome_da_cena = Cena(FUNDO)
nome_da_cena.vai()

texto_ = Texto(nome_da_cena, txt = "Mensagem desejada", foi = chama_elemento)
texto_.vai()

def chama_elemento(*_):
    nome_do_elemento = Elemento(LIVRO, tit="título_do_elemento", 
                       style=dict(height=60,widht=60, left=600, top=20))
    nome_do_elemento.entra(nome_da_cena)
                              
