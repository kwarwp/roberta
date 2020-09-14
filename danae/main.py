# roberta.danae.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto inicial do tutorial Python.

.. codeauthor:: Carlo <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    20.09
        Descreva o que você adicionou no código.

"""
from _spy.vitollino.main import STYLE, Cena

STYLE["width"] = 900 # width = 300 (default)
STYLE["height"] = "900px" # min-height = "300px"
CENA = "https://i.imgur.com/gSzqe5C.jpg"


class Tutorial:
    def __init__(self):
        self.cena = Cena(CENA)
        
    def vai(self):
        self.cena.vai()
    
    
if __name__ == "__main__":
    Tutorial().vai()
