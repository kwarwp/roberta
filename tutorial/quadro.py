# roberta.tutorial.quadro.py
# SPDX-License-Identifier: GPL-3.0-or-later
"""     xxxxx

.. codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""
from _spy.vitollino.main import Cena, STYLE 

STYLE["width"] = 900 
STYLE["heigth"] = "900px" 

FLORESTA = "https://upload.wikimedia.org/wikipedia/commons/4/4c/Po%C3%A7a_das_Asas%2C_floresta%2C_concelho_da_Horta%2C_ilha_do_Faial%2C_A%C3%A7ores%2C_Portugal.JPG"
MUNDO = "http://www.pngall.com/wp-content/uploads/1/World-Map.png"
ARCO = "https://i.ytimg.com/vi/ynxZPR27gi4/maxresdefault.jpg"
LAPIS = "https://i.ytimg.com/vi/5igYewGEoFo/maxresdefault.jpg"



def ambiente():
    self.floresta_verde = Cena(FLORESTA, direita = self.mundo, esquerda = arco, meio = lapis)
    self.mundo = Cena(MUNDO, esquerda = floresta_verde)
    self.floresta_verde.vai()
    
ambiente()





