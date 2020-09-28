# roberta.danae.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto inicial do tutorial Python.

.. codeauthor:: Carlo <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    20.09
        Uma página com uma cena.

"""
def main():
    from circus.circus import circus

    MASMORRA = {'Cahuitz': 'LO', 'Cauha': 'JN', 'Coycol': 'LS',
     'Huatlya': 'JO', 'Micpe': 'FN', 'Nenea': 'JL',
     'Pallotl': 'GS', 'Tetlah': 'JS', 'Zitllo': 'GL'}


    circus(4, MASMORRA)


from _spy.vitollino.main import STYLE, Cena

STYLE["width"] = 900 # width = 300 (default)
STYLE["height"] = "900px" # min-height = "300px"
CENA = "https://i.imgur.com/gSzqe5C.jpg"
ESQU = "https://i.imgur.com/aisVckn.jpg"
DIRE = "https://i.imgur.com/0yzM8ue.jpg"


class Tutorial:
    def __init__(self):
        esqu = Cena(ESQU)
        dire = Cena(DIRE)
        self.cena = Cena(CENA, direita=dire, esquerda=esqu)
        esqu.direita = self.cena
        dire.esquerda = self.cena
        
    def vai(self):
        self.cena.vai()


    
    
if __name__ == "__main__":
    main()
    #Tutorial().vai()

