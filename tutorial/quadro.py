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
import random

""" O objeto é o elementoclicável de alguma cena.
"""
FUNDO = "https://img.elo7.com.br/product/original/1D27E33/painel-cenario-mundo-encantado-frete-gratis-cenario.jpg"
LIVRO = "https://comunicamack.files.wordpress.com/2016/12/livro.png"

def embaralha_texto():
    texto = list("Fui na feira não sabia o que comprar. Comprei uma cadeira pra Olivia se sentar")
    print(texto.sort())

def funcao_de_acao_do_botao(event = None):
    #Função chamada no clique resultará na chamada de um texto
    texto = list("Fui na feira não sabia o que comprar. Comprei uma cadeira pra Olivia se sentar")
    anagrama = random.shuffle(texto)
    texto_surpresa = Texto(nome_da_cena, txt = anagrama)
    texto_surpresa.vai()
    cla = input("Qual a frase real??")
    
        
    

nome_da_cena = Cena(FUNDO)
nome_da_cena.vai()
nome_do_elemento = Elemento(LIVRO, tit="título_do_elemento", 
                            style=dict(height=60,widht=60, left=600, top=20), # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                            cena = nome_da_cena)
                              
nome_do_elemento.elt.bind("click", funcao_de_acao_do_botao)
