# roberta.tutorial.quadro.py
# SPDX-License-Identifier: GPL-3.0-or-later
"""     xxxxx

.. codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""
from _spy.vitollino.main import Cena, STYLE, Elemento

""" O objeto é o elementoclicável de alguma cena.
"""

STYLE["width"] = 900 # width = 300 (default) 
STYLE["heigth"] = "900px" # min-height = "300px


 

MINHA_CENA = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
MINHA_MUSICA = "https://www.youtube.com/watch?v=FuedXyc2Dro" # Extensões aceitas: mp3, mp4

nome_da_cena = Cena(MINHA_CENA)
nome_da_cena.vai()
   
nome_da_musica = Musica(MINHA_MUSICA, loop = True, autoplay = True)

                              
