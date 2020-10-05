# roberta.kwarwpp.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
# roberta.kwarwp.main.py
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

MOANGEKO = """
.@.........
...........
.....#.¨...
...........
.....^.....

"""
FOR = """

|||||||||||||
|^.########.&
|||||||||||||

"""
APII = """
|||||||||||||
||..........|
||.||||||||.|
||......#&|.|
|||||||||||.|
|^.¨........|
|||||||||||||
"""

APO = """
|||||.|||.|||
|.|||¨¨..¨..|
|#|.|.|.|.|#|
|^|¨..|...|.&
|||.|||||||||
"""


class Moangeko(Indio):
    def executa(self):
        """
            Conjunto de comandos que o índio executa:
        """
        self.anda()
        self.direita()
        self.anda()
        self.anda()
        self.esquerda()
        self.empurra()
        self.empurra()
        self.direita()
        self.anda()
        self.esquerda()
        self.anda()
        self.esquerda()
        self.empurra()
        self.empurra()

class For(Indio):
    def executa(self):
        """ Ajude o indio a chegar na oca.
        
            CONSELHO DO PAGÉ:
               "Há um enigma de meu tatara avô que sempre me ajudou a fazer tudo mais rápido:
                SE PADRÕES você encontrar INVOQUE o espírito dos Laços CORRETAMENTE e ele te ajudará:
                     for etapas in range(?):
                         self.o_que_você_deseja()"
        """
        self.direita()
        
class Apii(Indio):
    def executa(self):
        """ Ajude o indio a chegar na oca.
        
            CONSELHO DO PAGÉ:
               "Não tente levantar a pedra. Faz mal pro umbigo"
        """
        
        self.empurra()



class Vitollino(Jogo):
    """ Empacota o engenho de jogo Vitollino """
    pass

def main(vitollino, medidas):
    return kwarwp_main(vitollino=vitollino, medidas=medidas, mapa=MOANGEKO , indios=(Moangeko,))
        
    
if __name__ == "__main__":
    main(Jogo, STYLE)
