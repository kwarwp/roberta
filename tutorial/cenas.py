# janese.cenas.imix.py
# SPDX-License-Identifier: GPL-3.0-or-later
"""     Vitollino na UNESP 2020

.. codeauthor:: Equipe Supygirls <supygirls@gmail.com>

Changelog
---------
.. versionadded::    20.08
       - Cenas;
       - Texto de abertura;
       - Elemento;
       - Texto ao clicar no elemento;
       - Importação de classes de MESMO MÓDULO

"""
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
#from samantha.main import turmaDireita
#from kristen.main import inicialesquerda
#from danae.main import Lago

FUNDO = "https://img.elo7.com.br/product/original/1D27E33/painel-cenario-mundo-encantado-frete-gratis-cenario.jpg"
LIVRO = "https://comunicamack.files.wordpress.com/2016/12/livro.png"

STYLE["width"] = 900
STYLE["heigth"] = 900

cena_fundo = Cena(FUNDO)
cena_fundo.vai()

#def cria_fundo():
    #cena_fundo = Cena(FUNDO)
    #cena_fundo.vai()
    
    
#cria_fundo()
