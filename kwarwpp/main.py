# roberta.kwarwpp.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Jogo para ensino de programação Python.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    20.07
        classe Vitollino.

"""
from _spy.vitollino.main import Jogo, STYLE
from kwarwp.kwarwpp import main as kwarwp_main, Indio
MAPA_INICIO = """
@.....&
.......
p.....#
.#.....
"""

class Indio(Indio):
    def executa(self):
        """ Roteiro do índio. Conjunto de comandos para ele executar.
        """
        self.direita()
        self.direita()
        self.anda()
        self.esquerda()
        self.empurra()
        

class Vitollino(Jogo):
    """ Empacota o engenho de jogo Vitollino """
    pass

def main(vitollino, medidas):
    return kwarwp_main(vitollino=vitollino, medidas=medidas, mapa=MAPA_INICIO,indios= Indio)
        
    
if __name__ == "__main__":
    main(Jogo, STYLE)
